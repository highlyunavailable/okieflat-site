from datetime import datetime
from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Your contact page.'
    )

@app.route('/products')
def products():
    from productslist import get_products
    return render_template(
        'products.html',
        title = 'Products',
        year = datetime.now().year,
        products = get_products()
    )

