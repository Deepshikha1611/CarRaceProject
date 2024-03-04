import pygame

from src.utils.helper import scale_image

IMAGE_SCALE = 0.8
CAR_SCALE = 0.55

GRASS_IMAGE = scale_image(pygame.image.load("src/assets/images/grass.jpg"), IMAGE_SCALE)
TRACK_IMAGE = scale_image(pygame.image.load("src/assets/images/track.png"), IMAGE_SCALE)
FINISH_IMAGE = pygame.image.load("src/assets/images/finish.png")
TRACK_BORDER_IMAGE = scale_image(
    pygame.image.load("src/assets/images/track-border.png"), IMAGE_SCALE
)
RED_CAR_IMAGE = scale_image(
    pygame.image.load("src/assets/images/red-car.png"), CAR_SCALE
)
GREEN_CAR_IMAGE = scale_image(
    pygame.image.load("src/assets/images/green-car.png"), CAR_SCALE
)
