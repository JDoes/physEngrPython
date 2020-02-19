#Gordon Bates
#Started on 02/11/2020
#This program will calculate various values of a crane.
#Round to three decimal places.
#This program assumes the boom is attached to the tower with a hinge, and the
#mast is a solid part of the tower.

import math

m_load = float(input("How many grams of mass were on the load side of your crane? "))
m_bal = float(input("How many grams of mass were on the balance side of your crane? "))
m_total = m_load+m_bal
F_total = round((m_total*0.0098),3)
F_pounds = round((F_total*0.224809),3)

h = float(input("Enter the height of your mast, in cm. "))
x_load = float(input("How many cm is the load side of your boom? "))
x_bal = float(input("How many cm is the balance side of your boom? "))
theta_load = round((math.degrees(math.atan(h/x_load))),3)
theta_bal = round((math.degrees(math.atan(h/x_bal))),3)

F_load = m_load*0.0098
F_bal = m_bal*0.0098

T_load = round((F_load/math.sin(math.radians(theta_load))),3)
C_load = round((T_load*math.cos(math.radians(theta_load))),3)

T_bal = round((F_bal/math.sin(math.radians(theta_bal))),3)
C_bal = round((T_bal*math.cos(math.radians(theta_bal))),3)

print("The total weight supported by the crane was: " + str(F_total) + " Newtons.")
print("In pounds, that is " + str(F_pounds) + " Lbs")
print

print("The load side's angle is " + str(theta_load) + " degrees.")
print("The tension in the cable on the load side is " + str(T_load) + " Newtons.")
print("The compression in the boom on the load side is " + str(C_load) + " Newtons.")
print

print("The balance side's angle is " + str(theta_bal) + " degrees.")
print("The tension in the cable on the balance side is " + str(T_bal) + " Newtons.")
print("The compression in the boom on the balance side is " + str(C_bal) + " Newtons.")


