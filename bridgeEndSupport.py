#Program to calculate the supporting forces of a bridge, which is being supported by points at its ends, and with only vertical forces present.


input ("Assume the bridge\'s entire weight is concentrated at one point at the middle.\nThis program will ask you to specify the length of the bridge, the weight of the bridge, the amount of additional applied force, and the additional force's distance from the point which you are using as the center of the moment. The prompts will specify which units to enter your numerical values as.\nPress ENTER to continue.")
input ("Dont type in commas, and dont expect place value commas in your outputs, because I\'m a noob, lol.\nPress ENTER to continue")

L = float(input("Enter the length of the bridge, in meters: "))
input ("The weight of the bridge is in the middle, which is located at " + str(L/2) + " m. Press ENTER.")
#Side = input("Which side are you using as the center for the moment?")
# I have to figure out conditional statements, so I can have the program work for either doing the moment about the left or the right-most point.

w = float(input("Enter the weight of the bridge, in Newtons (1 kN = 1000 N): "))

Fa = float(input("Enter the amount of additional force applied to the bridge, in Newtons (1kN = 1000 N): "))
x = float(input("Enter the distance that the additional force is from the left, in meters: "))

#if (Side == "L" or "l" or "Left" or "left"):
Fr = round(((Fa*x + w*(L/2))/L),3)
Fl = round((Fa+w-Fr),3)    
print ("The supporting force on the right is:")
print ("F_R = " + str(Fr) + " Newtons.")
print ("The supporting force on the left is:")
print ("F_L = " + str(Fl) + " Newtons.")

#elif (Side == "R" or "r" or "Right" or "right"):
#Fl = round(((Fa*x + w*(L/2))/L),3)
#Fr = round((Fa + w - Fl),3)
#print ("The supporting force on the left is:")
#print ("F_L = " + str(Fl) + " Newtons.")
#print ("The supporting force on the right is:")
#print ("F_R = " + str(Fr) + " Newtons.")


print 
print ("Have a nice day!")


