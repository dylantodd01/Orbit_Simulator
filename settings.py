import pygame


class Settings:

	def __init__(self):

		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1400, 1000

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (61, 183, 228)
		self.YELLOW = (253, 184, 19)
		self.ORANGE = (255, 136, 73)
		self.GREEN = (105, 190, 40)

		self.BG_COLOUR = self.BLACK

		self.ICON = pygame.image.load('images/icon.png')
		self.FONT_SIZE = 30

		self.FPS = 1000

		self.INITIAL_X_VEL = 5
		self.INITIAL_Y_VEL = 0
		self.RUNGE_KUTTA_DT = 0.2

		self.STATIONARY_MASS = 1e4
		self.STATIONARY_RAD = 20
		self.MOVING_MASS = 1
		self.GRAV_CONST = 1

		self.TRAIL_SPACING = 15
		self.TRAIL_LENGTH = 100
		self.TRAIL_COLOUR = self.WHITE

		# Mass selector
		self.LARGE_R = 25
		self.MED_R = 20
		self.SMALL_R = 15
		self.SPACING = 20
		self.SELECTOR_CIRC_W = 4
		self.MASS_SCALING = 0.4



