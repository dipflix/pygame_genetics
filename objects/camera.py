from pygame import Vector2


class Camera:
    def __init__(self, position: Vector2, scale=1):
        self.position = position
        self.scale = scale

    def followTo(self, position: Vector2):
        self.position = self.position.lerp(position, 0.05)
