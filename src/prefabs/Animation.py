import pygame


class Animation:
    delay = 10
    delay_count = delay

    def __init__(self, sheet, app, delay=10):
        self.app = app
        self.sheet = sheet
        self.sprites = []

        self.sprite_index = 0
        self.delay = delay
        self.delay_count = self.delay
        self.position = [0, 0]

    def reset(self):
        self.sprite_index = 0
        self.delay_count = self.delay

    def set_position(self, position):
        self.position = position

    def set_sprites(self, rects):
        self.sprites = []
        for rect in rects:
            self.sprites.append(self.sheet.image_at(rect))

        self.delay_count = self.sprites.__len__()

    def get_rect(self):
        return pygame.Rect(self.position, self.sprites[self.sprite_index].get_size())

    def update(self):
        screen = self.app.screen

        self.delay_count -= 1
        if self.delay_count <= 0:
            self.delay_count = self.delay
            self.sprite_index += 1
            if self.sprite_index >= self.sprites.__len__():
                self.on_animation_end()

        screen.blit(self.sprites[self.sprite_index], self.position)

    def on_animation_end(self):
        self.sprite_index = 0
