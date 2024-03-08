"""
Module: pygame_utils_module

This module provides utility functions for handling Pygame-related operations,
including scaling images, rotating images around their center,
and rendering centered text.

"""

import pygame

pygame.font.init()


def scale_image(img: pygame.Surface, factor: float) -> pygame.Surface:
    """
    Scales a Pygame image by a specified factor.

    Args:
        img (pygame.Surface): The Pygame image to be scaled.
        factor (float): The scaling factor.

    Returns:
        pygame.Surface: The scaled Pygame image.
    """
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    """
    Blits and rotates an image around its center on the specified window.

    Args:
        win: The Pygame window surface.
        image: The Pygame image to be blitted and rotated.
        top_left: The top-left coordinates for blitting.
        angle: The rotation angle.

    Returns:
        None
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    """
    Renders centered text on the specified window using the given font.

    Args:
        win: The Pygame window surface.
        font: The Pygame font to be used for rendering.
        text (str): The text to be rendered.

    Returns:
        None
    """
    render = font.render(text, 1, (200, 200, 200))
    win.blit(
        render,
        (
            win.get_width() / 2 - render.get_width() / 2,
            win.get_height() / 2 - render.get_height() / 2,
        ),
    )
