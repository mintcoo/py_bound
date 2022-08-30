import pygame


class GameObject:
    name = None
    tags = []
    is_start_function_called = False

    def __init__(self):
        pass

    def update(self):
        pass

    def start(self):
        self.is_start_function_called = True
