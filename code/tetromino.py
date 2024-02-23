"""Contains all code needed to create and manage a Tetromino object."""


import pygame

import settings as st


class Tetromino:
    """A collection of tiles which make up a single piece on the board."""

    def __init__(self, pos=(4, 0)):
        """Handle all initialization logic for a new Tetromino."""

        # tetromino position
        self.pos = pos
        self.x, self.y = pos

        # misc. tetromino attributes
        self.color = "Red"

        # tetromino movement cooldown variables
        self.can_move = True
        self.move_time = pygame.time.get_ticks()
        self.move_duration = 800

        self.has_reached_bottom = False

    def update_y_pos(self, y_pos):
        """Update the current y-position or row on the board."""

        self.y = y_pos
        self.pos = (self.x, self.y)

    def manage_cooldown(self):
        """Manage the current movement cooldown."""

        current_time = pygame.time.get_ticks()

        if self.can_move:
            if (current_time - self.move_time
                >= self.move_duration):
                self.can_move = False
                self.move_time = pygame.time.get_ticks()

                self.update_y_pos(self.y + 1)

    def manage_movable(self):
        """Manage whether or not this tetromino can be moved."""

        if self.y == st.NUM_ROWS - 1:
            self.has_reached_bottom = True
        
        if not self.can_move:
            self.can_move = True

    def update(self):
        """Run all update logic, including cooldowns and the position on
        the board.
        """

        if not self.has_reached_bottom:
            self.manage_movable()
            self.manage_cooldown()
