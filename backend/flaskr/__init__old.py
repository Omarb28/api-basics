import os, sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS
import random

from models import setup_db, Book, db

BOOKS_PER_SHELF = 8

def paginate_books(request):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * BOOKS_PER_SHELF
  books = Book.query.order_by(Book.title).offset(start).limit(BOOKS_PER_SHELF).all()
  formatted_books = [book.format() for book in books]
  return formatted_books
  
# @DONE: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there. 
#     If you do not update the endpoints, the lab will not work - of no fault of your API code! 
#   - Make sure for each route that you're thinking through when to abort and with which kind of error 
#   - If you change any of the response body keys, make sure you update the frontend to correspond. 

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  # @DONE: Write a route that retrivies all books, paginated. 
  #         You can use the constant above to paginate by eight books.
  #         If you decide to change the number of books per page,
  #         update the frontend to handle additional books in the styling and pagination
  #         Response body keys: 'success', 'books' and 'total_books'
  # TEST: When completed, the webpage will display books including title, author, and rating shown as stars
  @app.route('/books')
  def get_books():

    current_books = paginate_books(request)

    if len(current_books) == 0:
      return abort(404)

    total_books = Book.query.count()

    return jsonify({
      'success': True,
      'books': current_books,
      'total_books': total_books
    })

  # @DONE: Write a route that will update a single book's rating. 
  #         It should only be able to update the rating, not the entire representation
  #         and should follow API design principles regarding method and route.  
  #         Response body keys: 'success'
  # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh
  #
  # curl localhost:5000/books/8 -X Patch -H "Content-Type: application/json" -d '{"rating": 5}' 
  @app.route('/books/<int:book_id>', methods=['PATCH'])
  def update_book_rating(book_id):
    try:
      book = Book.query.get(book_id)
      body = request.get_json()

      if book is None:
        return abort(404)

      if 'rating' in body:
        rating = int(body.get('rating'))
        if rating > 5 or rating < 0:
          return abort(305)

        book.rating = rating
      
      book.update()

      return jsonify({
        'success': True,
        'id': book_id
      })
    except:
      db.session.rollback()
      print(sys.exc_info())
      return abort(400)
    finally:
      db.session.close()

  # @DONE: Write a route that will delete a single book. 
  #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
  #        Response body keys: 'success', 'books' and 'total_books'

  # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.
  @app.route('/books/<int:book_id>', methods=['DELETE'])
  def delete_book(book_id):
    try:
      book = Book.query.get(book_id)

      if book is None:
        return abort(404)

      book.delete()

      return jsonify({
        'success': True,
        'deleted': book_id,
        'books': paginate_books(request),
        'total_books': Book.query.count()
      })
    except:
      db.session.rollback()
      print(sys.exc_info())
      return abort(422)
    finally:
      db.session.close()

  # @DONE: Write a route that create a new book. 
  #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
  # TEST: When completed, you will be able to a new book using the form. Try doing so from the last page of books. 
  #       Your new book should show up immediately after you submit it at the end of the page. 
  @app.route('/books', methods=['POST'])
  def create_book():
    body = request.get_json()

    new_title = body.get('title', None)
    new_author = body.get('author', None)
    new_rating = body.get('rating', None)

    try:
      book = Book(title=new_title, author=new_author, rating=int(new_rating))
      book.insert()

      current_books = paginate_books(request)

      return jsonify({
        'success': True,
        'created': book.id,
        'books': current_books,
        'total_books': Book.query.count()
      })

    except:
      db.session.rollback()
      print(sys.exc_info())
      return abort(422)
    finally:
      db.session.close()
      
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

        

  return app

    