#Parallel Plate capacitor

#import math functions
import math

#store values

#Permittivity constant
perm = 8.854187817e-12

#ADDITIONAL FUNCTIONALITY
#Ask user if electric field value is available
#If yes run electric_potential function and assign value to result
#

#Electric Field of a parallel plate capacitor formula (E = eta/Epsilon Naught)

def pp_electric_field():
    #In order to calculate eta we need the charge value and the area.
    charge = float(input('Enter the charge value.\n>>> '))
    area = float(input('Enter your area value.\n>>> '))
    charge_density = charge/area
    E_field = eta/perm
    return E_field

result = pp_electric_field()
print(result)

#delta V = Ed (being the voltage difference between two plates. This equals the electric field times the distance between them.)

def electric_potential():
    dist = float(input('What is the distance or separation between the capacitor plates?\n>>> '))
    change_in_V = result * dist
    return cng_volt

voltage = electric_potential()
print(voltage)
