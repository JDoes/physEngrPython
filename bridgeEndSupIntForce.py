import math

#Give summary/description of program and assumptions
input ("Assume all trusses are made of equillateral triangles, and that the bridge\'s entire weight is concentrated at one point at the middle.\nThis program will ask you to specify the length of the bridge, the weight of the bridge, the amount of additional applied force, and the additional force's distance from the point which you are using as the center of the moment. The prompts will specify which units to enter your numerical values as.\nPress ENTER to continue.")
input ("Dont type in commas, and dont expect place value commas in your outputs, because I\'m a noob, lol.\nPress ENTER to continue")


#Start asking for input and specifying dimensions and quantities 
#about the loaded bridge
L = float(input("Enter the length of the bridge, in meters: "))

w = float(input("Enter the weight of the bridge, in Newtons (1 kN = 1000 N): "))
input ("The weight of the bridge is in the middle, which is located at " + str(L/2) + " m. Press ENTER.")

Fa = float(input("Enter the amount of additional force applied to the bridge, in Newtons (1kN = 1000 N): "))
x = float(input("Enter the distance that the additional force is from the left, in meters: "))


#Calculate the supporting forces, and round to three decimal places
Fr = round(((Fa*x + w*(L/2))/L),3)
Fl = round((Fa+w-Fr),3)  

#Right side diagonal (Frd) and horizontal (Frh)
Frd = round((Fr/math.sin(math.radians(60))),3)
Frh = round((Frd*math.cos(math.radians(60))),3)

#Left side diagonal (Fld) and horizontal (Flh)
Fld = round((Fl/math.sin(math.radians(60))),3)
Flh = round((Fld*math.cos(math.radians(60))),3)


#Now add the calculation of the forces INSIDE of the truss members, 
#for the members touching where the supporting force is located.

#Right side first: print out Frd and Frh
print ("The supporting force on the right is:")
print ("F_R = " + str(Fr) + " Newtons.")
print ("The right side's diagonal truss member has")
print (str(Frd) + " Newtons of compression, and ")
print ("the horizontal truss member has ")
print (str(Frh) + " Newtons of tension.")
print       
#Then the left side: print out Fld and Flh
print ("The supporting force on the left is:")
print ("F_L = " + str(Fl) + " Newtons.")
print ("The left side's diagonal truss member has")
print (str(Fld) + " Newtons of compression, and ")
print ("the horizontal truss member has ")
print (str(Flh) + " Newtons of tension.")
print 
print ("Have a nice day!")


