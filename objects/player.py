import pygame
from pygame import Vector2

from objects.base.game_object import GameObject


class Player(GameObject):
    def __init__(self, position: Vector2, sprite, speed=10):
        super().__init__(sprite, position)

        self.speed = speed

        self.is_move = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.position.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.position.x += self.speed
        if keys[pygame.K_UP]:
            self.position.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.position.y += self.speed

    def update(self):
        self.move(pygame.key.get_pressed())
        self.rect.center = self.position
