from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask import dotenv

app = Flask(__name__)
FLASK_APP = os.dotenv('FLASK_APP')
FLASK_ENV = os.dotenv('FLASK_ENV')
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

#can't flask db init because... #NameError: name 'token_required' is not defined 
# flask db --help

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
