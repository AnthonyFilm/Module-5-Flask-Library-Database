from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Book, book_schema, books_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee' : 'haw'}

@api.route('/books', methods = ['POST'])
@token_required
def create_book(current_user_token):
    isbn = request.json['isbn']
    author_first = request.json['author_first']
    author_last = request.json['author_last']
    year = request.json['year']
    pages = request.json['pages']
    medium = request.json['medium']
    title = request.json['title']
    description = request.json['description']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    book = Book(isbn, author_first, author_last, title, pages, year, medium, description, user_token = user_token )

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods = ['GET'])
@token_required
def get_book(current_user_token):
    a_user = current_user_token.token
    books = Book.query.filter_by(user_token = a_user).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_single_book(current_user_token, id):
    book = Book.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods = ['POST','PUT'])
@token_required
def update_book(current_user_token,id):
    book = Book.query.get(id) 
    book.isbn = request.json['isbn']
    book.author_first = request.json['author_first']
    book.author_last = request.json['author_last']
    book.year = request.json['year']
    book.pages = request.json['pages']
    book.description = request.json['description']
    book.medium = request.json['medium']
    book.title = request.json['title']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

