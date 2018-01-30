# Point Charge Calculations:
#   The Calculator for the Electric Field produced by a Point Charge

#Access math functions
import math

#The beginning of the equation starts with 1/4pi this relates to a circle
circ = 1 / (math.pi * 4)

#The permittivity constant, termed 'Epsilon Naught'
perm = 8.854187817e-12

#Function needs two arguments, one for the radius from the point,
# and one for the charge value. All other values are unchanging.
def point_charge():
    crg = float(input('Please enter your charge density value. '))
    rad = float(input('Please enter your radius from charge at appropriate point in electric field. '))
    return((circ / perm) * (crg / rad ** 2))

point_charge()
