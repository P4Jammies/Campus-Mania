from constants import *

class MainMode(object):
    def __init__(self):
        self.timer = 0
        self.scatter()

    def on_update(self, dt):
        self.timer += dt
        if self.timer >= self.time:
            if self.mode is SCATTER:
                self.chase()
            elif self.mode is CHASE:
                self.scatter()

    def scatter(self):
        self.mode = SCATTER
        self.time = 7
        self.timer = 0
    
    def chase(self):
        self.mode = CHASE
        self.time = 20
        self.timer = 0

class ModeController(object):
    def __init__(self, entity):
        self.timer = 0
        self.time = None
        self.mainmode = MainMode()
        self.current = self.mainmode.mode
        self.entity = entity

    def on_update(self, dt):
        self.mainmode.on_update(dt)
        self.current = self.mainmode.mode