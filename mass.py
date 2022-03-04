import pygame
import numpy as np
import math

from settings import Settings

class Mass:

	def __init__(self, colour, location, mass, radius):
		self.mass = mass
		self.radius = radius
		self.colour = colour
		self.location = location

		self.settings = Settings()

	def update_location(self, new_location):
		self.location = new_location

	def draw(self, screen):
		pygame.draw.circle(screen, self.colour, self.location, self.radius)


class MovingMass(Mass):

	def __init__(self, colour, location, mass, radius):
		Mass.__init__(self, colour, location, mass, radius)

		self.z_vec = np.array([float(location[0]), float(self.settings.INITIAL_X_VEL), 
			float(location[1]), float(self.settings.INITIAL_Y_VEL)]) # Vector of form [x, x', y, y']
		self.gravitational_constant = self.settings.GRAV_CONST
		self.dt = self.settings.RUNGE_KUTTA_DT
		self.trail = []
		self.trail_iterations = 0


	def draw(self, screen):
		pygame.draw.circle(screen, self.colour, self.location, self.radius)

	def draw_trail(self, screen):
		for location in self.trail:
			pygame.draw.circle(screen, self.settings.BLUE, location, 2)

	def move(self, sun):
		self.runge_kutta_step(self.z_vec, sun)
		self.update_location((self.z_vec[0], self.z_vec[2]))
		self.update_trail()

	def state_deriv(self, z, sun):
		r_x = (sun.location[0] - z[0])
		r_y = (sun.location[1] - z[2])
		if r_x == 0:
			r_x = 0.01

		sign_x = 1 if r_x > 0 else -1
		sign_y = 1 if r_y > 0 else -1
		theta = math.atan(r_y / r_x)
	
		R_sqrd = (r_x ** 2) + (r_y ** 2)
		if R_sqrd < 20:
			R_sqrd = 20

		force = self.gravitational_constant * ((self.mass * sun.mass) / R_sqrd)
		force_x = force * abs(math.cos(theta)) * sign_x
		force_y = force * abs(math.sin(theta)) * sign_y

		z1 = z[1]
		z2 = force_x / self.mass
		z3 = z[3]
		z4 = force_y / self.mass

		return np.array([z1, z2, z3, z4])

	def runge_kutta_step(self, z, sun):
		A = self.dt * self.state_deriv(z, sun)
		B = self.dt * self.state_deriv(z + A/2, sun)
		C = self.dt * self.state_deriv(z + B/2, sun)
		D = self.dt * self.state_deriv(z + C, sun)

		self.z_vec += (1 / 6) * (A + 2 * B + 2 * C + D)

	def update_trail(self):
		if (self.trail_iterations % self.settings.TRAIL_SPACING) != 0:
			self.trail_iterations += 1
			return
		
		if len(self.trail) < self.settings.TRAIL_LENGTH:
			self.trail.append((self.z_vec[0], self.z_vec[2]))
		else:
			self.trail.pop(0)
			self.trail.append((self.z_vec[0], self.z_vec[2]))

		self.trail_iterations += 1






