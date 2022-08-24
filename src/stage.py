class Stage:
    def __init__(self, bombs, screen):
        self.bombs = bombs
        self.screen = screen

    def update(self):
        for bomb in self.bombs:
            bomb.update()
