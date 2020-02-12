import math

c = input("This program works assuming an initial launch height of zero meters.\n     It will accept the values of the launch angle,\nand the launch speed. It will output the \nx and y components of the launch velocity, as well as\nthe max height and the horizontal range.\n\nPRESS ENTER OR CLICK OKAY TO CONTINUE")
spd = float(input("Enter the launch speed, in m/s."))
angle = float(input("Enter the launch angle, in degrees."))




theta = angle*math.pi/180
vx = round(spd*math.cos(theta),3)
vy = round(spd*math.sin(theta),3)
tpk = round(vy/9.8,3)
t = tpk*2
xmax = round(vx*t,3)
ymax = round((4.9*tpk**2),3)

print("The x component of the velocity at launch is "+str(vx)+" m/s.")
print("The y component of the velocity at launch is "+str(vy)+" m/s.")
print("The time to the peak is "+str(tpk)+" seconds.")
print("The time of flight is "+str(t)+" seconds.")
print("The horizontal range is "+str(xmax)+" meters.")
print("The maximum height is "+str(ymax)+" meters.")

