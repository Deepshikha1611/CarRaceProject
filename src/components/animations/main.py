"""
Module: animation_module

This module defines classes related to handling animations in a game,
including the Animation class, AnimationType
enumeration, and AnimationFactory class.

"""

import os
from enum import Enum
from typing import List

import pygame


class Animation:
    """
    Represents an animation with a collection of frames loaded from a specified directory.

    Attributes:
        FRAME_RATE: A class variable representing the frame rate of the animation.
        frames: An instance variable representing the collection of frames.

    Methods:
        __init__(self, src: str):
            Initializes an Animation object with frames loaded from the specified directory.

        load_images(self, src: str) -> List[str]:
            Loads images from the specified directory and returns a list of image filenames.

        draw(self, win: pygame.Surface, clock: pygame.time.Clock) -> None:
            Draws the animation frames on the given window with the specified frame rate.

    """

    FRAME_RATE = 25

    def __init__(self, src: str) -> None:
        self.frames = self.load_images(src)

    def load_images(self, src: str) -> List[str]:
        """
        Loads images from the specified directory and returns a list of image filenames.

        Args:
            src (str): The directory containing the animation frames.

        Returns:
            List[str]: A list of image filenames.
        """
        gif_frames = []
        for lose_filename in sorted(os.listdir(src)):
            lose_frame = pygame.image.load(
                os.path.join(src, lose_filename)
            ).convert_alpha()
            gif_frames.append(lose_frame)
        return gif_frames

    def draw(self, win: pygame.Surface, clock: pygame.time.Clock) -> None:
        """
        Draws the animation frames on the given window with the specified frame rate.

        Args:
            win (pygame.Surface): The window surface on which the animation should be drawn.
            clock (pygame.time.Clock): The pygame Clock object to control the frame rate.

        Returns:
            None
        """
        frame_index = 0
        counter = 0
        while frame_index <= len(self.frames) and counter == 0:
            if frame_index == len(self.frames) - 1:
                counter += 1
            # Blit the current frame onto the screen
            win.blit(self.frames[frame_index], (30, 225))

            # Update the frame index for the next frame
            frame_index = (frame_index + 1) % len(self.frames)
            pygame.display.flip()
            clock.tick(self.FRAME_RATE)


class AnimationType(Enum):
    """
    Enumeration representing different types of animations.

    Values:
        WINNING: Animation for a winning scenario.
        LOSE: Animation for a losing scenario.
    """

    WINNING = 1
    LOSE = 2


# pylint: disable=too-few-public-methods
class AnimationFactory:
    """
    Factory class for creating instances of the Animation class
    based on the specified AnimationType.

    Methods:
        get_animation(type: AnimationType) -> Animation:
        Returns an instance of the Animation class based on the specified AnimationType.

    """

    @staticmethod
    def get_animation(animation_type: AnimationType) -> Animation:
        """
        Returns an instance of the Animation class based on the specified AnimationType.

        Args:
            animation_type (AnimationType): The type of animation to create.

        Returns:
            Animation: An instance of the Animation class.

        Raises:
            Exception: If the specified AnimationType is unknown.
        """
        if animation_type == AnimationType.WINNING:
            return Animation("src/assets/images/winning-frames")
        if animation_type == AnimationType.LOSE:
            return Animation("src/assets/images/losing-frames")
        raise ValueError("Unknown Animation Type")
