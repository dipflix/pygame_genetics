import os
import random

import numpy as np
import pygame as pg
from pygame import Surface, Vector2

from constants.assets import Assets
from generators.generator import WorldGenerator
from objects.camera import Camera
from objects.player import Player
from objects.world.chunk import Chunk

pg.init()

GAME_FOLDER = os.path.dirname(__file__)

TILE_SIZE = 8

CHUNK_SIZE = TILE_SIZE * 4
CHUNK_OFFSET = (0, 0)

SCREEN_SIZE = (48 * TILE_SIZE * 2, 48 * TILE_SIZE * 2)
WORLD_SIZE = CHUNK_SIZE * 4, CHUNK_SIZE * 4

BOARD = np.zeros(WORLD_SIZE)

screen = pg.display.set_mode(SCREEN_SIZE)

ASSETS = Assets(game_folder=GAME_FOLDER)

CLOCK = pg.time.Clock()
FONT = pg.font.SysFont('Arial', 16)

# pg.event.set_grab(True)

area_generator = WorldGenerator(WORLD_SIZE, random.random())


def FPS_TEXT():
    return FONT.render("FPS: " + str(int(CLOCK.get_fps())), True, (255, 0, 0))


TILES_VAR = {
    0: ASSETS.grass_tileset.getTile(12),
    1: ASSETS.water_tileset.getTile(0),
    2: ASSETS.grass_tileset.getTile(11),
}

background = pg.sprite.Group()

sprites = pg.sprite.Group()

screen_center = Vector2(screen.get_width() // 2, screen.get_height() // 2)

player = Player(position=Vector2(screen_center), sprite=ASSETS.player, speed=5)


class Game:
    def __init__(self):
        self.dt = 0
        self.camera = Camera(screen_center, 1)

        self.chunk_size = CHUNK_SIZE
        self.world: list[Chunk] = []
        self.background: list[list[Surface]] = [[]]
        self.paused = False
        self.done = False

    def run(self):
        self.init_world()

        sprites.add(background)
        sprites.add(player)

        while not self.done:
            screen.fill((255, 255, 255), screen.get_rect())
            self.update_events()

            self.update()

            screen.blit(FPS_TEXT(), (10, 10))
            pg.display.flip()
            pg.display.update()
            CLOCK.tick(60)

        pg.quit()

    def update(self):
        self.camera.followTo(player.position - screen_center)

        for sprite in sprites:
            screen.blit(sprite.image, (sprite.rect.x - self.camera.position.x, sprite.rect.y - self.camera.position.y))
        player.update()

    def init_world(self):
        self.world = area_generator.generate(CHUNK_SIZE)

        for chunk in self.world:
            background.add(chunk)

    def update_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.paused = not self.paused

                if event.key == pg.K_q:
                    pg.quit()
                    quit()


if __name__ == '__main__':
    game = Game()
    game.run()
