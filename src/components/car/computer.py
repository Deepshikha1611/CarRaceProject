"""
Module: computer_car_module

This module defines the ComputerCar class, a derived class from the AbstractCar class,
representing a computer-controlled car
with additional functionality for following a predefined path.

"""

import math

import pygame

from base.car import AbstractCar
from constants.images import ImageEnum, ImageFactory


class ComputerCar(AbstractCar):
    """
    Represents a computer-controlled car with the ability to follow a predefined path.

    Attributes:
        IMG: A class variable representing the image of the computer-controlled car.
        START_POS: A class variable representing the starting position of the
        computer-controlled car.

    Methods:
        __init__(self, max_vel, rotation_vel, path=[]):
            Initializes a ComputerCar object with the specified maximum velocity,
            rotation velocity, and path.

        draw_points(self, win: pygame.Surface) -> None:
            Draws points on the given window representing the path.

        calculate_angle(self) -> None:
            Calculates the angle to the next point on the path and
            adjusts the car's angle accordingly.

        update_path_point(self) -> None:
            Updates the current path point if the car has reached the target.

        move(self) -> None:
            Updates the car's position by following the predefined path.

        next_level(self, level: int) -> None:
            Resets the car's position and updates its velocity for the next level.

        reset(self) -> None:
            Resets the car's position and path to the starting configuration.

    """

    IMG = ImageFactory.get_image(ImageEnum.GREEN_CAR_IMAGE)
    START_POS = (660, 300)

    def __init__(self, max_vel, rotation_vel, path=[]):
        """
        Initializes a ComputerCar object with the specified maximum velocity,
        rotation velocity, and path.

        Args:
            max_vel: The maximum velocity of the computer-controlled car.
            rotation_vel: The rotation velocity of the computer-controlled car.
            path (list): A list of tuples representing the path points for the
            computer-controlled car to follow.

        Returns:
            None
        """
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win: pygame.Surface) -> None:
        """
        Draws points on the given window representing the path.

        Args:
            win (pygame.Surface): The window surface on which the points should be drawn.

        Returns:
            None
        """
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def calculate_angle(self) -> None:
        """
        Calculates the angle to the next point on the path and
        adjusts the car's angle accordingly.

        Returns:
            None
        """
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self) -> None:
        """
        Updates the current path point if the car has reached the target.

        Returns:
            None
        """
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self) -> None:
        """
        Updates the car's position by following the predefined path.

        Returns:
            None
        """
        if self.current_point >= len(self.path):
            return
        self.calculate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level: int) -> None:
        """
        Resets the car's position and updates its velocity for the next level.

        Args:
            level: The current level of the game.

        Returns:
            None
        """
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0

    def reset(self) -> None:
        """
        Resets the car's position and path to the starting configuration.

        Returns:
            None
        """
        self.current_point = 0
        super().reset()
