import pygame
from pygame.locals import *

"""Window parameters"""
nb_sprites = 15
len_spr = 40
side_window = nb_sprites * len_spr

"""Used pictures"""
pygame.display.init()
pygame.display.set_mode()
title = pygame.image.load("pictures/title.png").convert()
macgyver_o = pygame.image.load("pictures/MacGyver.png").convert()
macgyver = pygame.transform.smoothscale(macgyver_o, (len_spr, len_spr))
guardian_o = pygame.image.load("pictures/Gardien.png").convert()
guardian = pygame.transform.smoothscale(guardian_o, (len_spr, len_spr))
wall_o = pygame.image.load("pictures/wall.png").convert()
wall = pygame.transform.smoothscale(wall_o, (len_spr, len_spr))
background = pygame.image.load("pictures/background.png").convert()
black_sprite = pygame.transform.smoothscale(background, (len_spr, len_spr))
item_1_o = pygame.image.load("pictures/aiguille.png").convert_alpha()
item_1 = pygame.transform.smoothscale(item_1_o, (len_spr, len_spr))
item_2_o = pygame.image.load("pictures/ether.png").convert_alpha()
item_2 = pygame.transform.smoothscale(item_2_o, (len_spr, len_spr))
item_3_o = pygame.image.load("pictures/tube_plastique.png").convert_alpha()
item_3 = pygame.transform.smoothscale(item_3_o, (len_spr, len_spr))
youwin = pygame.image.load("pictures/youwin.png").convert()
youlost = pygame.image.load("pictures/youlost.png").convert()

"""Window"""
window = pygame.display.set_mode((side_window, side_window))