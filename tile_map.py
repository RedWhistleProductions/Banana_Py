import pygame
from settings import *
import csv


class Map_CSV:
    def __init__(self, map_file = "Test.map"):
        self.data = []

        with open(path.join(MAP_FOLDER, map_file)) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                self.data.append(row)

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

