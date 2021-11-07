import arcade
from nodes import NodeGroup
from player import Player
from enemy import Enemy
from constants import *

class GameController(arcade.Window):
    def __init__(self):
        super().__init__(SCREENWIDTH, SCREENHEIGHT, "Campus Mania")
        self.startGame()
        # self.clock = arcade.time.Clock()

    def setBackground(self):
        arcade.set_background_color(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.sprites = arcade.SpriteList()
        self.player = Player(self.nodes.get_start_node())
        self.sprites.append(self.player)
        self.entity = Enemy(self.nodes.get_start_node(), "sprites\\food.png", self.player)
        self.sprites.append(self.entity)

    def on_update(self, dt):
        self.sprites.on_update(dt)
        #self.checkEvents()
        #self.render()

    """
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    """

    def on_draw(self):
        arcade.start_render()
        #self.nodes.render()
        self.sprites.draw()
        # arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)


if __name__ == "__main__":
    game = GameController()
    arcade.run()
