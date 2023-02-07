from flask import Flask, request, render_template
from model import *
#from templates.Admin.public import *
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/product_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
def home():
    db = ProductModel()
    product_list = db.getHomeProducts()
    if product_list is not None:
        return render_template("index.html", products=product_list)


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/About')
def about():
    return render_template("About.html")


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route('/accountinfo')
def account_info():
    return render_template('Account_info.html')


@app.route('/UpdateProfile')
def update_profile():
    return render_template("UpdateProfile.html")


@app.route('/shipping_info')
def shipping_info():
    return render_template("shipping_info.html")

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
    db = ProductModel()
    product_list = db.getProducts()
    if product_list is not None:
        return render_template("Admin/Product_listing.html", products = product_list)


@app.route('/fruits')
def seed_fruits():
    """route to show seeds"""
    category = "seeds"
    subcategory = "fruits"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("seed.html",  products=product_list,  name=subcategory)
    else:
        return render_template("seed.html", msg="No Available Item in this list", name=subcategory)


@app.route('/flowers')
def seed_flowers():
    category = "seeds"
    subcategory = "flowers"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("seed.html",  products=product_list,  name=subcategory)
    else:
        return render_template("seed.html", msg="No Available Item in this list",  name=subcategory)


@app.route('/vegetables')
def seed_vegetables():
    """route to show seeds"""
    category = "seeds"
    subcategory = "vegetables"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("seed.html",  products=product_list,  name=subcategory)
    else:
        return render_template("seed.html", msg="No Available Item in this list", name=subcategory)


@app.route('/indoor_plants')
def seed_indoor_plants():
    """route to show seeds"""
    category = "seeds"
    subcategory = "indoor plants"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("seed.html",  products=product_list,  name=subcategory)
    else:
        return render_template("seed.html", msg="No Available Item in this list", name=subcategory)



@app.route('/Nfertilizer')
def show_n_fertilizer():
    """route to show fertilizers"""
    db = ProductModel()
    name = "fertilizers"
    subcategory = "nitrogen"
    fertilizer_list = db.get_categories_data(name, subcategory)
    if fertilizer_list:
        return render_template("fertilizer.html", fertilizers=fertilizer_list, fertilizerName=subcategory)
    else:
        return render_template("fertilizer.html", msg="No Available Item in this list", fertilizerName=subcategory)

@app.route('/PHfertilizer')
def show_ph_fertilizer():
    """route to show fertilizers"""
    name = "fertilizers"
    subcategory = "phosphorus"
    db = ProductModel()
    fertilizer_list = db.get_categories_data(name, subcategory)
    if fertilizer_list:
        return render_template("fertilizer.html", fertilizers=fertilizer_list, fertilizerName=subcategory)
    else:
        return render_template("fertilizer.html", msg="No Available Item in this list", fertilizerName=subcategory)



@app.route('/Pfertilizer')
def show_pf_fertilizer():
    """route to show fertilizers"""
    name = "fertilizers"
    subcategory = "potassium"
    db = ProductModel()
    fertilizer_list = db.get_categories_data(name, subcategory)
    if fertilizer_list:
        return render_template("fertilizer.html", fertilizers=fertilizer_list, fertilizerName=subcategory)
    else:
        return render_template("fertilizer.html", msg="No Available Item in this list", fertilizerName=subcategory)



@app.route('/flowering')
def flowering_plants():
    """route to show plants"""
    category = "plants"
    subcategory = "flowering plants"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("plant.html",  products=product_list,  name=subcategory)
    else:
        return render_template("plant.html", msg="No Available Item in this list", name=subcategory)


@app.route('/non-flowering')
def non_flowering_plants():
    """route to show plants"""
    category = "plants"
    subcategory = "non flowering plants"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("plant.html",  products=product_list,  name=subcategory)
    else:
        return render_template("plant.html", msg="No Available Item in this list", name=subcategory)


@app.route('/climber')
def climber_plants():
    """route to show plants"""
    category = "plants"
    subcategory = "climbing plants"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("plant.html",  products=product_list,  name=subcategory)
    else:
        return render_template("plant.html", msg="No Available Item in this list", name=subcategory)


@app.route('/creeper')
def creeper_plants():
    """route to show plants"""
    category = "plants"
    subcategory = "creepers"
    db = ProductModel()
    product_list = db.get_categories_data(category, subcategory)
    if product_list:
        return render_template("plant.html",  products=product_list,  name=subcategory)
    else:
        return render_template("plant.html", msg="No Available Item in this list", name=subcategory)


@app.route("/single_product", methods=["GET", "POST"])
def single_product():
    if request.method == "POST":
        id_ = int(request.form['product_id'])
        db = ProductModel()
        product_data = db.get_single_product_detail(id_)
        return render_template("singleProduct.html", product=product_data)
    else:
        return render_template("singleProduct.html")




if __name__ == '__main__':
    app.run()
