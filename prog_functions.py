"""
Name          : prog_functions.py
Author        : Randi Tinney
Description   : Contains all of the functions needed for the star_bounce program. This is where the
		program checks for events, updates the screen, draws polygons, and checks whether the
		polygons have hit an edge
"""

import sys
import pygame
import random

from polygon import Polygon

def check_events(area, button, polygons, colors):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_add_button(area, button, mouse_x, mouse_y, polygons, colors)

def update_screen(settings, screen, button, area, polygons):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(settings.bg_color)
	
	#Draw button and play area
	button.draw_button()
	screen.blit(area, (settings.play_x, settings.play_y))
	area.fill((0,0,0))
	#Draw polygons
	for polygon in polygons.sprites():
		polygon.update(settings, polygons)
	
	#Make screen visible
	pygame.display.flip()
	
def check_add_button(area, button, mouse_x, mouse_y, polygons, colors):
	"""Start a new game when the player clicks Play"""
	button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
	
	random.seed()
	
	if button_clicked:
		inner_radius = random.randint(0, 40) + 10
		outer_radius = random.randint(0, 40) + 40 + inner_radius
		angle = random.random() * 10
		points = random.randint(5, 11)
		
		c = random.randint(0, 6)
		color = colors[c]
		
		x = random.randint(1, 4)
		y = random.randint(1, 4)
		
		death = random.randint(10, 20)
		
		spin = random.random()
		
		polygon = Polygon(area, color, points, angle, inner_radius, outer_radius, x, y, spin, death)
		polygons.add(polygon)
		
def update_polygons(polygons):
	for polygon in polygons.copy():
		if polygon.check_horizontal_edges():
			polygon.change_x_direction()
			
		if polygon.check_vertical_edges():
			polygon.change_y_direction()