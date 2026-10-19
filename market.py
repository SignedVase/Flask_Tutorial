from flask import Flask, render_template
from flask_sqlalchemy_lite import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, select

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

    def __repr__(self) -> str:
        return f"Item {self.name}"


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    query = select(Item)
    items = db.session.scalars(query).all()
    return render_template("market.html", items=items)