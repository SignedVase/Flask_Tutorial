from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
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

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Errinhos na criação de usuários: {err}', category="danger")
    return render_template("register.html", form=form)