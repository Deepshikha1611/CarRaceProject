"""
Module: image_module

This module defines an ImageEnum enumeration and an ImageFactory class for managing
and loading image assets in the RacingGame application.

"""

from enum import Enum

import pygame

from utils.helper import scale_image


class ImageEnum(Enum):
    """
    Enumeration representing different types of images used in the game.

    Values:
        GRASS_IMAGE: Image for grass.
        TRACK_IMAGE: Image for the track.
        FINISH_IMAGE: Image for the finish line.
        TRACK_BORDER_IMAGE: Image for the track border.
        RED_CAR_IMAGE: Image for the red car.
        GREEN_CAR_IMAGE: Image for the green car.
    """

    GRASS_IMAGE = "src/assets/images/grass.jpg"
    TRACK_IMAGE = "src/assets/images/track.png"
    FINISH_IMAGE = "src/assets/images/finish.png"
    TRACK_BORDER_IMAGE = "src/assets/images/track-border.png"
    RED_CAR_IMAGE = "src/assets/images/red-car.png"
    GREEN_CAR_IMAGE = "src/assets/images/green-car.png"


class ImageFactory:
    """
    Factory class for loading and obtaining scaled image objects based on the specified
    ImageEnum type.

    Methods:
        get_image_scale(image_type: ImageEnum):
            Returns the scale factor for a specific image type.

        get_image(image_type: ImageEnum):
            Obtains a scaled image object based on the specified ImageEnum type.

    """

    @staticmethod
    def get_image_scale(image_type: ImageEnum):
        """
        Returns the scale factor for a specific image type.

        Args:
            image_type (ImageEnum): The type of image for which to obtain the scale factor.

        Returns:
            float: The scale factor.
        """
        if image_type in [
            ImageEnum.GRASS_IMAGE,
            ImageEnum.TRACK_IMAGE,
            ImageEnum.TRACK_BORDER_IMAGE,
        ]:
            return 0.8
        if image_type is ImageEnum.FINISH_IMAGE:
            return 1

        return 0.55

    @staticmethod
    def get_image(image_type: ImageEnum):
        """
        Obtains a scaled image object based on the specified ImageEnum type.

        Args:
            image_type (ImageEnum): The type of image to obtain.

        Returns:
            pygame.Surface: The obtained scaled image object.
        """
        scale = ImageFactory.get_image_scale(image_type)
        return scale_image(pygame.image.load(image_type.value), scale)
