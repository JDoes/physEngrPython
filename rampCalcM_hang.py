#Gordon Bates
#Started on 02/11/2020
#Given ramp angle and car mass, calculate hanging mass

import math

m_c = float(input("Enter the mass of the car, in grams: "))
theta = float(input("Enter the ramp angle, in degrees: "))

m_h = round((m_c*math.sin(math.radians(theta))),3)

print("To hold a " +str(m_c) + " gram car still")
print("on a " + str(theta) + " degree hill, you")
print("need " + str(m_h) + " grams of hanging mass.")
