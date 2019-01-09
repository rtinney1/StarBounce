"""
Name          : star_bounce.py
Author        : Randi Tinney
Description   : Main function for the Star Bounce program. Creates the GUI and contains the main
		program loop that will update the screen. The program ends when the user clicks the
		X on the GUI screen.
"""


import pygame

import prog_functions as pf

from pygame.sprite import Group
from pygame.surface import Surface

from button import Button
from settings import Settings
from play_area import Play_Area

def run_prog():
	"""Main function for prog"""
	#Initialize Screen
	pygame.init()
	
	settings = Settings()
	
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Bouncy")
	
	#Make "Add Star Button"
	add_button = Button(screen, "Add Star")
	
	#Create play area
	play_area = Surface((settings.play_width, settings.play_height))
	
	#Create group of polygons
	polygons = Group()
	
	#ROY G BIV
	colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (127, 0, 255), (255, 0, 255)]
	
	while True:
		pf.check_events(play_area, add_button, polygons, colors)
		
		if len(polygons) > 0:
			pf.update_polygons(polygons)
			
		pf.update_screen(settings, screen, add_button, play_area, polygons)
	
run_prog()