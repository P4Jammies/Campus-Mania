import arcade
#from pygame.pygame.locals import *
from constants import *

class GameController(object):
    def __init__(self):
        arcade.open_window(SCREENWIDTH, SCREENHEIGHT, "Working Title")

    def setBackground(self):
        arcade.set_background_color(BLACK)

    def startGame(self):
        self.setBackground()
        self.render()
        arcade.run()

    def update(self):
        self.checkEvents()
        self.render()

    """
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    """

    def render(self):
        arcade.start_render()
        arcade.draw_circle_filled(SCREENWIDTH/2, SCREENHEIGHT/2, 150, arcade.color.BLUE)
        arcade.finish_render()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    #while True:
    #    game.update()
