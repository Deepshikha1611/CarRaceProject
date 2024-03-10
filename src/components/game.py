"""
Module: racing_game_module

This module defines the RacingGame class,
representing the main game logic for the Racing Game application.

"""

import pygame

from components.animations import AnimationFactory, AnimationType
from components.car import ComputerCar, PlayerCar
from components.game_info import GameInfo
from constants.game import COMPUTER_PATH, FINISH_POSITION, GAME_FPS
from constants.images import ImageEnum, ImageFactory
from constants.sounds import SoundEnum, SoundFactory
from utils.helper import blit_text_center


class RacingGame:
    """
    Represents the main game class responsible for managing the game state and logic.

    Methods:
        __init__(self):
            Initializes a RacingGame object.

        draw(self):
            Draws the game elements on the window.

        move_player(self):
            Handles player input and moves the player car accordingly.

        handle_result(self, sound, animation_type, message):
            Handles the result of the game, playing sounds,
            displaying animations, and showing a message.

        lose(self):
            Handles the player losing the game.

        win(self):
            Handles the player winning the game.

        handle_collision(self):
            Handles collisions between cars and game elements.

        run_game(self):
            Runs the main game loop.

    """

    def __init__(self):
        """
        Initializes a RacingGame object.
        """
        self.init_pygame()

        pygame.display.set_caption("Racing Game!")

        self.main_font = pygame.font.SysFont("comicsans", 44)

        self.run = True
        self.clock = pygame.time.Clock()

        self.player_car = PlayerCar(4, 4)
        self.computer_car = ComputerCar(2, 4, COMPUTER_PATH)
        self.game_info = GameInfo()
        self.init_images()
        self.init_sounds()

    def init_pygame(self):
        """
        Initializes the pygame.
        """
        pygame.font.init()
        pygame.init()
        pygame.mixer.init()

    def init_images(self):
        """
        Initializes the images objects.
        """
        track_image = ImageFactory.get_image(ImageEnum.TRACK_IMAGE)
        self.width = track_image.get_width()
        self.height = track_image.get_height()

        self.window = pygame.display.set_mode(
            (track_image.get_width(), track_image.get_height())
        )
        self.images = [
            (ImageFactory.get_image(ImageEnum.GRASS_IMAGE), (0, 0)),
            (track_image, (0, 0)),
            (ImageFactory.get_image(ImageEnum.FINISH_IMAGE), FINISH_POSITION),
            (ImageFactory.get_image(ImageEnum.TRACK_BORDER_IMAGE), (0, 0)),
        ]

    def init_sounds(self):
        """
        Initializes the sounds.
        """
        self.acceration_sound = SoundFactory.get_sound(SoundEnum.ACCELERATION_SOUND)
        self.losing_sound = SoundFactory.get_sound(SoundEnum.LOSING_SOUND)
        self.winning_sound = SoundFactory.get_sound(SoundEnum.WINNING_SOUND)

    def draw(self):
        """
        Draws the game elements on the window.
        """
        for img, pos in self.images:
            self.window.blit(img, pos)

        text_color, text_antialias = (255, 255, 255), 1

        level_text = self.main_font.render(
            f"Level {self.game_info.level}", text_antialias, text_color
        )
        self.window.blit(level_text, (10, self.height - level_text.get_height() - 70))

        time_text = self.main_font.render(
            f"Time: {self.game_info.get_level_time()}s", text_antialias, text_color
        )
        self.window.blit(time_text, (10, self.height - time_text.get_height() - 40))

        vel_text = self.main_font.render(
            f"Vel: {round(self.player_car.vel, 1)}px/s", text_antialias, text_color
        )
        self.window.blit(vel_text, (10, self.height - vel_text.get_height() - 10))

        self.player_car.draw(self.window)
        self.computer_car.draw(self.window)

        pygame.display.update()

    def move_player(self):
        """
        Handles player input and moves the player car accordingly.
        """
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            self.player_car.rotate(left=True)
        if keys[pygame.K_d]:
            self.player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.player_car.move_backward()

        if moved:
            self.acceration_sound.set_volume(0.2)
            # self.acceration_sound.play()

        if not moved:
            self.player_car.reduce_speed()

    def handle_result(self, sound, animation_type, message):
        """
        Handles the result of the game, playing sounds,
        displaying animations, and showing a message.

        Args:
            sound (pygame.mixer.Sound): The sound to be played.
            animation_type (AnimationType): The type of animation to be displayed.
            message (str): The message to be shown.
        """
        self.acceration_sound.stop()
        sound.play()
        AnimationFactory.get_animation(animation_type).draw(self.window, self.clock)
        blit_text_center(self.window, self.main_font, message)
        sound.stop()
        pygame.display.update()
        pygame.time.wait(5000)

        self.game_info.reset()
        self.player_car.reset()
        self.computer_car.reset()
        self.draw()

    def lose(self):
        """
        Handles the player losing the game.
        """
        self.handle_result(self.losing_sound, AnimationType.LOSE, "YOU LOST!")

    def win(self):
        """
        Handles the player winning the game.
        """
        self.handle_result(
            self.winning_sound, AnimationType.WINNING, "YOU WON THE GAME!"
        )

    def handle_collision(self):
        """
        Handles collisions between cars and game elements.
        """
        if (
            self.player_car.collide(pygame.mask.from_surface(self.images[3][0]))
            is not None
        ):
            self.player_car.bounce()

        computer_finish_poi_collide = self.computer_car.collide(
            pygame.mask.from_surface(self.images[2][0]), *FINISH_POSITION
        )
        if computer_finish_poi_collide is not None:
            self.lose()

        player_finish_poi_collide = self.player_car.collide(
            pygame.mask.from_surface(self.images[2][0]), *FINISH_POSITION
        )
        if player_finish_poi_collide is not None:
            if player_finish_poi_collide[1] == 0:
                self.player_car.bounce()
            else:
                self.acceration_sound.stop()
                self.game_info.next_level()
                self.player_car.reset()
                self.computer_car.next_level(self.game_info.level)

    def run_game(self):
        """
        Runs the main game loop.
        """
        while self.run:
            self.clock.tick(GAME_FPS)
            self.draw()

            while not self.game_info.started:
                blit_text_center(
                    self.window,
                    self.main_font,
                    f"Press Any Key To Start Level {self.game_info.level}!",
                )
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    if event.type == pygame.KEYDOWN:
                        self.game_info.start_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break

            self.move_player()
            self.computer_car.move()

            self.handle_collision()

            if self.game_info.game_finished():
                self.win()

        pygame.quit()
