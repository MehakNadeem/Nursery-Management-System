from flask import Flask, request, render_template, jsonify, json, make_response, send_file, flash, session, redirect
from flask_session import Session
from db_classes import *
from model import *
from templates.Admin.public import *
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# configure app.config to fetch configuration from config.py
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]
Session(app)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/addProduct', methods = ["GET","POST"])
def addProduct():
    """route to add product"""
    if request.method == "POST":
        name = request.form["productName"]
        color = request.form["ProductColor"]
        quantity = request.form["productQuantity"]
        price = request.form["ProductPrice"]
        category = request.form["productcategory"]
        subCategory = request.form["ProductSubCategory"]
        description = request.form["ProductDescription"]
        image = request.files["productImage"]
        # Save the image to the UPLOAD_FOLDER
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        prod = Product(name,price,quantity,color,category,subCategory,description,image.filename)
        db = ProductModel()
        status = db.insertProduct(prod)
        if status:
            return render_template("Admin/Add Product.html",msg = "Added successfully")
        else:
            return render_template("Admin/Add Product.html")
    else:
        return render_template("Admin/Add Product.html")

@app.route('/productsReport')
def productsReport():
    """route to show products report"""
    db = ProductModel()
    product_list = db.getProducts()
    if product_list is not None:
        return render_template("Admin/Product_listing.html", products = product_list)


@app.route('/userProfile')
def showUserProfile():
    """route to show user profile info"""
    #uemail = session["uemail"]
    #if uemail is None:
       #return render_template("login.html")
    #else
    db_usr = UserModel()
    usr_id = db_usr.getUserID(uemail)
    db_cust = CustomerModel()
    cust_id, customerData = db_cust.getCustomerByUserID(usr_id)
    db_order = OrdersModel()
    order_list = db_order.getOrdersByCustomerID(cust_id)
    if order_list is not None:
        return render_template("accountinfo.html", customer = customerData, orders = order_list)
    else:
        return render_template("accountinfo.html", customer = customerData)

@app.route('/Nfertilizer')
def showNFertilizer():
    """route to show fertilizers"""
    db = ProductModel()
    fertilizer_list = db.getFertilizer("fertilizers", "nitrogen")
    if fertilizer_list is not None:
        return render_template("fertilizer.html", fertilizers = fertilizer_list, fertilizerName = "Nitrogen")

@app.route('/PHfertilizer')
def showPHFertilizer():
    """route to show fertilizers"""
    db = ProductModel()
    fertilizer_list = db.getFertilizer("fertilizers", "phosphorus")
    if fertilizer_list is not None:
        return render_template("fertilizer.html", fertilizers = fertilizer_list, fertilizerName = "Phosphorus")

@app.route('/Pfertilizer')
def showPFertilizer():
    """route to show fertilizers"""
    db = ProductModel()
    fertilizer_list = db.getFertilizer("fertilizers", "potassium")
    if fertilizer_list is not None:
        return render_template("fertilizer.html", fertilizers = fertilizer_list, fertilizerName = "Potassium")

@app.route('/updateProfile', methods = ["GET","POST"])
def updateProfile():
    """route to update profile data"""
    if request.method == "POST":
        #uemail = session["uemail"]
        #upassword = session["upassword"]
        #psw = request.form["password"]
        #if psw == upassword:
        db = UserModel()
        db_cust = CustomerModel()
        if 'firstname' in request.form:
            fname = request.form["firstname"]
            lname = request.form["lastname"]
            name = fname + " " + lname
            status = db.updateName(name, uemail)
        if 'email' in request.form:
            new_email = request.form["email"]
            status = db.updateEmail(new_email, uemail)
            #if status:
            #    session["uemail"] = new_email
        if 'phoneno' in request.form:
            phone = request.form["phoneno"]
            status = db_cust.updatePhoneNo(phone,uemail)
        if 'newpassword' in request.form:
            new_psw = request.form["newpassword"]
            status = db.updatePassword(new_psw,uemail)
            #if status:
            #    session["upassword"] = new_psw
        if 'address' in request.form:
            address = request.form["address"]
            status = db_cust.updateAddress(address,uemail)
        if status:
            flash('Profile Updated successfully!')
            return render_template("UpdateProfile.html")
        else:
            flash('Error in updating Profile!!')
            return render_template("UpdateProfile.html")
    else:
        return render_template("UpdateProfile.html")

@app.route('/cart', methods=["GET","POST"])
def viewCart():
    """route to add products in cart"""
    if 'cart' not in session:
        session['cart'] = []
    cart = session.get('cart', [])
    orderTotal = 0
    session['orderTotal'] = orderTotal
    session['referrer'] = request.referrer
    if request.method == "POST":
        product_id = int(request.form["product_id"])
        db = ProductModel()
        product = db.getProductByID(product_id)#product is list of dictionary objects
        cart_prod_ID = None
        for p in cart:
            if p.pID == product_id:
                cart_prod_ID = p.pID
                if int(product.quantity) > int(p.quantity):
                    p.quantity = int(p.quantity) + 1
        # product is already present in the cart session
        if cart_prod_ID is not None:
            if product is not None:
                for items in cart:
                    orderTotal += int(items.quantity) * int(items.price)
                session['orderTotal'] = orderTotal
                #session['referrer'] = request.referrer
                return render_template("cart.html", cart = cart, orderTotal = orderTotal)
            else:
                for items in cart:
                    orderTotal += int(items.quantity) * int(items.price)
                session['orderTotal'] = orderTotal
                #session['referrer'] = request.referrer
                flash("Product Out of Stock!!")
                return render_template("cart.html", cart = cart, orderTotal = orderTotal)
        # product is not present in cart session
        else:
            if product is not None:
                product.quantity = '1'
                session['cart'].append(product)
                for items in cart:
                    orderTotal += int(items.quantity) * int(items.price)
                session['orderTotal'] = orderTotal
                #session['referrer'] = request.referrer
                return render_template("cart.html", cart = cart, orderTotal = orderTotal)
            else:
                for items in cart:
                    orderTotal += int(items.quantity) * int(items.price)
                session['orderTotal'] = orderTotal
                #session['referrer'] = request.referrer
                flash("Product Out of Stock!!")
                return render_template("cart.html", cart = cart , orderTotal = orderTotal)
    else:
        if len(cart) == 0:
            flash("Nothing in Cart!!")
            #session['referrer'] = request.referrer
            return render_template("cart.html", orderTotal = session['orderTotal'])
        else:
            #session['referrer'] = request.referrer
            return render_template("cart.html", cart=cart, orderTotal = orderTotal)

@app.route('/removeFromCart', methods = ["POST"])
def removeFromCart():
    if request.method == "POST":
        product_id = request.form["product_id"]
        product_id = int(product_id)
        db = ProductModel()
        product = db.getProductByID(product_id)
        cart = session.get('cart', [])
        for prod in cart:
            if prod.pID == product_id:
                cart.remove(prod)
                break
        orderTotal = 0
        for items in cart:
            orderTotal += int(items.quantity) * int(items.price)
        session['orderTotal'] = orderTotal
        #session['referrer'] = request.referrer
        return render_template("cart.html",cart = cart, orderTotal = orderTotal)
    else:
        #session['referrer'] = request.referrer
        return render_template("cart.html")

"""
@app.route('/continueShopping')
def back_to_referrer():
    referValue = session['referrer']
    return redirect(referValue)
"""

if __name__ == '__main__':
    app.run()
