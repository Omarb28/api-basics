from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS

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

  @app.route('/plants', methods=['GET', 'POST'])
  def get_plants():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    #end = start + 10
    #plants = Plant.query.all()
    plants = Plant.query.offset(start).limit(10).all()
    formatted_plants = [plant.format() for plant in plants]
    total_plants = Plant.query.count()

    return jsonify({
      'success': True,
      #'plants': formatted_plants[start:end],
      'plants': formatted_plants,
      'total_plants': total_plants
    })

  @app.route('/plants/<int:plant_id>')
  def get_specific_plant(plant_id):
    #plant = Plant.query.get(plant_id)
    plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
    if plant is None:
      return abort(404)

    return jsonify({
      'success': True,
      'plant': plant.format()
    })


  return app