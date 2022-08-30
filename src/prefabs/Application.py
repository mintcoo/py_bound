import json
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
        self.load_pattern_files()

    def load_resources(self):
        folders = ['monsters', 'zolaman', 'weapon']
        for (dirpath, dirnames, filenames) in os.walk(f"resources/images"):
            for filename in filenames:
                self.RESOURCES["IMAGE"][f"{filename}"] = pygame.image.load(
                    f"{dirpath}/{filename}"
                )

        for inner_folder_name in folders:
            for (dirpath, dirnames, filenames) in os.walk(f"resources/images/{inner_folder_name}"):
                for filename in filenames:
                    self.RESOURCES["IMAGE"][f"{inner_folder_name}/{filename}"] = pygame.image.load(
                        f"{dirpath}/{filename}"
                    )

        for (dirpath, dirnames, filenames) in os.walk(f"resources/audios"):
            for filename in filenames:
                self.RESOURCES["AUDIO"][f"{filename}"] = pygame.mixer.Sound(
                    f"{dirpath}/{filename}"
                )

    def load_pattern_files(self):
        patterns_data = []
        for (dirpath, dirnames, filenames) in os.walk(f"resources/patterns"):
            for filename in filenames:
                try:
                    loaded_map = open(f"{dirpath}/{filename}", "r")
                    data = json.loads(loaded_map.read())
                    patterns_data.append(self.json_to_pattern_data(data))
                except Exception as error:
                    print(f"{filename} - {error}")
                    raise error

        self.stages = patterns_data

    def json_to_pattern_data(self, data):
        patterns = []
        for pattern in data["patterns"]:
            if type(pattern).__name__ == "list":
                pattern = list(
                    map(lambda location_name: data["locations"][location_name], pattern)
                )
            patterns.append(pattern)

        return patterns

    def set_delta_time(self, time):
        self.delta_time = time
