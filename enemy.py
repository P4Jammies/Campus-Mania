import arcade
from vector import Vector2
from constants import *
from entity import Entity
from modes import ModeController as Mode

class Enemy(Entity):
    def __init__(self, node, fname: str="sprites\\food.png", player=None, scale: float=1):
        super().__init__(node, fname, scale)
        self.name = ENEMY
        self.points = 200
        self.goal = Vector2()
        self.choose_direction = self.goal_direction
        self.player = player
        self.mode = Mode(self)

    def on_update(self, dt):
        self.mode.on_update(dt)
        if self.mode.current is SCATTER:
            self.scatter()
        elif self.mode.current is CHASE:
            self.chase()
        super().on_update(dt)

    def scatter(self):
        self.goal = Vector2()

    def chase(self):
        self.goal = self.player.position