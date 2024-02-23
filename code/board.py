"""Contains all code needed to create and manage a Tetris board."""


import pygame

import settings as st
from tile import Tile


class GameBoard:
    """A tetris board."""

    def __init__(self):
        """Handle initialization logic for a new Tetris board."""

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # create sprite group
        self.tile_sprites = pygame.sprite.Group()

        # custom clock / cooldown setup
        self.can_move = True
        self.move_time = pygame.time.get_ticks()
        self.move_duration = 1000
        
        # set up game board
        self.board = self.generate_board()
        self.create_board_sprites()

    def generate_board(self):
        """Create a new Tetris board."""

        board = []
        for row_num in range(20):
            row = []
            for column_num in range(10):
                row.append((column_num, row_num))
            board.append(row)

        return board
    
    def create_board_sprites(self):
        """Using self.board, create the sprites on the board."""

        for row_i, row in enumerate(self.board):
            for col_i, _ in enumerate(row):
                x = col_i * st.TILESIZE
                y = row_i * st.TILESIZE

                border_offset = pygame.math.Vector2(st.BORDERSIZE, st.BORDERSIZE)

                border_surface = pygame.Surface((st.TILESIZE, st.TILESIZE) + (border_offset * 2))
                border_surface.fill("Silver")

                # border
                Tile((x, y), [self.tile_sprites], border_surface)
                # tile
                Tile((x, y) + border_offset, [self.tile_sprites])

    def manage_tetromino_update_cooldown(self):
        """Manage the active tetromino's update cooldown."""

        current_time = pygame.time.get_ticks()

        if self.can_move:
            if (current_time - self.move_time
                >= self.move_duration):
                self.can_move = False
                self.move_time = pygame.time.get_ticks()
                print("Tick!")

    def run(self):
        """Update and draw the board."""

        self.manage_tetromino_update_cooldown()
        if not self.can_move:
            self.can_move = True

        self.tile_sprites.draw(self.display_surface)
        self.tile_sprites.update()
