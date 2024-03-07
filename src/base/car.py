# pylint: disable=too-many-instance-attributes


"""
This module defines the AbstractCar class, which serves
as a base class for representing an abstract car in a 2D game
environment. The AbstractCar class provides methods for
rotation, movement, drawing, collision detection, and
resetting the car's position.

"""

import math

import pygame

from utils.helper import blit_rotate_center


class AbstractCar:
    """
    A base class representing an abstract car.

    Attributes:
        IMG: A class variable representing the image of the car.
        START_POS: A class variable representing the starting position of the car.
        img: An instance variable representing the current image of the car.
        max_vel: An instance variable representing the maximum velocity of the car.
        vel: An instance variable representing the current velocity of the car.
        rotation_vel: An instance variable representing the rotation velocity of the car.
        angle: An instance variable representing the current angle of the car.
        x: An instance variable representing the x-coordinate of the car.
        y: An instance variable representing the y-coordinate of the car.
        acceleration: An instance variable representing the acceleration of the car.
    """

    IMG = None
    START_POS = None

    def __init__(self, max_vel, rotation_vel) -> None:
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False) -> None:
        """
        Rotates the car either left or right based on the specified parameters.

        Args:
            left (bool): If True, rotates the car to the left.
            right (bool): If True, rotates the car to the right.

        Returns:
            None
        """
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win) -> None:
        """
        Draws the car on the given window with the current image and rotation angle.

        Args:
            win: The window on which the car should be drawn.

        Returns:
            None
        """
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self) -> None:
        """
        Moves the car forward by increasing its velocity and updating its position.

        Returns:
            None
        """
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self) -> None:
        """
        Moves the car backward by decreasing its velocity and updating its position.

        Returns:
            None
        """
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self) -> None:
        """
        Updates the position of the car based on its current velocity and angle.

        Returns:
            None
        """
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        """
        Checks for collision between the car and a mask at the specified offset.

        Args:
            mask: The mask representing the object with which collision is checked.
            x (int): The x-coordinate offset for the collision check.
            y (int): The y-coordinate offset for the collision check.

        Returns:
            A mask representing the overlapping region if a collision occurs, otherwise None.
        """
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        return mask.overlap(car_mask, offset)

    def reset(self) -> None:
        """
        Resets the car's position and angle to the starting position.

        Returns:
            None
        """
        self.x, self.y = self.START_POS
        self.angle = 0
