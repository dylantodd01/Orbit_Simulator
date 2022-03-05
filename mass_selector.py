import pygame

from settings import Settings

class MassSelector:

	def __init__(self):
		self.settings = Settings()
		self.x_location = self.settings.SCREEN_WIDTH - 50
		self.y_location = self.settings.SCREEN_HEIGHT - 150
		self.SPACING1 = self.settings.LARGE_R + self.settings.MED_R + self.settings.SPACING
		self.SPACING2 = self.SPACING1 + self.settings.MED_R + self.settings.SMALL_R + self.settings.SPACING

		self.selected_mass = 0
		self.selector_circle_parameters = [[(self.x_location, self.y_location), self.settings.LARGE_R + self.settings.SELECTOR_CIRC_W], 
			[(self.x_location, self.y_location + self.SPACING1), self.settings.MED_R + self.settings.SELECTOR_CIRC_W], 
			[(self.x_location, self.y_location + self.SPACING2), self.settings.SMALL_R + self.settings.SELECTOR_CIRC_W]]


	def draw(self, screen):
		pygame.draw.circle(screen, self.settings.BLUE, (self.x_location, self.y_location), self.settings.LARGE_R)
		pygame.draw.circle(screen, self.settings.ORANGE, (self.x_location, self.y_location + self.SPACING1), self.settings.MED_R)
		pygame.draw.circle(screen, self.settings.GREEN, (self.x_location, self.y_location + self.SPACING2), self.settings.SMALL_R)
		pygame.draw.circle(screen, self.settings.WHITE, self.selector_circle_parameters[self.selected_mass][0], 
			self.selector_circle_parameters[self.selected_mass][1], self.settings.SELECTOR_CIRC_W)


	def selector_up(self):
		self.selected_mass = (self.selected_mass - 1) if self.selected_mass > 0 else 2

	def selector_down(self):
		self.selected_mass = (self.selected_mass + 1) % 3

