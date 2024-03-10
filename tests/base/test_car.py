import math

import pytest

from src.base.car import AbstractCar


class TestAbstractCar:
    @pytest.fixture
    def abstract_car(self):
        # Create an instance of AbstractCar for testing
        max_vel = 10
        rotation_vel = 0.1
        AbstractCar.START_POS = (100, 100)
        return AbstractCar(max_vel, rotation_vel)

    def test_move(self, abstract_car):
        abstract_car.angle = 45
        abstract_car.vel = 1
        abstract_car.move()
        expected_y = abstract_car.y - math.cos(math.radians(abstract_car.angle))
        expected_x = abstract_car.x - math.sin(math.radians(abstract_car.angle))
        assert abstract_car.y == pytest.approx(expected_y, 1)
        assert abstract_car.x == pytest.approx(math.ceil(expected_x), 1)

    def test_reset(self, abstract_car):
        abstract_car.angle = 45
        abstract_car.vel = 5
        abstract_car.reset()

        assert abstract_car.x == AbstractCar.START_POS[0]
        assert abstract_car.y == AbstractCar.START_POS[1]
        assert abstract_car.angle == 0
        assert abstract_car.vel == 0
