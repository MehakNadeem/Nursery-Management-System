from flask import Flask, request, render_template, jsonify, json, make_response, send_file
from db_classes import *
from model import *
from templates.Admin.public import *
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello():
    return "Hello!!"

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

if __name__ == '__main__':
    app.run()
