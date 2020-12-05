from flask import Blueprint,render_template
from myproject.models import Product,Category

category_blueprint = Blueprint("category",__name__,template_folder="templates/category")

@category_blueprint.route("/health")
def health():
    category = Category.query.filter_by(name="health").first()
    products = category.products.all()
    return render_template("product-list.html",product_list=products)

@category_blueprint.route("/beauty")
def beauty():
    category = Category.query.filter_by(name="beauty").first()
    products = category.products.all()
    return render_template("product-list.html",product_list=products)

@category_blueprint.route("/grocery")
def grocery():
    category = Category.query.filter_by(name="grocery").first()
    products = category.products.all()
    return render_template("product-list.html",product_list=products)

@category_blueprint.route("/hygiene")
def hygiene():
    category = Category.query.filter_by(name="hygiene").first()
    products = category.products.all()
    return render_template("product-list.html",product_list=products)

@category_blueprint.route("/charity")
def charity():
    category = Category.query.filter_by(name="charity").first()
    products = category.products.all()
    return render_template("product-list.html",product_list=products)