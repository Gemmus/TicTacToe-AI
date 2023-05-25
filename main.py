import sys
import pygame
import numpy as np
import random
import copy

                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.#
                            #                                                   #
                            #                     VARIABLES                     #
                            #                                                   #
                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*:*.*.*.*.*.*.*.*.*.#

width = 600
height = 600
background_colour = (247, 243, 234)
x_colour = (255, 32, 143)
o_colour = (0, 210, 210)

rows = 3
columns = 3

square_size = width // columns

line_colour = (82, 82, 75)
line_width = 15

                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.#
                            #                                                   #
                            #               SETTING UP THE GAME                 #
                            #                                                   #
                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*:*.*.*.*.*.*.*.*.*.#

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(background_colour)

                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.#
                            #                                                   #
                            #                      CLASSES                      #
                            #                                                   #
                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*:*.*.*.*.*.*.*.*.*.#


class Board:
    def __init__(self):
        self.squares = np.zeros((rows, columns))
        print(self.squares)

    def marking_square(self, row, column, player):
        self.squares[row][column] = player

    def empty_square(self, row, column):
        return self.squares[row][column] == 0


class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1
        self.show_lines()

    def show_lines(self):
        # Vertical lines
        pygame.draw.line(screen, line_colour, (square_size, 0), (square_size, height), line_width)
        pygame.draw.line(screen, line_colour, (width - square_size, 0), (width - square_size, height), line_width)
        # Horizontal lines
        pygame.draw.line(screen, line_colour, (0, square_size), (width, square_size), line_width)
        pygame.draw.line(screen, line_colour, (0, height - square_size), (width, height - square_size), line_width)

    def next_turn(self):
        self.player = self.player % 2 + 1  # changes player, value between 1 and 2

                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.#
                            #                                                   #
                            #                   MAIN PROGRAMME                  #
                            #                                                   #
                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*:*.*.*.*.*.*.*.*.*.#


def main():

    game = Game()
    board = game.board

    #################
    #   Main Loop   #
    #################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // square_size
                column = pos[0] // square_size
                print(row, column)

                if board.empty_square(row, column):
                    board.marking_square(row, column, game.player)
                    print(board.squares)
                    game.next_turn()
                    print(board.squares)

        pygame.display.update()


main()
