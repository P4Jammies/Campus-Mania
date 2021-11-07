import arcade
from vector import Vector2
from constants import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, node, fname: str="sprites\\food.png", scale: float=1):
        super().__init__(node, fname, scale)
        self.name = ENEMY
        self.points = 200
        self.goal = Vector2()
        self.choose_direction = self.goal_direction