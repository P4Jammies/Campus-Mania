import arcade
from vector import Vector2
from constants import *
from entity import Entity
from modes import ModeController as Mode

class Enemy(Entity):
    def __init__(self, node, fname: str="sprites\\null.png", player=None, leader=None, scale: float=SCALE/2):
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
        super().__init__(node, "sprites\\friend.png", player, leader)
        self.name = BLINKY
        self.color = RED

class Pinky(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\phone.png", player, leader)
        self.name = PINKY
        self.color = PINK

    def scatter(self):
        self.goal = Vector2(0, SCREENHEIGHT)

    def chase(self):
        self.goal = self.player.position + self.player.directions[self.player.direction]*SCALEWIDTH*2

class Inky(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\sleep.png", player, leader)
        self.name = INKY
        self.color = TEAL

    def scatter(self):
        self.goal = Vector2(SCREENWIDTH, 0)

    def chase(self):
        player = self.player.position + self.player.directions[self.player.direction]*SCALEWIDTH
        self.goal = self.leader.position + (player-self.leader.position)*2

class Clyde(Enemy):
    def __init__(self, node, player=None, leader=None):
        super().__init__(node, "sprites\\food.png", player, leader)
        self.name = CLYDE
        self.color = ORANGE

    def scatter(self):
        self.goal = Vector2()

    def chase(self):
        if (self.player.position-self.position).magnitude2() <= (SCALEWIDTH*4)**2:
            self.scatter()
        else:
            super().chase()

class EnemyGroup(arcade.Window):
    def __init__(self, nodes, player):
        self.blinky = Blinky(nodes[1], player)
        self.pinky = Pinky(nodes[0], player)
        self.inky = Inky(nodes[3], player, self.blinky)
        self.clyde = Clyde(nodes[2], player)
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