"""
Module: sound_module

This module defines a SoundEnum enumeration and a SoundFactory class for managing
and loading sound assets in the RacingGame application.

"""

from enum import Enum

import pygame


class SoundEnum(Enum):
    """
    Enumeration representing different types of sounds used in the game.

    Values:
        ACCELERATION_SOUND: Sound for acceleration.
        WINNING_SOUND: Sound for winning.
        LOSING_SOUND: Sound for losing.
    """

    ACCELERATION_SOUND = "src/assets/sounds/acceleration.mp3"
    WINNING_SOUND = "src/assets/sounds/winning.mp3"
    LOSING_SOUND = "src/assets/sounds/losing.mp3"


class SoundFactory:
    """
    Factory class for loading and obtaining sound objects based on the specified SoundEnum type.

    Methods:
        load_sound(src: str):
            Loads a sound object from the specified source file.

        get_sound(sound_type: SoundEnum):
            Obtains a sound object based on the specified SoundEnum type.

    """

    @staticmethod
    def load_sound(src: str):
        """
        Loads a sound object from the specified source file.

        Args:
            src (str): The file path of the sound.

        Returns:
            pygame.mixer.Sound: The loaded sound object.
        """
        return pygame.mixer.Sound(src)

    @staticmethod
    def get_sound(sound_type: SoundEnum):
        """
        Obtains a sound object based on the specified SoundEnum type.

        Args:
            sound_type (SoundEnum): The type of sound to obtain.

        Returns:
            pygame.mixer.Sound: The obtained sound object.
        """
        if sound_type == SoundEnum.ACCELERATION_SOUND:
            return SoundFactory.load_sound(SoundEnum.ACCELERATION_SOUND.value)
        if sound_type == SoundEnum.WINNING_SOUND:
            return SoundFactory.load_sound(SoundEnum.WINNING_SOUND.value)
        if sound_type == SoundEnum.LOSING_SOUND:
            return SoundFactory.load_sound(SoundEnum.LOSING_SOUND.value)
        raise ValueError("Invalid sound type")
