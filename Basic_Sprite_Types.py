import pygame
from settings import *
from Graphic_Image import *


class Basic_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image = None):

        self.groups = ALL_SPRITES


        pygame.sprite.Sprite.__init__(self, self.groups)

        if image is None:
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


MAP_KEY['G'] = lambda x, y: Basic_Sprite(x, y, "Grass.bmp")
MAP_KEY['S'] = lambda x, y: Basic_Sprite(x, y, "Sand.bmp")
MAP_KEY['D'] = lambda x, y: Basic_Sprite(x, y, "Dirt.bmp")



