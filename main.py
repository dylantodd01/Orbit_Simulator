import sys
import pygame
import time

from settings import Settings
from mass import Mass
from mass import MovingMass
from display_text import Text
from mass_selector import MassSelector

class GravitySimulator:

	def __init__(self):
		# Initialise pygame
		pygame.init()

		# Initialise the pygame settings
		self.settings = Settings()

		# Initialise the mass selector class
		self.mass_selector = MassSelector()

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

		# Create a list containing the mass options
		self.mass_options = [(self.settings.LARGE_R * self.settings.MASS_SCALING, self.settings.BLUE), 
			(self.settings.MED_R * self.settings.MASS_SCALING, self.settings.ORANGE), 
			(self.settings.SMALL_R * self.settings.MASS_SCALING, self.settings.GREEN)]
		

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
					radius=self.mass_options[self.mass_selector.selected_mass][0], 
					colour=self.mass_options[self.mass_selector.selected_mass][1], location=mouse_pos))

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.clear_masses()

				if event.key == pygame.K_UP:
					self.mass_selector.selector_up()

				if event.key == pygame.K_DOWN:
					self.mass_selector.selector_down()


	def update_screen(self):
		""" Update the screen """
		self.screen.fill(self.settings.BG_COLOUR)
		self.instructions.draw(self.screen)

		self.sun.draw(self.screen)
		self.mass_selector.draw(self.screen)
		for mass in self.masses:
			mass.draw(self.screen)
			mass.draw_trail(self.screen)

		pygame.display.update()


	def clear_masses(self):
		self.masses = []


simulation = GravitySimulator()
simulation.run()



