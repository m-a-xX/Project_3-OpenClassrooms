import pygame
import random
from pygame.locals import *

from constants import *
from maze import *

"""Manage the items"""
class Items:

	got_i1 = 0
	got_i2 = 0
	got_i3 = 0
	
	def __init__(self, image):
		self.image = image

	@staticmethod
	def checkItems(position_item1, position_item2, position_item3, position_macgyver):
		y, x = position_macgyver
		x = x * 40
		y = y * 40
		mg_pixpos = (x, y)
		if mg_pixpos == position_item1:
			Items.got_i1 = 1
		if mg_pixpos == position_item2:
			Items.got_i2 = 1
		if mg_pixpos == position_item3:
			Items.got_i3 = 1
		if Items.got_i1 == 0:
			window.blit(item_1, (position_item1))
		else:
			window.blit(black_sprite, (position_item1))
		if Items.got_i2 == 0:
			window.blit(item_2, (position_item2))
		else:
			window.blit(black_sprite, (position_item2))
		if Items.got_i3 == 0:
			window.blit(item_3, (position_item3))
		else:
			window.blit(black_sprite, (position_item3))
		pygame.display.flip()
		
	@staticmethod
	def randomPosition(struct):
		x = random.randint(0, 14)
		y = random.randint(0, 14)
		while int(Maze.struct[y][x]) != 1:
			x = random.randint(0, 14)
			y = random.randint(0, 14)
		Maze.struct[y][x] = 3
		x *= len_sprites
		y *= len_sprites
		return(x, y)