from flask import Flask, jsonify
from models import setup_db, Plant
from flask_corss import CORS

def create_app(test_config=None):
  app = Flask(__name__)
  CORS(app)
  #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  setup_db(app)

  # CORS Headers
  @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

  @app.route('/')
  def hello():
    return jsonify({'message': 'HELLO WORLD'})



  return app