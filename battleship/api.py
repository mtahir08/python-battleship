import http
import json
import flask

from jsonschema import validate, ValidationError
from battleship.constant import request_validator
from battleship.game import Game

ROWS = 10
COLS = 10

app = flask.Flask(__name__)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
  global game 
  game = Game(ROWS, COLS)
  req_data = flask.request.data
  data = json.loads(req_data)
  ships = data.get("ships")
  try:
    validate(data, request_validator.get("CREATE"))
    for ship in ships:
      validate(ship, request_validator.get("SHIP"))
    flag = game.create(ships)
    if flag:
      return flask.jsonify({"result": "Game created"}), http.HTTPStatus.OK
    return flask.jsonify({"message": "Bad Request"}), http.HTTPStatus.BAD_REQUEST
  except ValidationError as e:
    print("errors are :",e)
    return flask.jsonify({"message": "Bad Request","error":e}), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
  req_data = flask.request.data
  coords = json.loads(req_data)
  try:
    validate(coords, request_validator.get("SHOT"))
    result = game.fire(coords)
    return flask.jsonify({"result": result}), http.HTTPStatus.OK
  except ValidationError as e:
    print("errors are :",e)
    return flask.jsonify({"result": "Bad Request"}), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
  game.delete_game_progress()
  return flask.jsonify({"result": "Game has been reset successfully"}), http.HTTPStatus.OK
