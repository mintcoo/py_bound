from src.Bomb import Bomb


class PatternMaker:

    def __init__(self, screen, RESOURCES):
        self.screen = screen
        self.RESOURCES = RESOURCES
        self.IMAGE = RESOURCES["IMAGE"]

    def create(self):
        patterns = self.get_stage_one()
        for pattern in patterns:

            if type(pattern).__name__ == 'list':
                for index, position in enumerate(pattern):
                    pattern[index] = Bomb(position, self.screen, self.RESOURCES)

        return patterns

    def get_stage_one(self):
        location1 = (400, 50)
        location2 = (500, 50)
        location3 = (600, 50)
        location4 = (700, 50)
        location5 = (800, 50)
        location6 = (900, 50)
        location7 = (1000, 50)
        location8 = (1100, 50)

        return [
            [location8],
            400,
            [location7],
            400,
            [location6],
            400,
            [location5],
            400,
            [location4],
            400,
            [location3],
            400,
            [location2],
            400,
            [location1],
            400,
            [location1, location2, location3, location4],
            400,
            [location5, location6, location7, location8],
            400,
            [location1, location2, location3, location4],
            400,
            [location5, location6, location7, location8],
            400,
            [location1, location2, location3, location4],
            400,

            [location1, location2, location3, location5, location6, location7, location8],
            400,

            [location1, location2, location4, location5, location6, location7, location8],
            400,
        ]
