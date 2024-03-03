import os
import pygame
from enum import Enum

class Animation:
    FRAME_RATE = 25
    
    def __init__(self,src) -> None:
        self.frames = self.load_images(src)
        

    def load_images(self,src) -> None:
        gif_frames = []
        for lose_filename in sorted(os.listdir(src)):
            lose_frame = pygame.image.load(os.path.join(src, lose_filename)).convert_alpha()
            gif_frames.append(lose_frame)
        return gif_frames
    
    def draw(self,WIN,clock):
        frame_index = 0
        counter=0
        while(frame_index<=len(self.frames) and counter==0):
            if frame_index==len(self.frames)-1:
                counter+=1
            print(counter)
            print(frame_index)
            print(len(self.frames))
            # Blit the current frame onto the screen
            WIN.blit(self.frames[frame_index], (75, 250))
            
            # Update the frame index for the next frame
            frame_index = (frame_index + 1) % len(self.frames)
            
            # Update the display
            pygame.display.flip()
            
            # Cap the frame rate
            clock.tick(self.FRAME_RATE)

class AnimationType(Enum):
    WINNING = 1
    LOSE = 2


class AnimationFactory:
    @staticmethod
    def getCls(type:AnimationType) -> Animation:
        if type == AnimationType.WINNING:
            return Animation("src/assets/images/winning-frames")
        elif type == AnimationType.LOSE:
            return Animation("src/assets/images/losing-frames")

