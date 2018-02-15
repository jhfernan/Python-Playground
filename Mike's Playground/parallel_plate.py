#Parallel Plate capacitor

#import math functions
import math

#store values

#Perfmittivity constant
perm = 8.854187817e-12

#Electric Field of a parallel plate capacitor formula (E = eta/Epsilon Naught)

def pp_electric_field():
    crg = float(input('Enter the charge value.\n>>> '))
    area = float(input('Enter your area value.\n>>> '))
    eta = crg/area
    E_field = eta/perm
    return E_field

result = pp_electric_field()
print(result)

#delta V = Ed (being the voltage difference between two plates. This equals the electric field times the distance between them.)
