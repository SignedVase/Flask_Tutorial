from flask import Flask, render_template
from flask_sqlalchemy_lite import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

app = Flask(__name__)
app.config["SQLALCHEMY_ENGINES"] = {"default" : "sqlite:///db.sqlite3"}

db = SQLAlchemy()
db.init_app(app)

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    barcode: Mapped[str] = mapped_column(String(12), unique=True)
    description: Mapped[str] = mapped_column(String(1024), unique=True)
    price: Mapped[int]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html", items=items)