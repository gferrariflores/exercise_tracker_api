from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config  # Otra opción: from .config import Config

app = Flask(__name__)
CORS(app)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize db and ma
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import routes
