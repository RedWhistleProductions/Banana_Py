import os
import pygame
from settings import *
from os import path

_image_library = {}


def get_image(file, key = (255, 255, 255)):
    global _image_library
    file = path.join(IMAGE_FOLDER, file)
    image = _image_library.get(path)

    if image == None:
        canonicalized_path = file.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        _image_library[file] = image.set_colorkey(key)

    return image