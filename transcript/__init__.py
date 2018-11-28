from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b245eb98f56f7c909adbe0fada726b32e29a28f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transcript.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from transcript import routes