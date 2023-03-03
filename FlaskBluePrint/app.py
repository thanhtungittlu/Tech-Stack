from flask import Flask

from api.api import api_bp
from auth.auth import auth_bp
from cart.cart import cart_bp
from products.products import products_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(products_bp, url_prefix='/products')
