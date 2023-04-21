import pygame
import pygame as pg
from pygame import Vector2, Surface

from constants.colors import Colors


class GameObject(pg.sprite.Sprite):
    def __init__(self, sprite: Surface, position: Vector2):
        super().__init__()
        self.image = sprite
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        pass
