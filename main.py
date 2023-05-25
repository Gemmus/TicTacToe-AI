import sys
import pygame
import random
import numpy as np
import copy

#################
#   Variables   #
#################

WIDTH = 600
HEIGHT = 600

# Colours:
BACKGROUND_COLOUR = (247, 243, 234)


###########################
#   Setting up the Game   #
###########################

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BACKGROUND_COLOUR)


######################
#   Main Programme   #
######################

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()
