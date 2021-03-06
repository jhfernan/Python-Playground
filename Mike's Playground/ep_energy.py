#Electric potential energy, the easy way to solve physics problems.
#This energy is converted from potential to kinetic just like in any other situation.
#The calculations based upon Energy in general can be used to design and build anything.
#This application will attempt to quickly formulate Energy quantities and interpret them,
# calculate electric potential or voltage and electric field strength, which is - the derivative of Voltage.

#Quantities that would be nice not to have to type out every time:
#Charge of an electron
ech = -1.6e-19
#Charge of a proton
pch = 1.6e-19
#Mass of an electron
m_elec = 9.11e-31
#Mass of a proton
m_prot = 1.67e-27

#First there are several variable quantities needed.

#import math functions
import math

#Permittivity constant 'epsilon naught using alt 238'
ε = 8.854187817e-12

#Store the value of π for ease of use later 'alt 227' for PC 'option P' for mac
π = math.pi

#Electric constant ¼πε
k = 1/(4*π*ε)

#Define formulas for use
#Usube will be used for the Electric Potential Energy formula
#▲K = -▲Usube 'delta = alt 30'

#Formula for change in potential energy
#****▲U = k*(Qsource * qtest/rf - Qsource * qtest/ri)****

#Later we shall add a function that incorporates the use of this formula while taking inputs from the user.
#We first need a way to determine whether we want to calculate a potential energy
# value alone, that can be used later, rather than a change in potential energy.
