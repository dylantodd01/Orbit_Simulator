import pygame

class Text:

	def __init__(self, fontsize, position, message, colour):
		self.font = pygame.font.SysFont("bahnschrift", fontsize)
		self.message = self.font.render(message, True, colour)
		self.message_rect = self.message.get_rect(midleft=position)

	def draw(self, screen):
		screen.blit(self.message, self.message_rect)

