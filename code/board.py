"""Contains all code needed to create and manage a Tetris board."""


import pygame

import settings as st


class GameBoard:
    """A tetris board."""

    def __init__(self):
        """Handle initialization logic for a new Tetris board."""
        
        self.board = self.generate_board()

    def generate_board(self):
        """Create a new Tetris board."""

        board = []
        for row_num in range(20):
            row = []
            for column_num in range(10):
                row.append((column_num, row_num))
            board.append(row)

        return board
