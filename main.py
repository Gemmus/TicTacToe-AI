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

rows = 3
columns = 3

square_size = width // columns

line_colour = (82, 82, 75)
line_width = 15

offset = 50

x_colour = (0, 210, 210)
x_width = 20

o_colour = (255, 32, 143)
o_width = 15
radius = square_size // 4

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
        self.empty_slots = self.squares
        self.marked_slots = 0

    def final_state(self):
        # return 0: no one wins; return 1: player1 wins; return 2: player2 wins
        # Horizontal lines #
        for i in range(rows):
            if self.squares[i][0] == self.squares[i][1] == self.squares[i][2] != 0:
                return self.squares[i][0]

        # Vertical lines #
        for j in range(columns):
            if self.squares[0][j] == self.squares[1][j] == self.squares[2][j] != 0:
                return self.squares[0][j]

        # Diagonal lines #
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            return self.squares[1][1]

        return 0  # no winner yet

    def marking_square(self, row, column, player):
        self.squares[row][column] = player
        self.marked_slots += 1

    def empty_square(self, row, column):
        return self.squares[row][column] == 0

    def get_empty_squares(self):
        empty_square_list = []
        for i in range(rows):
            for j in range(columns):
                if self.empty_square(i, j):
                    empty_square_list.append((i, j))
        return empty_square_list

    def checking_full(self):
        return self.marked_slots == 9

    def checking_empty(self):
        return self.marked_slots == 0


class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def random(self, board):
        empty_squares = board.get_empty_squares()
        indexes = random.randrange(0, len(empty_squares))
        return empty_squares[indexes]  # (row, column)

    def eval(self, main_board):
        if self.level == 0:
            #####################
            #   Random Choice   #
            #####################
            move = self.random(main_board)
        else:
            ################################
            #   Minimax Algorithm Choice   #
            ################################
            pass
        return move # row, column


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1 = X, 2 = O
        self.game_mode = 'ai'  # 'pvp' or 'ai'
        self.running = True
        self.show_lines()

    def show_lines(self):
        # Vertical lines
        pygame.draw.line(screen, line_colour, (square_size, 0), (square_size, height), line_width)
        pygame.draw.line(screen, line_colour, (width - square_size, 0), (width - square_size, height), line_width)
        # Horizontal lines
        pygame.draw.line(screen, line_colour, (0, square_size), (width, square_size), line_width)
        pygame.draw.line(screen, line_colour, (0, height - square_size), (width, height - square_size), line_width)

    def draw_figure(self, row, column):
        if self.player == 1:
            #################
            #   Drawing X   #
            #################
            # Descending Part #
            start_descend = (column * square_size + offset, row * square_size + offset)
            end_descend = (column * square_size + square_size - offset, row * square_size + square_size - offset)
            pygame.draw.line(screen, x_colour, start_descend, end_descend, x_width)
            # Ascending Part #
            start_ascend = (column * square_size + offset, row * square_size + square_size - offset)
            end_ascend = (column * square_size + square_size - offset, row * square_size + offset)
            pygame.draw.line(screen, x_colour, start_ascend, end_ascend, x_width)
        elif self.player == 2:
            #################
            #   Drawing O   #
            #################
            center = (column * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(screen, o_colour, center, radius, o_width)

    def next_turn(self):
        self.player = self.player % 2 + 1  # changes player, value between 1 and

                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.#
                            #                                                   #
                            #                   MAIN PROGRAMME                  #
                            #                                                   #
                            # *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*:*.*.*.*.*.*.*.*.*.#


def main():

    game = Game()
    board = game.board
    ai = game.ai

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
                    game.draw_figure(row, column)
                    game.next_turn()
                    print(board.squares)

        if game.game_mode == 'ai' and game.player == ai.player:
            pygame.display.update()

            row, column = ai.eval(board)

            board.marking_square(row, column, game.player)
            print(board.squares)
            game.draw_figure(row, column)
            game.next_turn()
            print(board.squares)

        pygame.display.update()


main()
