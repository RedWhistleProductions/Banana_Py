from os import path

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREY = (40, 40, 40)
LIGHT_GREY = (100, 100, 100)

# game options/settings
TITLE = "Bananas Game Engine"
WIDTH = 32 * 40  # 1280 1024
HEIGHT = 32 * 24  # 704 768
FULL_SCREEN = True
FPS = 30
BGCOLOR = WHITE

TILE_SIZE = 32
GRID_WIDTH = WIDTH / TILE_SIZE  # 32
GRID_HEIGHT = HEIGHT / TILE_SIZE  # 24

# Player Settings
PLAYER_SPEED = 7 * TILE_SIZE
PLAYER_IMAGE = "ball.png"

GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, "Maps")
IMAGE_FOLDER = path.join(GAME_FOLDER, "Images")
MAP_KEY = {}

