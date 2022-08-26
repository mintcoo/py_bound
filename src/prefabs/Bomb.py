from copy import copy, deepcopy

import pygame


class Bomb:
    def __init__(self, position, app):
        self.app = app
        self.position = position
        self.screen = app.screen
        self.RESOURCES = app.RESOURCES
        self.IMAGE = self.RESOURCES["IMAGE"]
        self.AUDIO = self.RESOURCES["AUDIO"]
        self.is_collider = True

        self.animation_index = 0
        self.animation_delay = 3
        self.animation_delay_count = self.animation_delay + 0

        IMAGE = self.IMAGE
        # self.sprites = [IMAGE["over1.png"], IMAGE["over2.png"], IMAGE["over3.png"], IMAGE["over4.png"]]
        self.sprites = [
            IMAGE["bomb01.png"],
            IMAGE["bomb02.png"],
            IMAGE["bomb03.png"],
            IMAGE["bomb04.png"],
            IMAGE["bomb05.png"],
        ]

        for index, sprite in enumerate(self.sprites):
            self.sprites[index] = pygame.transform.scale(sprite, (100, 100))

        self.reset()

    def reset(self):
        self.image = self.sprites[0]
        self.animated = False
        self.animation_index = 0

    def set_image(self, image):
        self.image = image

    def update(self):
        self.animate()

        if self.animation_index + 1 == self.sprites.__len__():
            self.animated = True

    def play_explode(self):
        channel = pygame.mixer.get_num_channels()
        pygame.mixer.set_num_channels(channel + 1)
        self.AUDIO["bomb.wav"].set_volume(0.3)
        self.AUDIO["bomb.wav"].play()

    def animate(self):
        # set animation draw speed(delay)
        if self.animation_delay_count > 0:
            self.animation_delay_count -= 1

        if self.animation_delay_count == 0:
            self.animation_delay_count = self.animation_delay
            self.on_change_animation_frame()

        # 투명도
        alpha = 255
        if self.animation_index > 0:
            alpha = (
                255 * ((self.sprites.__len__() - self.animation_index * 10) + 70) / 100
            )

        self.set_image(self.sprites[self.animation_index])
        self.image.set_alpha(alpha)
        self.screen.blit(self.image, self.position)

    def on_change_animation_frame(self):
        if self.animation_index == 0:
            self.play_explode()

        self.animation_index += 1
        if self.animation_index >= self.sprites.__len__():
            self.animation_index = 0
