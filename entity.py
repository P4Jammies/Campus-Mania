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
        self.set_speed(100)
        self.radius = 10
        self.hitbox = 5
        self.color = RED
        self.node = node
        self.set_position()
        self.target = node
        self.invisible = False
        self.disablePortal = False
        
    def set_position(self):
        self.position = self.node.position.asTuple()

    def set_speed(self, speed):
        self.speed = speed * TILEWIDTH / 16
    
    def set_velocity(self, dt):
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

        if self.overshot_target():
            self.node = self.target
            directions = self.valid_directions()
            direction = self.choose_direction(directions)
            if not self.disablePortal:
                if self.node.neighbors[PORTAL] is not None:
                    self.node = self.node.neighbors[PORTAL]
            self.target = self.get_new_target(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.get_new_target(self.direction)

            self.set_position()
            self.set_velocity(dt)

    def get_new_target(self, direction):
        if self.valid_direction(direction):
            return self.node.neighbors[direction]
        return self.node

    def overshot_target(self):
        if self.target is not None:
            position = Vector2(self.center_x, self.center_y)
            target = self.target.position - self.node.position
            progress = position - self.node.position
            return progress.magnitude2() >= target.magnitude2()
        return False

    def reverse_direction(self):
        self.direction *= -1
        temp = self.node
        self.node = self.target
        self.target = temp

    def opposite_direction(self, direction):
        if direction is not STOP:
            if direction == self.direction * -1:
                return True
        return False

    def valid_direction(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False

    def valid_directions(self):
        directions = []
        for key in [UP, DOWN, LEFT, RIGHT]:
            if self.valid_direction(key):
                if key != self.direction * -1:
                    directions.append(key)
        if len(directions) == 0:
            directions.append(self.direction * -1)
        return directions

    def choose_direction(self, directions):
        # random by default
        return directions[randint(0, len(directions)-1)]