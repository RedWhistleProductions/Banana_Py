import pygame
from settings import *
from Graphic_Image import *
vec = pygame.math.Vector2


class Basic_Sprite(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image = None):
        self.groups = game.all_sprites, game.SOLID_SPRITES
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        if image == None:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill(GREEN)

        else:
            self.image = get_image(image)
            self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

MAP_KEY['G'] = lambda game, x, y: Basic_Sprite(game, x, y, "Grass.bmp")
MAP_KEY['S'] = lambda game, x, y: Basic_Sprite(game, x, y, "Sand.bmp")
MAP_KEY['D'] = lambda game, x, y: Basic_Sprite(game, x, y, "Dirt.bmp")



class Character(Basic_Sprite):
    def __init__(self, game, x, y, image = None):
        Basic_Sprite.__init__(self, game, x, y, image)
        self.HP = 100
        self.SP = 0
        self.Lives = 1


