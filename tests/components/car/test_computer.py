import pygame
import pytest

from src.components.car import ComputerCar


class TestComputerCar:
    @pytest.fixture
    def computer_car(self):
        # Create an instance of ComputerCar for testing
        max_vel = 10
        rotation_vel = 0.1
        path = [(100, 100), (200, 200), (300, 300)]  # Example path
        return ComputerCar(max_vel, rotation_vel, path)

    def test_update_path_point(self, computer_car):
        computer_car.current_point = 0
        computer_car.x = 100
        computer_car.y = 100
        computer_car.img = pygame.Surface((50, 50))  # Example surface size
        computer_car.update_path_point()
        assert computer_car.current_point == 1
