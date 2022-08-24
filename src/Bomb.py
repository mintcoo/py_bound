import pygame


class Bomb:
    animation_index = 0
    animation_delay = 5
    animation_delay_count = animation_delay

    def __init__(self, position, screen, IMAGE):
        self.position = position
        self.screen = screen
        self.IMAGE = IMAGE

        # self.sprites = [IMAGE["over1.png"], IMAGE["over2.png"], IMAGE["over3.png"], IMAGE["over4.png"]]
        self.sprites = [IMAGE["bomb01.png"], IMAGE["bomb02.png"], IMAGE["bomb03.png"], IMAGE["bomb04.png"],
                        IMAGE["bomb05.png"]]

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

    def animate(self):
        if self.animation_delay_count > 0:
            self.animation_delay_count -= 1
            self.screen.blit(self.image, self.position)
            return

        # delay, set frame
        self.animation_delay_count = self.animation_delay
        self.animation_index += 1

        # 프레임 변경
        if self.animation_index >= self.sprites.__len__():
            self.animation_index = 0

        # 투명도
        alpha = 255
        if self.animation_index > 0:
            alpha = 255 * ((self.sprites.__len__() - self.animation_index * 10) + 70) / 100

        self.set_image(self.sprites[self.animation_index])
        self.image.set_alpha(alpha)
        self.screen.blit(self.image, self.position)
