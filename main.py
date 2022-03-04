import sys
import pygame
import time

from settings import Settings
from mass import Mass
from mass import MovingMass
from display_text import Text

class GravitySimulator:

	def __init__(self):
		# Initialise pygame
		pygame.init()

		# Initialise the pygame settings
		self.settings = Settings()

		# Set up window
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
		pygame.display.set_caption("Gravity Simulator")
		pygame.display.set_icon(self.settings.ICON)

		# Set up text instructions
		self.instructions = Text(fontsize=self.settings.FONT_SIZE, position=(20, self.settings.SCREEN_HEIGHT - 30),
			message="Click anywhere to add a mass. Press space to clear the masses", colour=self.settings.WHITE)

		# Create the sun
		self.sun = Mass(mass=self.settings.STATIONARY_MASS, radius=self.settings.STATIONARY_RAD, colour=self.settings.YELLOW, 
			location=(self.settings.SCREEN_WIDTH // 2, self.settings.SCREEN_HEIGHT // 2))
		
		# Create an empty list to contain the masses
		self.masses = []
		

	def run(self):
		""" Main loop """
		while True:
			self.check_events()

			for mass in self.masses:
				mass.move(self.sun)

			self.update_screen()
			time.sleep(1/self.settings.FPS)


	def check_events(self):
		""" Check for user input events """
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self.masses.append(MovingMass(mass=self.settings.MOVING_MASS, 
					radius=self.settings.MOVING_RAD, colour=self.settings.WHITE, location=mouse_pos))

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.clear_masses()


	def update_screen(self):
		""" Update the screen """
		self.screen.fill(self.settings.BG_COLOUR)
		self.instructions.draw(self.screen)

		self.sun.draw(self.screen)
		for mass in self.masses:
			mass.draw(self.screen)
			mass.draw_trail(self.screen)

		pygame.display.update()


	def clear_masses(self):
		self.masses = []


simulation = GravitySimulator()
simulation.run()



