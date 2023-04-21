import random

import noise
import pygame

from objects.world.chunk import Chunk


class WorldGenerator:
    def __init__(self, area_size: tuple[int, int], seed):
        self._width = area_size[0]
        self._height = area_size[1]
        self.world = [[noise.snoise3(i / self._width, j / self._height, seed) for j in range(self._width)] for i in
                      range(self._height)]

        self.water_threshold = -0.2

    def generate(self, chunk_size) -> list[Chunk]:
        world = [
            [
                1 if self.world[i][j] < self.water_threshold
                else 0
                for j in range(self._width)
            ] for i in range(self._height)
        ]
        chunks = []

        for x in range(0, self._width, chunk_size):
            for y in range(0, self._height, chunk_size):
                chunk_rect = pygame.Rect(x, y, chunk_size, chunk_size)
                chunk = Chunk(chunk_rect, self.get_objects_in_chunk(world, chunk_rect))
                chunks.append(chunk)
        return chunks

    def get_objects_in_chunk(self, world, chunk_rect):

        chunk_objects = []
        for x in range(chunk_rect.left, chunk_rect.right):
            row = []
            for y in range(chunk_rect.top, chunk_rect.bottom):
                if x < 0 or x >= self._width or y < 0 or y >= self._height:
                    continue  # skip out-of-bounds tiles
                row.append(world[x][y])
            chunk_objects.append(row)
        return chunk_objects
