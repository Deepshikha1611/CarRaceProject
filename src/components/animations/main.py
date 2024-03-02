import os
from enum import Enum
from typing import List

import pygame


class Animation:
    FRAME_RATE = 25

    def __init__(self, src: str) -> None:
        self.frames = self.load_images(src)

    def load_images(self, src: str) -> List[str]:
        gif_frames = []
        for lose_filename in sorted(os.listdir(src)):
            lose_frame = pygame.image.load(
                os.path.join(src, lose_filename)
            ).convert_alpha()
            gif_frames.append(lose_frame)
        return gif_frames

    def draw(self, win: pygame.Surface, clock: pygame.time.Clock) -> None:
        frame_index = 0
        while frame_index <= len(self.frames):
            win.blit(self.frames[frame_index], (75, 250))
            frame_index = (frame_index + 1) % len(self.frames)
            pygame.display.flip()
            clock.tick(self.FRAME_RATE)


class AnimationType(Enum):
    WINNING = 1
    LOSE = 2


class AnimationFactory:
    @staticmethod
    def getCls(type: AnimationType) -> Animation:
        if type == AnimationType.WINNING:
            return Animation("src/assets/images/winning-frames")
        elif type == AnimationType.LOSE:
            return Animation("src/assets/images/losing-frames")
