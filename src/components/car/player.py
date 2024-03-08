"""
Module: player_car_module

This module defines the PlayerCar class, a derived class from the AbstractCar class,
representing a player-controlled car
with additional functionality for reducing speed and bouncing.
"""

from base.car import AbstractCar
from constants.images import ImageEnum, ImageFactory


class PlayerCar(AbstractCar):
    """
    Represents a player-controlled car with the ability to reduce speed and bounce.

    Attributes:
        IMG: A class variable representing the image of the player-controlled car.
        START_POS: A class variable representing the starting position of the player-controlled car.

    Methods:
        reduce_speed(self) -> None:
            Reduces the speed of the player-controlled car and updates its position.

        bounce(self) -> None:
            Causes the player-controlled car to bounce by reversing its velocity.

    """

    IMG = ImageFactory.get_image(ImageEnum.RED_CAR_IMAGE)
    START_POS = (630, 300)

    def __init__(self, vel, position):
        super().__init__(vel, position)
        self.vel = 0

    def reduce_speed(self) -> None:
        """
        Reduces the speed of the player-controlled car and updates its position.

        Returns:
            None
        """
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self) -> None:
        """
        Causes the player-controlled car to bounce by reversing its velocity.

        Returns:
            None
        """
        self.vel = -(self.vel / 2)
        self.move()
