
from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
