import math


class Electric:
	circ = 1 / (math.pi * 4)
	perm = 8.854187817e-12

	def point_charge(self):
		crg = float(input('Please enter your charge value\n>>> '))
		rad = float(input('Please enter your radius from charge at appropriate point in electric field\n>>> '))
		value = ((self.circ / self.perm) * (crg / rad ** 2))
		return value
