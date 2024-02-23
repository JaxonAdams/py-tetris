"""Contains all code needed to create and manage a Tetris board."""


import pygame

import settings as st
from tile import Tile
from tetromino import Tetromino


class GameBoard:
    """A tetris board."""

    def __init__(self):
        """Handle initialization logic for a new Tetris board."""

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # create sprite group
        self.tile_sprites = pygame.sprite.Group()

        # new tetromino logic
        self.can_create_tetromino = True
        self.active_tetromino = None
        
        # set up game board
        self.board = self.generate_board()

    def generate_board(self):
        """Create a new Tetris board."""

        board = []
        for row_num in range(st.NUM_ROWS):
            row = []
            for column_num in range(st.NUM_COLUMS):
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
                if self.active_tetromino is not None and (col_i, row_i) in self.active_tetromino.positions:                 
                    tetromino_surf = pygame.Surface((st.TILESIZE, st.TILESIZE))
                    tetromino_surf.fill(self.active_tetromino.color)

                    Tile((x, y) + border_offset, [self.tile_sprites], tetromino_surf)
                else:
                    Tile((x, y) + border_offset, [self.tile_sprites])

    def run(self):
        """Update and draw the board."""

        self.create_board_sprites()

        if self.can_create_tetromino:
            self.active_tetromino = Tetromino((4, 1), (5, 1), (6, 1), (5, 0))
            self.can_create_tetromino = False

        self.active_tetromino.update()

        self.tile_sprites.draw(self.display_surface)
        self.tile_sprites.update()
