import os
import pygame
from settings import *
from os import path

_image_library = {}


def get_image(file, key = (255, 255, 255)):
    if file is None:
        return None

    global _image_library
    file = path.join(IMAGE_FOLDER, file)
    image = _image_library.get(path)

    if image == None:
        canonicalized_path = file.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)

        _image_library[file] = image.set_colorkey(key)

    return image


def get_sprite(sprite_name, file = None, rectangle = None, key = (255, 255, 255)):
    if sprite_name in _image_library:
        return _image_library[sprite_name]
    else:
        if file is None:
            print("Error: Sprite not loaded, because the Sprite Sheet isn't loaded")
            pygame.quit()
            exit()

        sprite_sheet = get_image(file, key)

        if sprite_name is None or rectangle is None:
            return sprite_sheet
        else:
            rect = pygame.Rect(rectangle)
            image = pygame.Surface(rect.size)
            image.blit(sprite_sheet, (0, 0), rect)
            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            _image_library[sprite_name] = image.set_colorkey(key)
            return image


