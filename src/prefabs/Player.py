import pygame

from src.prefabs.MousePointer import MousePointer
from src.utils.spritesheet import SpriteSheet


class Player:
    speed = 0.1
    offset = [0, 0]
    sprites_delay = 7
    sprites_delay_count = sprites_delay

    def __init__(self, app):
        self.app = app
        sheets = SpriteSheet(app.RESOURCES["IMAGE"]["poong-sheet.png"])
        self.sprites = [
            sheets.image_at((0, 0, 30, 30)),
            sheets.image_at((30, 0, 30, 30)),
            sheets.image_at((60, 0, 30, 30))
        ]
        self.sheet_index = 0
        self.image = self.sprites[self.sheet_index]

        self.size = self.image.get_rect().size
        self.setup_mouse()
        self.offset = [self.image.get_width() / 2, self.image.get_height() / 2]
        self.set_position([0, 0])

        self.reset()

    def reset(self):
        self.destination = None
        self.departure = None
        self.rect = None

    def setup_mouse(self):
        self.mouse = MousePointer(self.app, self)

    def set_position(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position, self.size)
        self.rect.left = self.position[0] - self.size[0] / 2
        self.rect.top = self.position[1] - self.size[1] / 2

    def set_pos_x(self, x):
        self.set_position([x, self.position[1]])

    def set_pos_y(self, y):
        self.set_position([self.position[0], y])

    def set_speed(self, speed):
        self.speed = speed

    def forward(self, destination):
        self.destination = destination
        self.departure = self.position

    def death(self):
        self.reset()
        self.set_position([150, 100])

    def on_collision(self):
        self.position = self.last_position

    def update_sprites(self):
        self.sprites_delay_count -= 1
        if self.sprites_delay_count == 0:
            self.sheet_index += 1
            if self.sheet_index >= self.sprites.__len__():
                self.sheet_index = 0
            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay

    def update(self):
        screen = self.app.screen
        self.last_position = self.position
        if self.destination is not None:
            horizontal_direction = (
                1 if self.destination[0] - self.departure[0] > 0 else -1
            )
            vertical_direction = (
                1 if self.destination[1] - self.departure[1] > 0 else -1
            )

            distance_x = abs(self.destination[0] - self.departure[0])
            distance_y = abs(self.destination[1] - self.departure[1])
            delta_speed = self.speed * self.app.delta_time
            if distance_x > distance_y:
                self.set_pos_x(self.position[0] + (delta_speed * horizontal_direction))
                self.set_pos_y(
                    self.position[1]
                    + ((distance_y / distance_x) * delta_speed * vertical_direction)
                )

            if distance_x < distance_y:
                self.set_pos_x(
                    self.position[0]
                    + ((distance_x / distance_y) * delta_speed * horizontal_direction)
                )
                self.set_pos_y(self.position[1] + (delta_speed * vertical_direction))

            if abs(self.position[0] - self.departure[0]) > abs(
                    self.destination[0] - self.departure[0]
            ):
                abs(self.position[0] - self.departure[0]) > abs(
                    self.destination[0] - self.departure[0]
                )
                self.set_pos_x(self.destination[0])

            if abs(self.position[1] - self.departure[1]) > abs(
                    self.destination[1] - self.departure[1]
            ):
                self.set_pos_y(self.destination[1])

        screen.blit(self.image, self.rect)

        self.mouse.update()
        self.update_sprites()
