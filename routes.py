from flask import Blueprint, jsonify

from models import Player

api = Blueprint('api', __name__, url_prefix='/api')
index = Blueprint('index', __name__)


@api.route('/players')
def get_players():
    return jsonify([(lambda player: player.json())(player) for player in Player.query.all()])


@api.route('/player/id/<int:player_id>')
def get_player(player_id):
    player = Player.query.get(player_id)
    return player.json() if player else jsonify()


@index.route('/')
@index.route('/index')
def get_index():
    return '''<html>
                <head>
                  <title>The simple RESTful web service with Python and Flask</title>
                </head>
                <body>
                  <header>
                    <h3>The simple RESTful web service with Python and Flask</h3>
                  </header>
                  <article>
                    <p>API: <a href="./api/players">Players</a> </p>
                  </article>
                </body>
              </html>'''
