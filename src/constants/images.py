import pygame
from utils.helper import scale_image

GRASS_IMAGE = scale_image(pygame.image.load("src/assets/images/grass.jpg"), 2.5)
TRACK_IMAGE = scale_image(pygame.image.load("src/assets/images/track.png"), 0.9)
FINISH_IMAGE = pygame.image.load("src/assets/images/finish.png")
TRACK_BORDER_IMAGE = scale_image(
    pygame.image.load("src/assets/images/track-border.png"), 0.9
)
RED_CAR_IMAGE = scale_image(pygame.image.load("src/assets/images/red-car.png"), 0.55)
GREEN_CAR_IMAGE = scale_image(
    pygame.image.load("src/assets/images/green-car.png"), 0.55
)
