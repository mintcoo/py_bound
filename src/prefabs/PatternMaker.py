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
        print(index)
        return getattr(self, f'stage_{index}')()

    def stage_0(self):
        loc1 = (400, 50)
        loc2 = (500, 50)
        loc3 = (600, 50)
        loc4 = (700, 50)
        loc5 = (800, 50)
        loc6 = (900, 50)
        loc7 = (1000, 50)
        loc8 = (1100, 50)

        return [
            [loc1, loc3, loc5, loc7],
            1000,
            [loc2, loc4, loc6, loc8],
            1000,
        ]

    def stage_1(self):
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
            550,
            [location7],
            550,
            [location6],
            550,
            [location5],
            550,
            [location4],
            550,
            [location3],
            550,
            [location2],
            550,
            [location1],
            550,
            [location1, location2, location3, location4],
            550,
            [location5, location6, location7, location8],
            550,
            [location1, location2, location3, location4],
            550,
            [location5, location6, location7, location8],
            550,
            [location1, location2, location3, location4],
            550,
            [
                location1,
                location2,
                location3,
                location5,
                location6,
                location7,
                location8,
            ],
            900,
            [
                location1,
                location2,
                location4,
                location5,
                location6,
                location7,
                location8,
            ],
            800,
        ]
