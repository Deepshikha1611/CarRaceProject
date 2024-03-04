import time


class GameInfo:
    LEVELS = 3

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self) -> None:
        self.level += 1
        self.started = False

    def reset(self) -> None:
        # self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self) -> bool:
        return self.level > self.LEVELS

    def start_level(self) -> None:
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self) -> int:
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)
