from Utils.Direction import *
#from Scripts.Utils.Direction import Direction
import math

class SpaceShip:
    pos_X = 300
    pos_Y = 300

    direction = Direction.RIGHT
    shape = [(10,10), None]

    def __init__(self, pos_X, pos_Y, direction):
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.direction = direction
        self.updateShape()

    def updateShape(self):
        if self.direction == Direction.UP:
            self.shape[1] = [(self.pos_X-15, self.pos_Y-15),
                             (self.pos_X-15, self.pos_Y+5),
                             (self.pos_X-5, self.pos_Y-5),
                             (self.pos_X+5, self.pos_Y-5)]

        elif self.direction == Direction.RIGHT:
            self.shape[1] = [(self.pos_X-15, self.pos_Y-15),
                             (self.pos_X-15, self.pos_Y+5),
                             (self.pos_X-5, self.pos_Y-5),
                             (self.pos_X+5, self.pos_Y-5)]

        elif self.direction == Direction.DOWN:
            self.shape[1] = [(self.pos_X-15, self.pos_Y-15),
                             (self.pos_X-15, self.pos_Y+5),
                             (self.pos_X-5, self.pos_Y-5),
                             (self.pos_X+5, self.pos_Y-5)]

        elif self.direction == Direction.LEFT:
            self.shape[1] = [(self.pos_X-15, self.pos_Y-15),
                             (self.pos_X-15, self.pos_Y+5),
                             (self.pos_X-5, self.pos_Y-5),
                             (self.pos_X+5, self.pos_Y-5)]

        else:
            self.shape[1] = [(self.pos_X-15, self.pos_Y-15),
                             (self.pos_X-15, self.pos_Y+5),
                             (self.pos_X-5, self.pos_Y-5),
                             (self.pos_X+5, self.pos_Y-5)]
        return

    def updateMove(self):
        if self.direction == Direction.UP:
            self.pos_Y -= 10
        elif self.direction == Direction.DOWN:
            self.pos_Y += 10
        elif self.direction == Direction.RIGHT:
            self.pos_X += 10
        elif self.direction == Direction.LEFT:
            self.pos_X -= 10
        elif self.direction == Direction.UP_RIGHT:
            self.pos_Y -= 7
            self.pos_X += 7
        elif self.direction == Direction.DOWN_RIGHT:
            self.pos_Y += 7
            self.pos_X += 7
        elif self.direction == Direction.DOWN_LEFT:
            self.pos_Y += 7
            self.pos_X -= 7
        elif self.direction == Direction.UP_LEFT:
            self.pos_Y -= 7
            self.pos_X -= 7
        else:
            print("Erro: Player idle.")
        self.updateShape()

    def moveUp(self):
        self.direction = Direction.UP
        self.updateShape()

    def moveDown(self):
        self.direction = Direction.DOWN
        self.updateShape()

    def moveRight(self):
        self.direction = Direction.RIGHT
        self.updateShape()

    def moveLeft(self):
        self.direction = Direction.LEFT
        self.updateShape()

    def moveUpRight(self):
        self.direction = Direction.UP_RIGHT
        self.updateShape()

    def moveDownRight(self):
        self.direction = Direction.DOWN_RIGHT
        self.updateShape()

    def moveDownLeft(self):
        self.direction = Direction.DOWN_RIGHT
        self.updateShape()

    def moveUpLeft(self):
        self.direction = Direction.UP_LEFT
        self.updateShape()
