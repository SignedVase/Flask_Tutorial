from flask import Flask
from flask_sqlalchemy_lite import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_ENGINES"] = {"default" : "sqlite:///db.sqlite3"}
app.config['SECRET_KEY'] = '93ba68117882976f807bdb40'

db = SQLAlchemy()
db.init_app(app)

from market import routes