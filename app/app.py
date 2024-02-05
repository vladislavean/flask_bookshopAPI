from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import config


conf = config.Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{conf.DB_USER}:{conf.DB_PASSWORD}@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_NAME}'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


import mainshop
import auth
import admin

app.register_blueprint(mainshop.bp)
app.register_blueprint(admin.bp)