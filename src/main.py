"""
Module: main_game_module

This module serves as the entry point for the RacingGame application,
 initializing the game environment and running the game loop.


"""

from os import environ

from components.game import RacingGame

# Hide Pygame support prompt
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

if __name__ == "__main__":
    RacingGame().run_game()
