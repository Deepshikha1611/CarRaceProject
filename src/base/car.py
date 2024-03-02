import math

import pygame

from utils.helper import blit_rotate_center


class AbstractCar:
    def __init__(self, max_vel, rotation_vel) -> None:
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False) -> None:
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win) -> None:
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self) -> None:
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self) -> None:
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()

    def move(self) -> None:
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        return mask.overlap(car_mask, offset)

    def reset(self) -> None:
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0
