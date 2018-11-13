"""Constants and images used in the game, and principals parameters"""

import pygame
from pygame.locals import *

NB_SPRITES = 15
LEN_SPR = 40
SIDE_WINDOW = NB_SPRITES * LEN_SPR

pygame.display.init()
pygame.display.set_mode()
TITLE = pygame.image.load("pictures/title.png").convert()
MACGYVER_O = pygame.image.load("pictures/MacGyver.png").convert()
MACGYVER = pygame.transform.smoothscale(MACGYVER_O, (LEN_SPR, LEN_SPR))
GUARDIAN_O = pygame.image.load("pictures/Gardien.png").convert()
GUARDIAN = pygame.transform.smoothscale(GUARDIAN_O, (LEN_SPR, LEN_SPR))
WALL_O = pygame.image.load("pictures/wall.png").convert()
WALL = pygame.transform.smoothscale(WALL_O, (LEN_SPR, LEN_SPR))
BACKGROUND = pygame.image.load("pictures/background.png").convert()
BLACK_SPRITE = pygame.transform.smoothscale(BACKGROUND, (LEN_SPR, LEN_SPR))
ITEM_1_O = pygame.image.load("pictures/aiguille.png").convert_alpha()
ITEM_1 = pygame.transform.smoothscale(ITEM_1_O, (LEN_SPR, LEN_SPR))
ITEM_2_O = pygame.image.load("pictures/ether.png").convert_alpha()
ITEM_2 = pygame.transform.smoothscale(ITEM_2_O, (LEN_SPR, LEN_SPR))
ITEM_3_O = pygame.image.load("pictures/tube_plastique.png").convert_alpha()
ITEM_3 = pygame.transform.smoothscale(ITEM_3_O, (LEN_SPR, LEN_SPR))
YOUWIN = pygame.image.load("pictures/youwin.png").convert()
YOULOST = pygame.image.load("pictures/youlost.png").convert()

WINDOW = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
