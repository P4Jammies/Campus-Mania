import arcade
from nodes import NodeGroup
from constants import *

class GameController(arcade.Window):
    def __init__(self):
        super().__init__(SCREENWIDTH, SCREENHEIGHT, "Working Title")
        self.startGame()
        # self.clock = arcade.time.Clock()

    def setBackground(self):
        arcade.set_background_color(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()

    """
    def update(self):
        self.checkEvents()
        self.render()
    """

    """
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    """

    def on_draw(self):
        arcade.start_render()
        self.nodes.render()
        # arcade.finish_render()


if __name__ == "__main__":
    game = GameController()
    arcade.run()
