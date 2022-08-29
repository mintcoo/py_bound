import pygame

from src.prefabs.GameObject import GameObject
from src.prefabs.ZolaMan import ZolaMan
from src.utils.spritesheet import SpriteSheet


class Snail(GameObject):
    tags = ["Monster"]
    speed = 0.1
    sheet_index = 0
    sprites_delay = 10
    sprites_delay_count = sprites_delay
    status = "neutral"

    def __init__(self, app):
        self.app = app
        self.set_sheets()

    def set_sheets(self):
        RESOURCES = self.app.RESOURCES
        move_sheet = SpriteSheet(RESOURCES["IMAGE"]["monsters/snail_move.png"])
        death_sheet = RESOURCES["IMAGE"]["monsters/snail_move.png"]

        self.sprites = [
            move_sheet.image_at((37 * 0, 0, 37, 26)),
            move_sheet.image_at((37 * 1, 0, 37, 26)),
            move_sheet.image_at((37 * 2, 0, 37, 26)),
            move_sheet.image_at((37 * 3, 0, 37, 26)),
            move_sheet.image_at((37 * 4, 0, 37, 26)),
        ]
        self.image = self.sprites[0]
        self.rect = self.sprites[0].get_rect()

    def set_position(self, position):
        self.position = position
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.position, self.image.get_rect().size)
        self.rect.left = self.position[0] - self.rect.size[0] / 2
        self.rect.top = self.position[1] - self.rect.size[1] / 2

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

    def start(self):
        [zolaman] = list(filter(lambda instance: instance.__class__.__name__ == 'ZolaMan', self.app.game_objects))
        self.zolaman = zolaman

    def forward(self, destination):
        self.update_rect()
        if self.rect.collidepoint(destination):
            return
        self.set_position([self.position[0] - self.speed * self.app.delta_time, self.position[1]])

    def update(self):
        screen = self.app.screen
        screen.blit(self.image, self.rect)

        self.forward(self.zolaman.position)

        self.update_sprite()
