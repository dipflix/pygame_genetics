import pygame

from objects.world.tile import Tile


class Chunk(pygame.sprite.Group):
    def __init__(self, rect: pygame.Rect, objects: list[list[int]]):
        super().__init__()

        self.rect = rect

        self.objects = objects
        self._dimension = len(objects)
        self._init_tiles()

    def _init_tiles(self):
        tiles: list[Tile] = []

        from main import TILES_VAR, TILE_SIZE
        for x in range(self._dimension):
            for y in range(self._dimension):
                tiles.append(
                    Tile(
                        TILES_VAR[self.objects[x][y]],
                        x * TILE_SIZE + self.rect.x * TILE_SIZE,
                        y * TILE_SIZE + self.rect.y * TILE_SIZE
                    )
                )

        self.add(tiles)
