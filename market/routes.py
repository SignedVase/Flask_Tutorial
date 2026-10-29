from market import app, db
from flask import render_template
from market.models import Item
from sqlalchemy import select
from market.fonts import RegisterForm

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    query = select(Item)
    items = db.session.scalars(query).all()
    return render_template("market.html", items=items)

@app.route("/register")
def register_page():
    form = RegisterForm()
    return render_template("register.html", form=form)