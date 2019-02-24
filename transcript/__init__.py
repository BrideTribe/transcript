from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b245eb98f56f7c909adbe0fada726b32e29a28f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transcript.db'
db = SQLAlchemy(app)
js = Bundle('jquery.countryselector.es5.min.js', 'jquery.countrySelector.js', 'lga.js', 'lga.min.js', output='gen.js')
assets = Environment(app)
assets.register('main_js', js)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#configuring the mail server for email and password reset
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ritymontero@gmail.com'
app.config['MAIL_PASSWORD'] = 'sinequanon'

from transcript import routes