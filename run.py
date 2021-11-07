import arcade
from nodes import NodeGroup
from player import Player
from entity import Entity
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
        self.entity = Entity(self.nodes.getStartNode())
        self.sprites.append(self.entity)
        self.player = Player(self.nodes.getStartNode())
        self.sprites.append(self.player)

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
        self.nodes.render()
        self.sprites.draw()
        # arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)


if __name__ == "__main__":
    game = GameController()
    arcade.run()
