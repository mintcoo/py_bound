import os

import pygame

from src.prefabs.MousePointer import MousePointer


class Application:
    RESOURCES = {"IMAGE": {}, "AUDIO": {}}

    def __init__(self, size=(100, 100), fps=60, title="Untitled"):

        # initialize for just app
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.size = size
        self.fps = fps
        self.delta_time = 0
        self.is_running = False
        self.game_objects = []

        # 화면 타이틀 설정
        pygame.display.set_caption("Bound")

        # 기타 초기화
        self.load_resources()

    def load_resources(self):
        for (dirpath, dirnames, filenames) in os.walk(f"resources/images"):
            for filename in filenames:
                self.RESOURCES["IMAGE"][f"{filename}"] = pygame.image.load(
                    f"{dirpath}/{filename}"
                )

        for (dirpath, dirnames, filenames) in os.walk(f"resources/music"):
            for filename in filenames:
                self.RESOURCES["AUDIO"][f"{filename}"] = pygame.mixer.Sound(
                    f"{dirpath}/{filename}"
                )

    def set_delta_time(self, time):
        self.delta_time = time
