import pygame
from settings import *
from Graphic_Image import *
vec = pygame.math.Vector2
from Basic_Sprite_Types import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, pic = None):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.Player = self
        if pic == None:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill(YELLOW)
        else:
            self.image = get_image(pic)

        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILE_SIZE


    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x= PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt

        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
MAP_KEY['P'] = lambda game, x, y: Player(game, x, y, PLAYER_IMAGE)

class Wall(Basic_Sprite):
    def __init__(self, game, x, y, image = None):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        Basic_Sprite.__init__(self, game, x, y, image)

MAP_KEY['W'] = lambda game, x, y: Wall(game, x, y, "Cement.bmp")
MAP_KEY['1'] = lambda game, x, y: Wall(game, x, y, "Red_Brick.bmp")