import math

a = float(input("Enter the acceleration, in m/s^2: "))

v = float(input("Enter the initial velocity, in m/s: "))

x = float(input("Enter the starting position, in meters: "))

t = float(input("Enter the time, in seconds: "))

vF = a*t+v

xF = 0.5*a*t**2+v*t+x

if(vF < 0):
    vD = "negative"
else:
    vD = "positive"

print("If your starting position is " + str(x) + " meters, ")

print("with a starting velocity of " + str(v) + "m/s,")

print("and you accelerate at a rate of " +str(a) + "m/s^2,")

print("for " + str(t) + " seconds, your final velocity")

print("will be " + str(vF) + "m/s, and your final ")

print("position will be " +str(xF)+ " meters.")

print(" ")

print("If your velocity is " + str(vF) + "m/s, that means your")

print("speed is " + str(math.fabs(vF)) + "m/s, and the direction is " + str(vD) + ".")

