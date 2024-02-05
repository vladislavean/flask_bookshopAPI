from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from auth.models import Users
from app import db
from auth.auth import auth
from mainshop.models import Book

bp = Blueprint("admin", __name__)

@bp.route("/api/v1/create_user", methods=["POST"])
@auth.login_required
def create_user() -> dict:
    data = request.json
    username = data["username"]
    password = generate_password_hash(data["password"])
    user = Users(name=username, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return {'code': 200,
                'response': f'User {username} is created'}
    except:
        return {
            'code': 504,
            'response': 'Creating is terminated'
        }

@bp.route('/api/v1/addBook', methods=["POST"])
@auth.login_required
def addBook() -> dict:
    data = request.json
    try:
        book_obj = Book(name=data['name'], genre=data['genre'], description=data['description'])
        db.session.add(book_obj)
    except:
        return "504"
    db.session.commit()
    return {"code": 200, "posted": "true"}