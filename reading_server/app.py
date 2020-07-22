from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) 

currentDirectory = os.getcwd() 

app.config.from_object('config.Config')
db = SQLAlchemy(app) 

import routes , models 