import pygame
from pygame.locals import *

from constants import *

"""Manage the items"""
class Items:

	def __init__(self, image):
		self.image = image

	@staticmethod
	def checkItems(position_item1, position_item2, position_item3, position_macgyver):
		if position_macgyver == position_item1:
			items_count += 1
		if position_macgyver == position_item2:
			items_count += 1
		if position_macgyver == position_item3:
			items_count += 1
		return items_count

	@staticmethod
	def randomPosition(struct): #Liste contenant la structure en parametre
		x = 0
		y = 0
		while struct[x][y] != 1:
			x = random.randint(0, 14)
			y = random.randint(0, 14)
		struct[x][y] = 3
		x = x * len_sprites
		y = y * len_sprites
		return 	(x, y)