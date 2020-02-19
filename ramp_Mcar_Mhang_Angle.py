#Gordon Bates
#Started on 02/12/2020
#This program assumes no friction anywhere, a cable that is parallel to the ramp.
#This program will calculate any of various quantities for a car on an inclined ramp,
#held in place by a hanging mass over a pulley.

import math

solve = input("Which variable do you want to solve for: m_car, m_hang, or angle? ")

#Given an angle and a car's mass, calculate hanging mass
if solve.lower() == "m_hang":
    theta = float(input("Enter the ramp angle, in degrees: "))
    m_car = float(input("Enter the mass of the car, in grams: "))

    m_hang = round((m_car*math.sin(math.radians(theta))),3)

    print("On a " + str(theta) + " degree incline, a")
    print(str(m_car) + " gram car requires " + str(m_hang) + " grams" )
    print("of hanging mass to hold it in place.") 

#Given an angle and hanging mass, calculate car mass
elif solve.lower() == "m_car":
    theta = float(input("Enter the angle, in degrees: "))
    m_hang = float(input("Enter the mass of the hanger, in grams: "))

    m_car = round((m_hang/math.sin(math.radians(theta))),3)

    print("On a " + str(theta) + " degree ramp, with a ")
    print(str(m_hang) + "gram hanger, the mass of car that")  
    print("it can hold still is " + str(m_car) + " grams.")

#Given hanging mass and car mass, calculate the angle
elif solve.lower() == "angle":
    m_car = float(input("Enter the mass of the car, in grams: "))
    m_hang = float(input("Enter the mass of the hanger, in grams: "))

    theta = round((math.degrees(math.asin(m_hang/m_car))),3)

    print("For a car with a mass of " + str(m_car) + " grams,")
    print("being held by a " + str(m_hang) + " gram hanging mass,")
    print("the ramp angle needs to be " + str(theta) + " degrees.")






