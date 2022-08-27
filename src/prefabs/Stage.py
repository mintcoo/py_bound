class Stage:
    patterns = []
    pattern_index = 0
    waited = 0

    def __init__(self, patterns, app):
        self.app = app
        self.screen = self.app.screen

        self.patterns = patterns
        self.current_pattern = self.patterns[self.pattern_index]

    def trigger(self, pattern, delta_time):
        class_name = type(pattern).__name__

        if class_name == "list":
            is_completed = self.explode_bombs(pattern)
            if is_completed:
                for bomb in pattern:
                    bomb.reset()
            self.next_pattern()

        if class_name == "int":
            destination_wait = pattern
            self.waited += delta_time
            if self.waited >= destination_wait:
                self.next_pattern()

    def explode_bombs(self, bombs):
        is_completed = True
        for bomb in bombs:
            # bomb.update()
            self.app.game_objects.append(bomb)

            if is_completed == False:
                continue

            is_completed = bomb.animated

        return is_completed

    def next_pattern(self):
        self.pattern_index += 1
        if self.pattern_index >= self.patterns.__len__():
            self.pattern_index = 0

        self.current_pattern = self.patterns[self.pattern_index]
        if type(self.current_pattern).__name__ == "list":
            for pattern in self.current_pattern:
                pattern.reset()

        self.waited = 0

    def update(self, delta_time):
        self.trigger(self.current_pattern, delta_time)
