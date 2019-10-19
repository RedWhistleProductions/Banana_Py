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
        # def Add_Pic(self, sprite_name, sheet_name = None, rectangle = None, key = (255, 255, 255))
        self.player.Animation_Right.Add_Pic("Link_Right_0", "links.gif", (0, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_1", "links.gif", (100, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_2", "links.gif", (200, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_3", "links.gif", (300, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_4", "links.gif", (400, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_5", "links.gif", (500, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_6", "links.gif", (600, 0, 70, 100))
        self.player.Animation_Right.Add_Pic("Link_Right_7", "links.gif", (700, 0, 70, 100))

        self.player.Animation_Down.Add_Pic("Link_Down_0", "links.gif", (800, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_1", "links.gif", (900, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_2", "links.gif", (1000, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_3", "links.gif", (1100, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_4", "links.gif", (1200, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_5", "links.gif", (1300, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_6", "links.gif", (1400, 0, 70, 100))
        self.player.Animation_Down.Add_Pic("Link_Down_7", "links.gif", (1500, 0, 70, 100))

        self.player.Animation_Left.Add_Pic("Link_Left_0", "links.gif", (1600, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_1", "links.gif", (1700, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_2", "links.gif", (1800, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_3", "links.gif", (1900, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_4", "links.gif", (2000, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_5", "links.gif", (2100, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_6", "links.gif", (2200, 0, 70, 100))
        self.player.Animation_Left.Add_Pic("Link_Left_7", "links.gif", (2300, 0, 70, 100))

        self.player.Animation_Up.Add_Pic("Link_Up_0", "links.gif", (2400, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_1", "links.gif", (2500, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_2", "links.gif", (2600, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_3", "links.gif", (2700, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_4", "links.gif", (2800, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_5", "links.gif", (2900, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_6", "links.gif", (3000, 0, 70, 100))
        self.player.Animation_Up.Add_Pic("Link_Up_7", "links.gif", (3100, 0, 70, 100))

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