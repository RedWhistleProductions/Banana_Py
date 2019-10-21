import pygame
import sys
from settings import *
from os import path
from Player import *
from tile_map import *
from Camera import *
from functools import partial
from Basic_Sprite_Types import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        if FULL_SCREEN:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()


    def load_data(self):
        self.map = Map_CSV("Test_2.map")


    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.curent_map = pygame.sprite.Group()
        self.SOLID_SPRITES = pygame.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):


                if tile in MAP_KEY:
                    foo = MAP_KEY[tile]
                    if tile == 'P':
                        self.player = foo(self, col, row)
                    else:
                        foo(self, col, row)




        self.camera = Camera(self.map.width, self.map.height)
        # def Load(self, sheet_name, animation_name, num_pics, start_x, start_y, w, h):
        self.player.Animation_Right.Load("links.gif", "Link_Right", 8, 0, 0, 70, 100, 30)
        self.player.Animation_Down.Load("links.gif", "Link_Down", 8, 800, 0, 70, 100, 30)
        self.player.Animation_Left.Load("links.gif", "Link_Left", 8, 1600, 0, 70, 100, 30)
        self.player.Animation_Up.Load("links.gif", "Link_Up", 8, 2400, 0, 70, 100, 30)

        self.player.Animation_Standing.Add_Pic("Link_Standing", "links.gif", (800, 0, 70, 100))
        # self.player.Animation_Standing.Add_Pic("ball.png")
        # self.player.Animation_Standing.Add_Pic("Grass.bmp")
        # self.player.Animation_Standing.Add_Pic("Dirt.bmp")


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        # Game Loop - events
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def draw(self):
        self.screen.fill(BGCOLOR)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, LIGHT_GREY, (0, y), (WIDTH, y))

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()