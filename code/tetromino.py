"""Contains all code needed to create and manage a Tetromino object."""


import pygame


class Tetromino:
    """A collection of tiles which make up a single piece on the board."""

    def __init__(self, pos=(5, 0)):
        """Handle all initialization logic for a new Tetromino."""

        # tetromino position
        self.pos = pos
        self.x, self.y = pos

        # misc. tetromino attributes
        self.color = "Red"

        # tetromino movement cooldown variables
        self.can_move = True
        self.move_time = pygame.time.get_ticks()
        self.move_duration = 1000

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
                # print("Tick!")

                self.update_y_pos(self.y + 1)

    def update(self):
        """Run all update logic, including cooldowns and the position on
        the board.
        """

        self.manage_cooldown()
        if not self.can_move:
            self.can_move = True
