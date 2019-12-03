from flask import Blueprint, jsonify

from models import Player

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/players')
def get_players():
    return jsonify([(lambda player: player.json())(player) for player in Player.query.all()])


@api.route('/player/id/<int:player_id>')
def get_player(player_id):
    player = Player.query.get(player_id)
    return player.json() if player else jsonify()
