from flask import Blueprint,render_template,redirect,url_for,session
from myproject.models import Product
from flask_login import logout_user,login_required

index_blueprint = Blueprint("index",__name__,template_folder="templates/index")

@index_blueprint.route("/")
def index():
    product_list = Product.query.all()
    return render_template("index.html",product_list=product_list)

@index_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))

@index_blueprint.route("/addToCart/<int:id>")
def add_cart_item(id):
    if "cart" not in session:
        session["cart"] = []
    cart_list = session["cart"]
    if id not in cart_list:
        cart_list.append(id)
    else:
        cart_list.remove(id)
    session["cart"] = cart_list
    data = {"productId":id}
    return data

@index_blueprint.route("/getCartCount")
def cart_count():
    if "cart" not in session:
        return {"itemCount": 0}
    else:
        return {"itemCount": len(session["cart"])}

@index_blueprint.route("/addToWish/<int:id>")
def add_wish_item(id):
    if "wish" not in session:
        session["wish"] = []
    wish_list = session["wish"]
    if id not in wish_list:
        wish_list.append(id)
    else:
        wish_list.remove(id)
    session["wish"] = wish_list
    data = {"productId":id}
    return data

@index_blueprint.route("/getWishCount")
def wish_count():
    if "wish" not in session:
        return {"itemCount": 0}
    else:
        return {"itemCount": len(session["wish"])}