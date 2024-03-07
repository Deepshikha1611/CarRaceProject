"""
Module: game_info_module

This module defines the GameInfo class, representing information about the game state,
including the current level, whether the game has started, and timing information.

"""

import time


class GameInfo:
    """
    Represents information about the game state, including the current level,
    whether the game has started, and timing information.

    Attributes:
        LEVELS: A class variable representing the total number of levels in the game.

    Methods:
        __init__(self, level=1):
            Initializes a GameInfo object with the specified initial level.

        next_level(self) -> None:
            Advances to the next level and resets the 'started' flag.

        reset(self) -> None:
            Resets the game state to the initial configuration.

        game_finished(self) -> bool:
            Checks if the game has finished by comparing the current level
            with the total number of levels.

        start_level(self) -> None:
            Marks the start of a new level and records the start time.

        get_level_time(self) -> int:
            Calculates and returns the time elapsed since the start of the current level.

    """

    LEVELS = 3

    def __init__(self, level=1):
        """
        Initializes a GameInfo object with the specified initial level.

        Args:
            level: The initial level of the game.

        Returns:
            None
        """
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self) -> None:
        """
        Advances to the next level and resets the 'started' flag.

        Returns:
            None
        """
        self.level += 1
        self.started = False

    def reset(self) -> None:
        """
        Resets the game state to the initial configuration.

        Returns:
            None
        """
        self.started = False
        self.level_start_time = 0

    def game_finished(self) -> bool:
        """
        Checks if the game has finished by comparing the current level with
        the total number of levels.

        Returns:
            bool: True if the game has finished, False otherwise.
        """
        return self.level > self.LEVELS

    def start_level(self) -> None:
        """
        Marks the start of a new level and records the start time.

        Returns:
            None
        """
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self) -> int:
        """
        Calculates and returns the time elapsed since the start of the current level.

        Returns:
            int: Time elapsed since the start of the current level (in seconds).
        """
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)
