"""Contains all the code needed to create and manage a game tile."""


import pygame

import settings as st


class Tile(pygame.sprite.Sprite):
    """A tile on the game board."""

    def __init__(self, pos, groups=[], surface = pygame.Surface((st.TILESIZE, st.TILESIZE))):

        # initialize parent Sprite class
        super().__init__(groups)

        # set up sprite rect
        self.image = surface

        self.rect = self.image.get_rect(topleft=pos)
