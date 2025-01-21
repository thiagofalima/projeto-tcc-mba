from flask import Flask
from routes import pages
from secrets import token_urlsafe

def create_app():

    app = Flask(__name__)
    app.register_blueprint(pages)

    app.secret_key = 'ydDwtAeEJZqhmCHuZA9RPNQXPgsI1cnnzYOBDuXHxFk'

    # DB settup and connection

    return app

print(token_urlsafe())