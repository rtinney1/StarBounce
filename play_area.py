"""
Name          : play_area.py
Author        : Randi Tinney
Description   : Creates the play area that will contain the polygons created
"""

import pygame.font
from pygame.surface import Surface

class Play_Area(Surface):
	def __init__(self, settings, screen):
		"""Initialize play area"""
		super().__init__((settings.play_width, settings.play_height))
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.settings = settings
		
		#Set color of play area
		self.bg_color = self.settings.play_bg_color
				
		#Build the button's rect object and place in the top center
		self.rect = pygame.Rect(0, 0, self.settings.play_width, self.settings.play_height)
		self.rect.center = self.screen_rect.center
		self.rect.top = self.screen_rect.top + 75
		
	def draw_area(self):
		#Draw the area
		self.screen.fill(self.bg_color, self.rect)