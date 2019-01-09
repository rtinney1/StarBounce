"""
Name          : settings.py
Author        : Randi Tinney
Description   : General settings for the program that includes the size and colors of the screens
"""

class Settings():
	"""Settings to be referred to throughout the program"""
	
	def __init__(self):
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		
		#Play area settings
		
		self.play_width = 1100
		self.play_height = 700
		self.play_x = 50
		self.play_y = 75
		self.play_bg_color = (0, 0, 0)