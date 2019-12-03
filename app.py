from flask import Flask

from models import db, Player
from routes import api

app = Flask(__name__)
db.init_app(app)
app.register_blueprint(api)

db.create_all(app=app)
with app.app_context():
    db.session.add(Player(name='Mike', height=205))
    db.session.add(Player(name='Rocky', height=198))
    db.session.add(Player(name='Bob', height=195))
    db.session.commit()

if __name__ == '__main__':
    app.run()
