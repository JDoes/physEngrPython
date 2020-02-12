#Program to let you select what you want calculated, and then
#the program asks fro the stuff that is needed to calculate it.

num = str(input("EFF = Eout/Ein * 100%\nWhat part of the efficiency equation are you trying to solve for? Type \"out\" \"in\", or \"eff\""))

if (num=="in"):
    input ("To calculate the ENERGY IN, provide the EFFICIENCY and the and the ENERGY OUT.\nPRESS ENTER") 
    Eout = float(input("Enter the energy you want to get out, in Joules: "))
    Eff = float(input("Enter the efficiency, in percent form percent."))
    Ein = Eout/(Eff/100)
    print ("In order to get " + str(Eout) + " J out,")
    print ("with an efficiency of " + str(Eff) + "%,")
    print ("the amount of energy you will") 
    print ("need to put in is:")
    print (str(Ein) + " Joules.")

if (num=="out"):
    input ("To calculate the ENERGY OUT, provide the EFFICIENCY and the ENERGY IN.\nPRESS ENTER") 
    Ein = float(input("Enter the energy that goes in, in Joules: "))
    Eff = float(input("Enter the efficiency, in percent form."))
    Eout = Ein*(Eff/100)
    print ("If you put " + str(Ein) + " J in,")
    print ("with an efficiency of " + str(Eff) + "%,")
    print ("the amount of energy you will") 
    print ("be able to get out will be:")
    print (str(Eout) + " Joules.")

if (num=="eff"):
    input ("To calculate the EFFICIENCY, provide the ENERGY OUT and the ENERGY IN.\nPRESS ENTER") 
    Ein = float(input("Enter the energy that goes in, in Joules: "))
    Eout = float(input("Enter the energy out, in Joules."))
    Eff = ((Eout/Ein)*100)
    print ("If you put " + str(Ein) + " J in,")
    print ("and you get out " + str(Eout) + " J,")
    print ("The efficiency is " + str(Eff) + "%.")

print
print ("Have a good day!")

