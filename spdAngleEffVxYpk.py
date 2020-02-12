import math

input("Enter the SPEED, the ANGLE, MASS and the EFFICIENCY. This program will tell you the projectile's height above the release point of the launch, and the speed at the peak of its arc. \nAssume gravity is g=9.8m/s^2.\nPRESS ENTER TO CONTINUE")

#assume gravity is 9.8m/s^2, towards Earth's center
g = 9.8

#ask user for launch speed
v = float(input("Enter the launch speed, in meters per second (m/s): "))

#ask for launch angle, which can be entered in degrees
a = float(input("Enter the launch angle, in degrees: "))

#ask for mass
m= float(input("Enter the mass, in kg: "))

#ask for efficiency, but have the user enter whole numbers 
#as percents, like 75 means 75%, instead of 0.75
EFF = float(input("Enter the percent of efficiency.\n\nFor example: 75 means \"75%\" "))
eff = EFF/100

#calculate and store the components of the speed
vx = round((v*math.cos(math.radians(a))),3)
vy = round((v*math.sin(math.radians(a))),3)

#calculate and store the initial kinetic energy, according to the kinetic energy in the 
#vertical and horizontal directions
KEx = round((0.5*m*vx**2),3)
KEy = round((0.5*m*vy**2),3)

#vx will be used for calculating the speed at the peak of the arc, 
#vy will be used to calculate the peak height
vxpk = round((math.sqrt((eff*KEx)/(0.5*m))),3)
ypk = round((eff*KEy/(m*g)),3)
print
#print some intermediate calculation results:
print("At the time of launch, \nthe x-component of the velocity is:\nv_x= " + str(vx) + " m/s.")
print("This gives an initial KEx of:")
print("KE_x = " + str(KEx) + " J.")
print
print("At the time of launch, \nthe y-component of the velocity is:\nv_y= " + str(vy) + " m/s.")
print("This gives an initial KEy of:")
print("KE_y = " + str(KEy) + " J.")
print
#Print results for max height and speed at the peak:
print("The horizontal speed at the peak of the arc is\nv_xpk= " + str(vxpk) + " m/s.")
print("The highest point on the arc is\ny_pk= " +  str(ypk) + " m.")
