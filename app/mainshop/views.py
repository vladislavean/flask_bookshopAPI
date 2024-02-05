from flask import Blueprint, request, jsonify
from .models import Book, db

from auth import auth

bp = Blueprint("main", __name__)
#
#@bp.route('/api/v1/auth')
#def heandle_auth_data():
    #   print(request.authorization['username'])
    #  print(request.authorization['password'])
    # return '200'



@bp.route('/api/v1/byId/<id>', methods=["GET"])
def get_by_id(id: Book.id) -> dict:
    try:
        object_by_id = db.session.query(Book).filter(Book.id == id).first()
    except:
        return "Invalid!"
    
    if object_by_id is None:
        return {"CODE": "404 NOT FOUND"}
    
    return {"id": object_by_id.id,
            "name": object_by_id.name,
            "genre": object_by_id.genre,
            "description": object_by_id.description}



@bp.route('/api/v1/search', methods=["GET"])
def search() -> dict:
    data = request.json
    search_data = data["select"]

    
    try:
        searched_by_name = db.session.query(Book).filter(Book.name.like(f'%{search_data}%')).all()
        searched_by_description = db.session.query(Book).filter(Book.description.like(f'%{search_data}%')).all()
        db.session.commit()
    except:
        print("Ошибка!")
    res = {}

    datas = searched_by_name + searched_by_description
    for ob in datas:
        res[ob.id] = {
            "description": ob.description,
            "genre": ob.genre,
            "name": ob.name
        }

    return res