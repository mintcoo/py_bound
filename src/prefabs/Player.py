import pygame


class Player:
    speed = 0.1

    def __init__(self, app):
        self.app = app
        self.image = app.RESOURCES["IMAGE"]["poong.png"]

        self.size = self.image.get_rect().size
        self.position = (0, 0)

    def set_position(self, position):
        self.position = position

    def set_pos_x(self, x):
        self.set_position(x, self.position[1])

    def set_pos_y(self, y):
        self.set_position(self.position[0], y)

    def set_speed(self, speed):
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(self.position, self.size)

    def update(self):
        pass
