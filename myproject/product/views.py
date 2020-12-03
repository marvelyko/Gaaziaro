from flask import Blueprint,render_template
from myproject.models import Product

product_blueprint = Blueprint("product",__name__,template_folder="templates/product")

@product_blueprint.route("/<int:id>")
def product(id):
    related_products = Product.query.all()
    return render_template("product-detail.html",related_products=related_products)