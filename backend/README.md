# The Great Bookshelf of Udacity Backend API

## Introduction

This is the backend API for the Great Bookshelf of Udacity. The API provides endpoints for various methods on the books that are stored there, as explained below.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql bookshelf < books.psql
```

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## API Reference

#### Base URL

The base url for the books is accessed at:
```
http://127.0.0.1/books
```

#### API Keys / Authentication

Not yet included

### Introduction

Through the books API you could create, list, and delete the books. Togeether with the ability to change the rating on the books as shown below.

### Resource Endpoint Library

You can access all books through this endpoint:
```
GET   http://127.0.0.1:5000/books
```


You can create a book using the following end point:
```
POST  http://127.0.0.1:5000/books
```
The JSON formatted data expected to create a book is:
```
{
  "title": "Book Title",
  "author": "Author's Name",
  "rating": 4
}
```
The rating should be between 1-5 stars.


You can update a book's rating using the following appraoch which expects an ID at the end of the endpoint:
```
PATCH   http://127.0.0.1:5000/books/5
```
The JSON formatted data expected is:
```
{
  "rating": 3
}
```


You can delete a book using the following apprach which expects an ID at the end of the endpoint:
```
DELETE   http://127.0.0.1:5000/books/5
```



### Error Handling

This section will show which errors you might get if something goes wrong:

You'll get error 400 when a bad request has been sent to the server, as follows:
```
{
  "success": False,
  "error": 400,
  "message": "Bad Request"
}

```

You'll get error 404 when a book has not been found, as follows:
```
{
  "success": False,
  "error": 404,
  "message": "Not Found"
}
```

You'll get error 405 when a method used on an endpoint is not allowed, as follows:
```
{
  "success": False,
  "error": 405,
  "message": "Method Not Allowed"
}
```

You'll get error 422 unprocessable entity when a request to create or edit a book doesn't meet all the criterea, as follows:
```
{
  "success": False,
  "error": 422,
  "message": "Unprocessable Entity"
}
```
<!--
## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/api/v1.0/categories'
GET ...
POST ...
DELETE ...

GET '/api/v1.0/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```
-->

## Testing
To run the tests, run
```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```