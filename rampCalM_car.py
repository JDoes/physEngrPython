#Gordon Bates
#Started on 02/11/2020
#Given ramp angle and hanging mass, calculate car mass

import math

m_h = float(input("Enter the mass of the hanger, in grams: "))
theta = float(input("Enter the ramp angle, in degrees: "))

m_c = round((m_h/math.sin(math.radians(theta))),3)


print("On a " + str(theta) + " degree hill,")
print("if you have " + str(m_h) + " grams of hanging mass,")
print("you can hold a " +str(m_c) + " gram car still")


