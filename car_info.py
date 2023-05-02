
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Car:
    def __init__(self, x, y):
        self.health = 100
        self.pos = Coordinate(x, y)
        self.is_alive = True
        self.sprite = 'car'

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False

