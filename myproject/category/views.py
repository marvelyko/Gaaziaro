from flask import Blueprint,render_template
from myproject.models import Product

category_blueprint = Blueprint("category",__name__,template_folder="templates/category")

@category_blueprint.route("/health")
def health():
    products = Product.query.all()
    return render_template("product-list.html",products=products)