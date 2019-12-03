from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(128))
    height = db.Column(db.Integer)

    def __repr__(self):
        return '<Player {}>'.format(self.id)

    def json(self):
        return {'id': self.id, 'name': self.name, 'height': self.height}
