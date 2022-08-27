from src.prefabs.Bomb import Bomb


class PatternMaker:
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen
        self.RESOURCES = app.RESOURCES
        self.IMAGE = app.RESOURCES["IMAGE"]

    def create(self, patterns=[]):
        for pattern in patterns:
            if type(pattern).__name__ == "list":
                for index, position in enumerate(pattern):
                    pattern[index] = Bomb(position, self.app)

        return patterns

    def get_stage(self, index):
        return self.app.stages[index]
