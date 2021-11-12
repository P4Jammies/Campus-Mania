# Screen
TILEWIDTH = 16
TILEHEIGHT = 16
SCALE = 3
XBUFFER = 1
YBUFFER = 1
NROWS = (8+YBUFFER+XBUFFER)*SCALE
NCOLS = (16+2*XBUFFER)*SCALE
SCREENWIDTH = NCOLS*TILEWIDTH
SCREENHEIGHT = NROWS*TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
SCALEWIDTH = SCALE*TILEWIDTH
SCALEHEIGHT = SCALE*TILEHEIGHT

# Modes
SCATTER = 0
CHASE = 1
FRIGHT = 2
SPAWN = 3

# Movement Directions
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2
PORTAL = 3

# Entities
PLAYER = 0
PELLET = 1
POWERP = 2
ENEMY = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 100, 150)
TEAL = (100, 255, 255)
ORANGE = (230, 190, 40)

# Values
POINTS = 200
SPEED = 50