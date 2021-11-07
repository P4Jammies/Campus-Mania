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

    def set_velocity(self, dt):
        super().set_velocity(dt)

    def draw(self):
        print("Player is drawn")
        super().draw()

    def on_update(self, dt):
        super().update()

        if self.overshot_target():
            self.node = self.target
            if self.node.neighbors[PORTAL] is not None:
                self.node = self.node.neighbors[PORTAL]
            self.target = self.get_new_target(self.key)
            if self.target is not self.node:
                self.direction = self.key
            else:
                self.target = self.get_new_target(self.direction)

            if self.target is self.node:
                self.direction = STOP
            self.set_position()
            self.set_velocity(dt)
        else:
            if self.opposite_direction(self.key):
                self.reverse_direction()
                self.set_velocity(dt)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.key = UP
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.key = DOWN
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.key = LEFT
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.key = RIGHT
