from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

import routes