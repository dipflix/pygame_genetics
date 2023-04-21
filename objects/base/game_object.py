import pygame
import pygame as pg
from pygame import Vector2, Surface

from constants.colors import Colors


class GameObject(pg.sprite.Sprite):
    def __init__(self, sprite: Surface, position: Vector2):
        super().__init__()
        self.image = sprite
        self.position = position
        self.rect = pygame.rect.Rect(
            left=position.x,
            top=position.y,
            width=self.image.get_width(),
            height=self.image.get_height()
        )

    def update(self):
        pass
