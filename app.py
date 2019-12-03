from flask import Flask, jsonify

from players import Player

app = Flask(__name__)


@app.route('/api/players')
def get_players():
    return jsonify([Player('Mike', 205).json(), Player('Rocky', 195).json(), Player('Bob', 193).json()])


if __name__ == '__main__':
    app.run()
