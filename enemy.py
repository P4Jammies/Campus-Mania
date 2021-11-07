import arcade
from nodes import Node
from vector import Vector2
from constants import *
from entity import Entity
from modes import ModeController as Mode

class Enemy(Entity):
    def __init__(self, node: Node, fname: str="sprites\\null.png", player=None, leader=None, scale: float=1):
        super().__init__(node, fname, scale)
        self.name = ENEMY
        self.points = POINTS
        self.goal = Vector2()
        self.choose_direction = self.goal_direction
        self.player = player
        self.mode = Mode(self)
        self.leader = leader
        self.home = node

    def on_update(self, dt):
        self.mode.on_update(dt)
        if self.mode.current is SCATTER:
            self.scatter()
        elif self.mode.current is CHASE:
            self.chase()
        super().on_update(dt)

    def scatter(self):
        self.goal = Vector2(SCREENWIDTH, SCREENHEIGHT)

    def chase(self):
        self.goal = self.player.position

class Blinky(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\eyel.png", player, leader)
        self.name = BLINKY
        self.color = RED

class Pinky(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\eyed.png", player, leader)
        self.name = PINKY
        self.color = PINK

    def scatter(self):
        self.goal = Vector2(0, SCREENHEIGHT)

    def chase(self):
        self.goal = self.player.position + self.player.directions[self.player.direction]*TILEWIDTH*4

class Inky(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\eyer.png", player, leader)
        self.name = INKY
        self.color = TEAL

    def scatter(self):
        self.goal = Vector2(SCREENWIDTH, 0)

    def chase(self):
        player = self.player.position + self.player.directions[self.player.direction]*TILEWIDTH*2
        self.goal = self.leader.position + (player-self.leader.position)*2

class Clyde(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\eyeu.png", player, leader)
        self.name = CLYDE
        self.color = ORANGE

    def scatter(self):
        self.goal = Vector2()

    def chase(self):
        if (self.player.position-self.position).magnitude2() <= (TILEWIDTH*8)**2:
            self.scatter()
        else:
            super().scatter()

class EnemyGroup(arcade.Window):
    def __init__(self, node: Node, player):
        self.blinky = Blinky(node, player)
        self.pinky = Pinky(node, player)
        self.inky = Inky(node, player, self.blinky)
        self.clyde = Clyde(node, player)
        self.enemies = [self.blinky, self.pinky, self.inky, self.clyde]
        
    def __iter__(self):
        return iter(self.enemies)

    def on_update(self, dt):
        for enemy in self:
            enemy.on_update(dt)

    def set_spawn(self, node):
        for enemy in self:
            enemy.set_spawn(node)

    def update_points(self):
        for enemy in self:
            enemy.points *= 2
    
    def reset_points(self):
        for enemy in self:
            enemy.points = POINTS

    def reset(self):
        for enemy in self:
            enemy.reset()

    def hide(self):
        for enemy in self:
            enemy.invisible = True
    
    def show(self):
        for enemy in self:
            enemy.invisible = False
    
    def render(self):
        for enemy in self:
            enemy.render()