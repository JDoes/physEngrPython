print("This program uses a function of time to tell you\n")
print("the position of an object that is experiencing one -\n") 
print("dimensional, constant acceleration. The \n")
print("movement of the object can be in any direction,\n")
print("and the position is the position, in that\n")
print("direction, from whatever is being called zero.\n\n")


a = float(input("Enter the acceleration, in meters/second^2: "))
v = float(input("Enter the initial velocity, in meters/second: "))
x = float(input("Enter the initial position, in meters: "))
t = float(input("Enter the time in seconds, and I'll tell you what the position will be in meters: "))

height = 0.5*a*t**2 + v*t + x

#print("The time of flight is " + str(fFt + fIn) + " feet, " + str(iLeft) + " inches. ")
print("The position from start at") 
print("t = " + str(t) + " seconds is x = " + str(height) + " meters. ")

