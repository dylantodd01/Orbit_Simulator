import pygame


class Settings:

	def __init__(self):

		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 800

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (115, 147, 255)
		self.YELLOW = (253, 184, 19)
		self.BG_COLOUR = self.BLACK

		self.ICON = pygame.image.load('images/icon.png')
		self.FONT_SIZE = 30

		self.FPS = 600

		self.INITIAL_X_VEL = 5
		self.INITIAL_Y_VEL = 0
		self.RUNGE_KUTTA_DT = 0.2

		#self.AU = 1.495978707 * 10e11
		self.STATIONARY_MASS = 1e4
		self.MOVING_MASS = 1
		self.STATIONARY_RAD = 20
		self.MOVING_RAD = 5
		self.GRAV_CONST = 1

		self.TRAIL_SPACING = 15
		self.TRAIL_LENGTH = 100


