import pygame
from settings import *
from Graphic_Image import *
vec = pygame.math.Vector2
from Basic_Sprite_Types import *
from Animation import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, pic = None):
        self.groups = ALL_SPRITES
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.Player = self

        self.Animation_Standing = Animation()
        self.Animation_Up = Animation()
        self.Animation_Down = Animation()
        self.Animation_Left = Animation()
        self.Animation_Right = Animation()
        self.Current_Animation = self.Animation_Standing

        if pic == None:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill(YELLOW)
        else:
            self.image = get_image(pic)
            self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILE_SIZE


    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
            if self.Current_Animation != self.Animation_Left:
                self.Current_Animation.Reset()
                self.Current_Animation = self.Animation_Left

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x= PLAYER_SPEED
            if self.Current_Animation != self.Animation_Right:
                self.Current_Animation.Reset()
                self.Current_Animation = self.Animation_Right

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
            if self.Current_Animation != self.Animation_Up:
                self.Current_Animation.Reset()
                self.Current_Animation = self.Animation_Up

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            if self.Current_Animation != self.Animation_Down:
                self.Current_Animation.Reset()
                self.Current_Animation = self.Animation_Down

        else:
            if self.Current_Animation != self.Animation_Standing:
                self.Current_Animation.Reset()
                self.Current_Animation = self.Animation_Standing

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, WALLS, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, WALLS, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * CLOCK.tick(FPS) / 1000
        if self.Current_Animation.pics.__len__() > 0:
            self.image = self.Current_Animation.Update()
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')


MAP_KEY['P'] = lambda x, y: Player(x, y, PLAYER_IMAGE)

class Wall(Basic_Sprite):
    def __init__(self, x, y, image = None):

        self.groups = ALL_SPRITES, WALLS
        pygame.sprite.Sprite.__init__(self, self.groups)
        Basic_Sprite.__init__(self, x, y, image)


MAP_KEY['W'] = lambda x, y: Wall(x, y, "Cement.bmp")
MAP_KEY['1'] = lambda x, y: Wall(x, y, "Red_Brick.bmp")