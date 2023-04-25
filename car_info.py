
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Car:
    def __init__(self, x, y):
        self.health = 100
        self.pos = Coordinate(x, y)
        self.is_alive = True
        self.sprite = 'O'

    def move(self, move_choice):
        if move_choice == 1:
            self.pos.x += 15
        elif move_choice == 2:
            self.pos.x -= 15

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False

