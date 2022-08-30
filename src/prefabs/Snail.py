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
    is_death_ready = False

    def __init__(self, app):
        self.app = app
        self.set_sheet('move')

    def reset(self):
        self.sheet_index = 0
        self.sprites_delay_count = self.sprites_delay

    def set_sheet(self, status):
        RESOURCES = self.app.RESOURCES

        self.reset()
        sheet = None
        width, height = 0, 0

        if status == 'move':
            sheet = SpriteSheet(RESOURCES["IMAGE"]["monsters/snail_move.png"])
            width, height = 37, 26
        if status == 'death':
            self.is_death_ready = True
            sheet = SpriteSheet(RESOURCES["IMAGE"]["monsters/snail_death.png"])
            width, height = 45, 33

        self.sprites = [
            sheet.image_at((width * 0, 0, width, height)),
            sheet.image_at((width * 1, 0, width, height)),
            sheet.image_at((width * 2, 0, width, height)),
            sheet.image_at((width * 3, 0, width, height)),
            sheet.image_at((width * 4, 0, width, height)),
        ]
        self.image = self.sprites[0]
        self.rect = self.sprites[0].get_rect()

    def destroy(self):
        self.app.game_objects.remove(self)

    def set_position(self, position):
        self.position = position
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.position, self.image.get_rect().size)
        self.rect.left = self.position[0] - self.rect.size[0] / 2
        self.rect.top = self.position[1] - self.rect.size[1] / 2

    def update_sprite(self):
        self.sprites_delay_count -= 1
        if self.sprites_delay_count == 0:
            self.sheet_index += 1
            if self.sheet_index >= self.sprites.__len__():
                self.sheet_index = 0
                if self.is_death_ready:
                    self.destroy()

            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay

    def start(self):
        super().start()
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
