import arcade
from vector import Vector2
from constants import *
from entity import Entity

class Player(Entity):
    def __init__(self, node, fname: str="sprites\eyer.png", scale: float=1):
        super().__init__(node, fname, scale)
        self.name = PLAYER
        self.color = WHITE
        self.velocity = (0, 0)
        self.key = STOP

    def setVelocity(self, dt):
        super().setVelocity(dt)

    def draw(self):
        print("Player is drawn")
        super().draw()

    def on_update(self, dt):
        super().update()

        if self.overshotTarget():
            self.node = self.target
            self.target = self.getNewTarget(self.key)
            if self.target is not self.node:
                self.direction = self.key
            else:
                self.target = self.getNewTarget(self.direction)

            if self.target is self.node:
                self.direction = STOP
            self.setPosition()
            self.setVelocity(dt)
        else:
            if self.oppositeDirection(self.key):
                self.reverseDirection()
                self.setVelocity(dt)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.key = UP
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.key = DOWN
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.key = LEFT
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.key = RIGHT
