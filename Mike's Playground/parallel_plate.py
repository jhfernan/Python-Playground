#Parallel Plate capacitor

#import math functions
import math

#store values

#Permittivity constant
permittivity = 8.854187817e-12

#ADDITIONAL FUNCTIONALITY
#Ask user if electric field value is available
#If yes run electric_potential function and assign value to result
#

#Electric Field of a parallel plate capacitor formula (E = eta/Epsilon Naught)

def get_float_value(value_type):
	value = None
	while not value:
		try:
			value = float(input('Enter the {} value.\n>>> '.format(value_type)))
		except ValueError:
			print('Please enter a valid decimal number.')
	return value

def pp_electric_field():
	#In order to calculate eta we need the charge value and the area.
	charge = get_float_value('charge')
	area = get_float_value('area')
	charge_density = charge/area
	electric_field = charge_density/permittivity
	return electric_field

result = pp_electric_field()
print(result)

#delta V = Ed (being the voltage difference between two plates. This equals the electric field times the distance between them.)

def electric_potential():
	distance = float(input('What is the distance or separation between the capacitor plates?\n>>> '))
	change_in_voltage = result * distance
	return change_in_voltage

voltage = electric_potential()
print(voltage)
