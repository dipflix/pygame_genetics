import os

import pygame as pg
from pygame import Surface


from objects.utils.tileset import Tileset


class Assets:

    def __init__(self, game_folder):
        self.assets_folder = os.path.join(game_folder, 'resources')
        self.player = Tileset(self.loadAsset('characters/cow.png').convert_alpha(), 32).getTile(0)
        self.grass_tileset = Tileset(self.loadAsset('tilesets/grass.png').convert_alpha(), 16)
        self.water_tileset = Tileset(self.loadAsset('tilesets/water.png').convert_alpha(), 16)

    def loadAsset(self, file_path) -> Surface:
        image_path = os.path.join(self.assets_folder, file_path)
        return pg.image.load(image_path)


