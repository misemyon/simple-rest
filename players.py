class Player(object):

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def json(self):
        return {'name': self.name, 'height': self.height}
