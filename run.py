import arcade
from nodes import NodeGroup
from player import Player
from enemy import EnemyGroup
from constants import *

class GameController(arcade.Window):
    def __init__(self):
        super().__init__(SCREENWIDTH, SCREENHEIGHT, "Campus Mania")
        self.startGame()
        self.devisible = False
        # self.clock = arcade.time.Clock()

    def setBackground(self):
        arcade.set_background_color(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.sprites = arcade.SpriteList()
        self.player = Player(self.nodes.get_start_node())
        self.sprites.append(self.player)
        self.enemies = EnemyGroup(self.nodes.get_start_node(), self.player)
        self.sprites.extend(self.enemies)

    def on_update(self, dt):
        self.sprites.on_update(dt)

    def on_draw(self):
        arcade.start_render()
        if self.devisible:
            for entity in self.sprites:
                entity.draw_thoughts()
        #self.nodes.render()
        self.sprites.draw()
        # arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.V:
            self.devisible = not self.devisible
        self.player.on_key_press(symbol, modifiers)


if __name__ == "__main__":
    game = GameController()
    arcade.run()
