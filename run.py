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
        self.paused = False
        # self.clock = arcade.time.Clock()

    def setBackground(self):
        arcade.set_background_color(BLACK)

    def setMap(self):
        self.nodes = NodeGroup()
        self.map = arcade.load_texture("sprites\\level1.png")

    def startGame(self):
        self.setBackground()
        self.setMap()
        self.sprites = arcade.SpriteList()
        self.player = Player(self.nodes.get_player_start())
        self.sprites.append(self.player)
        self.enemies = EnemyGroup(self.nodes.get_enemy_start(), self.player)
        self.sprites.extend(self.enemies)

    def on_update(self, dt):
        if self.paused:
            return
        self.sprites.on_update(dt)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(SCALE*4, SCALE*4, SCREENWIDTH-SCALE*8, SCREENHEIGHT-SCALE*8, self.map)
        #self.nodes.render()
        if self.devisible:
            for entity in self.sprites:
                entity.draw_thoughts()
        self.sprites.draw()
        # arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            self.paused = not self.paused
        if symbol == arcade.key.V:
            self.devisible = not self.devisible
            for entity in self.sprites:
                speed = SPEED/2 if self.devisible else SPEED
                entity.set_speed(speed)
        self.player.on_key_press(symbol, modifiers)


if __name__ == "__main__":
    game = GameController()
    arcade.run()
