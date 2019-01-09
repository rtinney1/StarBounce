"""
Name          : polygon.py
Author        : Randi Tinney
Description   : Creates a polygon and adds it to the play area. Each polygon is given an inner and 
		outer radius to determin the size, and random x and y speed, a random color, random number
		of points, a float for a spin value, and a random deathtime. The polygons will bounce around 
		the screen until they die, upon which they will vanish.
"""

import pygame
import math
import random

from pygame.sprite import Sprite
from datetime import datetime, timedelta

class Polygon(Sprite):
	"""A class to represent a single polygon"""
	
	def __init__(self, area, color, points, angle, inner_radius, outer_radius, x_speed, y_speed, spin, deathtime):
		"""Initialize the polygon and set its starting position"""
		super().__init__()
		self.area = area
		self.area_rect = area.get_rect()
		self.color = color
		self.points = points
		self.angle = angle
		self.inner_radius = inner_radius
		self.outer_radius = outer_radius
		self.deathtime = deathtime
		
		self.spin = spin
		
		self.birth = datetime.now()
		
		self.x_speed = x_speed
		self.y_speed = y_speed
		
		self.xPos = self.area_rect.left + self.outer_radius + 10 + self.x_speed
		self.yPos = self.area_rect.top + self.outer_radius + 10 + self.y_speed
		
		r = random.randint(0, 1)
		
		if r == 0:
			self.down_move = -1
		else:
			self.down_move = 1
			
		r = random.randint(0, 1)
		
		if r == 0:
			self.left_move = -1
		else:
			self.left_move = 1
		
		self.get_vertices()
		
	def blitme(self):
		"""Draw the polygon at its current location"""
		self.area.blit(self.image, self.rect)
		
	def get_vertices(self):
		self.vertices = []
		a = self.angle
		
		for num in range(self.points):
			x = self.xPos + math.cos(a) * self.inner_radius
			y = self.yPos + math.sin(a) * self.inner_radius
			self.vertices.append((x, y))
			
			a = a + math.pi/self.points
			x = self.xPos + math.cos(a) * self.outer_radius
			y = self.yPos + math.sin(a) * self.outer_radius
			self.vertices.append((x, y))
			
			a = a + math.pi/self.points
		
	def update(self, settings, polygons):
		self.xPos += self.left_move * self.x_speed		
		self.yPos += self.down_move * self.y_speed
		self.angle += self.spin
		
		alive = datetime.now()
		
		length = alive - self.birth
		
		if length > timedelta(seconds=self.deathtime):
			polygons.remove(self)
		
		self.get_vertices()
		self.draw_polygon()
		
	def draw_polygon(self):
		pygame.draw.polygon(self.area, self.color, self.vertices, 0)
		#pygame.draw.rect(self.area, self.color, self.rect)
		
	def check_horizontal_edges(self):
		"""Return True if polygon is at left or right edges of screen"""
		if self.xPos >= self.area_rect.right - self.outer_radius:
			return True
		elif self.xPos <= self.outer_radius:
			return True
			
	def check_vertical_edges(self):
		"""Return True if polygon is at top or bottom edges of screen"""
		if self.yPos >= self.area_rect.bottom - self.outer_radius:
			return True
		elif self.yPos <= self.outer_radius:
			return True
			
	def change_x_direction(self):
		self.left_move *= -1
		
	def change_y_direction(self):
		self.down_move *= -1