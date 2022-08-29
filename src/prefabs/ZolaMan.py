import pygame

from src.prefabs.GameObject import GameObject
from src.utils.spritesheet import SpriteSheet


class ZolaMan(GameObject):
    speed = 0.1
    offset = [0, 0]
    sprites_delay = 10
    sprites_delay_count = sprites_delay
    status = "neutral"

    def __init__(self, app):
        self.app = app
        sheets = SpriteSheet(app.RESOURCES["IMAGE"]["zolasheet.png"])
        self.sprites = [
            sheets.image_at((0, 0, 15, 30)),
            sheets.image_at((15, 0, 15, 30)),
            sheets.image_at((30, 0, 15, 30))
        ]
        self.sheet_index = 0
        self.image = self.sprites[self.sheet_index]
        self.size = self.image.get_rect().size

    def set_position(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position, self.size)
        self.rect.left = self.position[0] - self.size[0] / 2
        self.rect.top = self.position[1] - self.size[1] / 2

    def update_sprite(self):
        if self.status == '1neutral':
            self.sheet_index = 0
            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay
            return

        self.sprites_delay_count -= 1
        if self.sprites_delay_count == 0:
            self.sheet_index += 1
            if self.sheet_index >= self.sprites.__len__():
                self.sheet_index = 0
            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay

    def update(self):
        screen = self.app.screen
        screen.blit(self.image, self.rect)
        self.update_sprite()
