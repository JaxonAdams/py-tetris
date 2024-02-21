"""Creates a new Game instance and runs the game to completion."""


import sys

import pygame

import settings as st
from board import GameBoard


class Game:
    """Defines how to build an instance of a PyTetris game."""

    def __init__(self):
        """Set up a new Game instance with all necessary attributes."""

        # general setup
        pygame.init()

        # set up display window
        self.screen = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
        pygame.display.set_caption("PyTetris")

        # set up clock for steady fps
        self.clock = pygame.time.Clock()

        # set up game board
        self.game_board = GameBoard()

    def run(self):
        """Run the game. Set up a game loop and an event listener."""
        
        # event loop
        while True:
            # get events
            for event in pygame.event.get():
                # if player quit, stop the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            # fill in screen
            self.screen.fill("STEELBLUE")
            # run board logic
            self.game_board.run()
            # update screen
            pygame.display.update()
            # update clock
            self.clock.tick(st.FPS)


# !---------------------------------------------------------------------------
if __name__ == "__main__":

    game = Game()
    game.run()
