from flask import Blueprint, render_template
from  .models import Product

views = Blueprint('views', __name__)

@views.route('/')
def home():

    items = Product.query.filter_by(flash_sale=True)

    # for i in items:
    #    print(i,"5")

    return render_template("home.html")