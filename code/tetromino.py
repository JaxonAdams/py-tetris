"""Contains all code needed to create and manage a Tetromino object."""


import pygame

import settings as st


class Tetromino:
    """A collection of tiles which make up a single piece on the board."""

    def __init__(self, first_pos, second_pos, third_pos, fourth_pos):
        """Handle all initialization logic for a new Tetromino."""

        # tetromino tile positions
        self.positions = [first_pos, second_pos, third_pos, fourth_pos]

        # misc. tetromino attributes
        self.color = "purple"

        # tetromino movement cooldown variables
        self.can_move = True
        self.move_time = pygame.time.get_ticks()
        self.move_duration = 800

        self.has_reached_bottom = False

    def update_y_pos(self, index, y_pos):
        """Update the current y-positions or rows on the board."""

        self.positions[index] = (self.positions[index][0], y_pos)

    def manage_cooldown(self):
        """Manage the current movement cooldown."""

        current_time = pygame.time.get_ticks()

        if self.can_move:
            if (current_time - self.move_time
                >= self.move_duration):
                self.can_move = False
                self.move_time = pygame.time.get_ticks()

                for i in range(4):
                    self.update_y_pos(i, self.positions[i][1] + 1)

    def manage_movable(self):
        """Manage whether or not this tetromino can be moved."""

        for _, y_pos in self.positions:
            if y_pos == st.NUM_ROWS - 1:
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
