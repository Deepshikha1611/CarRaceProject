from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import sys

import pygame

from utils.helper import blit_text_center

pygame.font.init()
pygame.init()
pygame.mixer.init()

from components.animations import AnimationFactory, AnimationType
from components.car import ComputerCar, PlayerCar
from components.game_info import GameInfo
from constants import COMPUTER_PATH, FINISH_POSITION, GAME_FPS
from constants.images import FINISH_IMAGE, GRASS_IMAGE, TRACK_BORDER_IMAGE, TRACK_IMAGE
from constants.sounds import ACC_SOUND, LOSING_SOUND, WINNING_SOUND

TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER_IMAGE)
FINISH_MASK = pygame.mask.from_surface(FINISH_IMAGE)

WIDTH, HEIGHT = TRACK_IMAGE.get_width(), TRACK_IMAGE.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

MAIN_FONT = pygame.font.SysFont("comicsans", 44)

run = True
clock = pygame.time.Clock()
images = [
    (GRASS_IMAGE, (0, 0)),
    (TRACK_IMAGE, (0, 0)),
    (FINISH_IMAGE, FINISH_POSITION),
    (TRACK_BORDER_IMAGE, (0, 0)),
]
player_car = PlayerCar(4, 4)
computer_car = ComputerCar(2, 4, COMPUTER_PATH)
game_info = GameInfo()


def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = MAIN_FONT.render(f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255)
    )
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(
        f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255)
    )
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if moved:
        ACC_SOUND.play()
        ACC_SOUND.set_volume(0.2)

    if not moved:
        player_car.reduce_speed()


def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
        ACC_SOUND.stop()
        LOSING_SOUND.play()
        AnimationFactory.getCls(AnimationType.LOSE).draw(WIN, clock)
        blit_text_center(WIN, MAIN_FONT, "YOU LOST!")
        LOSING_SOUND.stop()
        pygame.display.update()
        pygame.time.wait(5000)
        draw(WIN, images, player_car, computer_car, game_info)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)


while run:
    clock.tick(GAME_FPS)

    draw(WIN, images, player_car, computer_car, game_info)

    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press Any Key To Start Level {game_info.level}!"
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car, game_info)

    if game_info.game_finished():
        ACC_SOUND.stop()
        WINNING_SOUND.play()
        AnimationFactory.getCls(AnimationType.WINNING).draw(WIN, clock)
        blit_text_center(WIN, MAIN_FONT, "YOU WON THE GAME!")
        WINNING_SOUND.stop()
        pygame.time.wait(5000)
        draw(WIN, images, player_car, computer_car, game_info)
        game_info.reset()
        player_car.reset()
        computer_car.reset()


pygame.quit()

sys.exit()
