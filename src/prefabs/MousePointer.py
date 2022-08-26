import pygame

from src.utils.constants import M_RIGHT


class MousePointer:
    preserve_time = 100  # preserve milliseconds
    preserve_time_count = 0

    def __init__(self, app, parent):
        self.app = app
        self.image = app.RESOURCES["IMAGE"]["mouse.png"]
        self.parent = parent
        self.position = (0, 0)

    def on_event(self, event):
        mouse_position = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == M_RIGHT:
                self.on_click_right_button(mouse_position)

    def on_click_right_button(self, position):
        #print(position)
        self.position = position
        self.preserve_time_count = self.preserve_time
        self.parent.forward(position)

    def update(self):
        if self.preserve_time_count <= 0:
            self.preserve_time_count = 0
            return

        screen = self.app.screen
        screen.blit(self.image,
                    (self.position[0] - self.image.get_width() / 2, self.position[1] - self.image.get_height() / 2))

        self.preserve_time_count -= self.app.delta_time
