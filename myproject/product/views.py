from flask import Blueprint,render_template

product_blueprint = Blueprint("product",__name__,template_folder="templates/product")

@product_blueprint.route("/product/<int:id>")
def product(id):
    return render_template("product-detail.html")