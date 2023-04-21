import pygame
import os


class Tileset(pygame.sprite.Sprite):
    def __init__(self, tileset_image, tile_size,):
        super().__init__()

        self.image = tileset_image
        self.rect = self.image.get_rect()
        self.tile_size = tile_size

        self.num_cols = tileset_image.get_width() // self.tile_size
        self.num_rows = tileset_image.get_height() // self.tile_size

        self.tiles = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                rect = pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                tile_image = self.image.subsurface(rect)
                self.tiles.append(tile_image)

    def getTile(self, index):
        return self.tiles[index]
