from flask_httpauth import HTTPBasicAuth
from flask import Blueprint, request
from werkzeug.security import check_password_hash
from .models import Users, db


auth = HTTPBasicAuth()
    

def get_user_info(name):
    return db.session.query(Users).filter( Users.name == name ).first()

@auth.verify_password
def verify_password(username: str, password: str) -> str:
    user = get_user_info(username)
    if (user is not None) and (check_password_hash(user.password, password)):
        return username
 

