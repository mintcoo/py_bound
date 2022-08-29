import pygame

from src.prefabs.GameObject import GameObject
from src.utils.spritesheet import SpriteSheet


class ZolaMan(GameObject):
    speed = 0.1
    offset = [0, 0]
    sprites_delay = 10
    sprites_delay_count = sprites_delay
    status = "neutral"
    attack_speed = 1000
    attack_speed_delay_count = attack_speed

    def __init__(self, app):
        self.app = app
        self.sprites = []
        self.set_status('neutral')
        self.size = self.image.get_rect().size

    def set_position(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position, self.size)
        self.rect.left = self.position[0] - self.size[0] / 2
        self.rect.top = self.position[1] - self.size[1] / 2

    def set_status(self, status):
        app = self.app
        sheet = []
        idle_sheet = SpriteSheet(app.RESOURCES["IMAGE"]["zolaman/zola-idle.png"])
        attack_sheet = SpriteSheet(app.RESOURCES["IMAGE"]["zolaman/zola-attack.png"])
        if status == 'neutral':
            sheet = [
                idle_sheet.image_at((0, 0, 15, 30)),
                idle_sheet.image_at((15, 0, 15, 30)),
                idle_sheet.image_at((30, 0, 15, 30))
            ]

        if status == 'attack':
            sheet = [
                attack_sheet.image_at((0, 0, 20, 30)),
                attack_sheet.image_at((20, 0, 20, 30)),
                attack_sheet.image_at((40, 0, 20, 30))
            ]

        self.sprites = sheet

        self.sprites_delay_count = self.sprites_delay
        self.sheet_index = 0
        self.image = self.sprites[0]

        self.status = status

    def update_sprite(self):

        # if self.status == 'attack':
        self.attack_speed_delay_count -= self.app.delta_time
        if self.attack_speed_delay_count <= 0:
            self.attack_speed_delay_count = self.attack_speed
            self.set_status('attack')

        self.sprites_delay_count -= 1
        if self.sprites_delay_count == 0:
            self.sheet_index += 1
            if self.sheet_index >= self.sprites.__len__():
                self.sheet_index = 0
                self.on_sprite_animation_end()
                pass
            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay

    def on_sprite_animation_end(self):
        if self.status == 'attack':
            self.set_status('neutral')

    def update(self):
        screen = self.app.screen
        screen.blit(self.image, self.rect)
        self.update_sprite()
