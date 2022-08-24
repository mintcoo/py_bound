class Bomb:
    animation_frames = 3
    animation_index = 0
    animation_delay = 5
    animation_delay_count = animation_delay

    def __init__(self, position, screen, IMAGE):
        self.position = position
        self.screen = screen
        self.IMAGE = IMAGE

        self.set_image(IMAGE["bomb01.png"])

    def set_image(self, image):
        self.image = image

    def update(self):
        screen = self.screen

        target_image_filename = f"bomb{str(self.animation_index + 1).zfill(2)}.png"
        self.set_image(self.IMAGE[target_image_filename])
        screen.blit(self.image, self.position)

        self.animate()

    def animate(self):
        if self.animation_delay_count > 0:
            self.animation_delay_count -= 1
            return

        self.animation_index += 1
        # 프레임 변경
        if self.animation_index >= self.animation_frames:
            self.animation_index = 0

        self.animation_delay_count = self.animation_delay

        # 투명도
        # alpha = 0
        # if self.animation_index > 0:
        #     alpha = 255 * ((self.animation_index + 1) / 10)

        # self.image.set_alpha(alpha)
