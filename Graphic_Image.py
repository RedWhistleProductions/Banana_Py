import os
from Game_Screen import *

_image_library = {}
def get_image(path, key = (255, 255, 255)):
        global _image_library
        image = _image_library.get(path)

        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                _image_library[path] = image.set_colorkey(key)
        return image