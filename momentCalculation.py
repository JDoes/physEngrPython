#A program to calculate moment, based on force, lever
#arm length, and the direction of rotation.

input ("This is a progam that will calculate moment, based force, distance, and direction. Press enter to continue.")

F = float( input ("Enter the force, in Newtons: "))

x = float(input ("Enter the lever arm distance, in meters: "))

dir = str(input("Enter the direction (cw or ccw): ")) 

if dir == "cw":
    d = -1
if dir == "ccw":
    d = 1

if d == -1:
    D = "clockwise (-)"
if d == 1:
    D = "counter-clockwise (+)"

print ("For a force of " + str(F) + " N, and a")
print ("lever arm distance of " + str(x) + " m,")
print ("in the " + D + " direction, the ")
print ("MOMENT = " + str(d*F*x) + " N/m.")
print ("Have a nice day!")

