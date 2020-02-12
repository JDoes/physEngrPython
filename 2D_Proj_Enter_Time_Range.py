import math

c = input("Given the time of flight and the horizontal range, \nthis program will calculate the max height, and the \nspeed at launch. \nWe can write another program later, which \nwill also be able to tell you the angle of \nlaunch, the vertical and the horizontal components \nof the velocity at the time of launch. \nAre you ready to go? \n\nPress ENTER to continue.")

t = float(input("Enter the time of flight, in seconds: "))
r = float(input("Enter the horizontal range, in meters: "))

vx = round((1.0*r/t),3)
tpk = round(t/2,3)
vyi = round(9.8*tpk,2)
ymax = round((0.5*9.8*tpk**2),3)
spd = round(math.sqrt(vx**2 + vyi**2),3)
theta = round(math.degrees(math.atan(vyi/vx)),3)

print("The speed at launch is "+str(spd)+" m/s,")
print("with a launch angle of "+str(theta)+" degrees.")
print("The peak height is reached at "+str(tpk)+" seconds,")
print("and the peak height is "+str(ymax)+" meters.")



