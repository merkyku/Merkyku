class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Brick:
    def __init__(self, x, y):
        self.pos = Coordinate(x, y)
        self.sprite = 'b'
