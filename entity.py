import arcade
from vector import Vector2
from constants import *
from random import randint

class Entity(arcade.Sprite):
    def __init__(self, node, fname: str="sprites\\food.png", scale: float=1):
        super().__init__(fname, scale)
        self.name = None
        self.directions = {UP:Vector2(0, 1), RIGHT:Vector2(1, 0),
                          DOWN:Vector2(0, -1), LEFT:Vector2(-1, 0),
                          STOP:Vector2()}
        self.direction = STOP
        self.setSpeed(100)
        self.radius = 10
        self.hitbox = 5
        self.color = RED
        self.node = node
        self.setPosition()
        self.target = node
        self.invisible = False
        self.disablePortal = False
        
    def setPosition(self):
        self.position = self.node.position.asTuple()

    def setSpeed(self, speed):
        self.speed = speed * TILEWIDTH / 16
    
    def setVelocity(self, dt):
        self.velocity = self.directions[self.direction]*self.speed*dt

    def draw(self):
        print("Entity is drawn")
        if not self.invisible:
            arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
    """
    def update(self):
        return super().update()
    """
    def on_update(self, dt):
        super().update()

        if self.overshotTarget():
            self.node = self.target
            directions = self.validDirections()
            direction = self.chooseDirection(directions)
            if not self.disablePortal:
                if self.node.neighbors[PORTAL] is not None:
                    self.node = self.node.neighbors[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)

            self.setPosition()
            self.setVelocity(dt)

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbors[direction]
        return self.node

    def overshotTarget(self):
        if self.target is not None:
            position = Vector2(self.center_x, self.center_y)
            target = self.target.position - self.node.position
            progress = position - self.node.position
            return progress.magnitude2() >= target.magnitude2()
        return False

    def reverseDirection(self):
        self.direction *= -1
        temp = self.node
        self.node = self.target
        self.target = temp

    def oppositeDirection(self, direction):
        if direction is not STOP:
            if direction == self.direction * -1:
                return True
        return False

    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False

    def validDirections(self):
        directions = []
        for key in [UP, DOWN, LEFT, RIGHT]:
            if self.validDirection(key):
                if key != self.direction * -1:
                    directions.append(key)
        if len(directions) == 0:
            directions.append(self.direction * -1)
        return directions

    def chooseDirection(self, directions):
        # random by default
        return directions[randint(0, len(directions)-1)]