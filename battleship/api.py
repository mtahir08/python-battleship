import http
import json
import flask

from jsonschema import validate, ValidationError
from battleship.constant import request_validator
from battleship.game import Game

ROWS = 10
COLS = 10

app = flask.Flask(__name__)
game = Game(ROWS, COLS)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    response = flask.request.data
    data = json.loads(response)
    ships = data.get("ships")
    try:
        validate(data, request_validator.get("CREATE"))
        for ship in ships:
            validate(ship, request_validator.get("SHIP"))
        val = game.create(ships)
        if val:
            return flask.jsonify({"result": "Game created"}), http.HTTPStatus.OK
        return flask.jsonify({"message": "Bad Request"}), http.HTTPStatus.BAD_REQUEST
    except ValidationError as e:
        print("errors are :",e)
        return flask.jsonify({"message": "Bad Request","error":e}), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED
