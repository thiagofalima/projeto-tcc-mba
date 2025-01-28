from flask import Flask
from routes import pages
from secrets import token_urlsafe
import os
from pymongo import MongoClient

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'ydDwtAeEJZqhmCHuZA9RPNQXPgsI1cnnzYOBDuXHxFk'
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.db = MongoClient(app.config["MONGODB_URI"]).projeto_tcc


    app.register_blueprint(pages)



    return app

print(token_urlsafe())