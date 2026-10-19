from flask import Flask
from flask_sqlalchemy_lite import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_ENGINES"] = {"default" : "sqlite:///db.sqlite3"}
db = SQLAlchemy()
db.init_app(app)

from market import routes