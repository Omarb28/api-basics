import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('vagrant', 'vagrant','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc. 
#        Since there are four routes currently, you should have at least eight tests. 
# Optional: Update the book information in setUp to make the test database your own! 
    def test_get_paginated_books(self):
      res = self.client().get('/books')
      data = json.loads(res.data.decode('utf-8'))

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertTrue(data['total_books'])
      self.assertTrue(len(data['books']))
      
    def test_404_sent_requesting_beyond_valid_page(self):
      res = self.client().get('/books?page=1000', json={'rating': 1})
      data = json.loads(res.data.decode('utf-8'))

      self.assertEqual(res.status_code, 404)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'Not Found')

    def test_update_book_rating(self):
      rating = {'rating': 1}
      res = self.client().patch('/books/5', json=rating)
      data = json.loads(res.data.decode('utf-8'))
      book = Book.query.get(5)
      
      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertEqual(book.format()['rating'], 1)

    def test_update_book_rating_fail(self):
      res = self.client().patch('/books/5')
      data = json.loads(res.data.decode('utf-8'))

      self.assertEqual(res.status_code, 400)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'Bad Request')

    def test_delete_book(self):
      pass

    def test_delete_book_fail(self):
      pass

    def test_create_book(self):
      book = {
        'author': 'Test Author',
        'title': 'Test Book',
        'rating': 5
      }
      res = self.client().post('/books', json=book)
      data = json.loads(res.data.decode('utf-8'))

      self.assertEqual(res.status_code, 200)
      self.assertTrue(data['total_books'])
      self.assertTrue(len(data['books']))

    def test_create_book_fail(self):
      res = self.client().post('/books')
      self.assertEqual(res.status_code, 400)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()