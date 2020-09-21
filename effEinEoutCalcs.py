#Program to let you select what you want calculated, and then
#the program asks fro the stuff that is needed to calculate it.

num = str(input("EFF = (Eout/Ein) * 100%\n\nWhat part of the efficiency equation are you trying\nto solve for? Type \"out\" \"in\", or \"eff\" "))

if (num=="in"):
    print("")
    input ("To calculate the ENERGY IN, provide the EFFICIENCY\nand the ENERGY OUT.\nPRESS ENTER ") 
    print("")
    Eout = float(input("Enter the energy you want to get out, in Joules: \nEout= "))
    Eff = float(input("Enter the efficiency, in percent form: \nEff= "))
    Ein = Eout/(Eff/100)
    print("")
    print ("In order to get " + str(Eout) + " J out,")
    print ("with an efficiency of " + str(Eff) + "%,")
    print ("the amount of energy you will") 
    print ("need to put in is:")
    print (str(Ein) + " Joules.")

if (num=="out"):
    print("")
    input ("To calculate the ENERGY OUT, provide the EFFICIENCY\nand the ENERGY IN.\nPRESS ENTER") 
    print("")
    Ein = float(input("Enter the energy that goes in, in Joules:\nEin= "))
    Eff = float(input("Enter the efficiency, in percent form.\n%EFF= "))
    Eout = Ein*(Eff/100)
    print("")
    print ("If you put " + str(Ein) + " J in,")
    print ("with an efficiency of " + str(Eff) + "%,")
    print ("the amount of energy you will") 
    print ("be able to get out will be:")
    print (str(Eout) + " Joules.")

if (num=="eff"):
    print("")
    input ("To calculate the EFFICIENCY, provide the ENERGY OUT\nand the ENERGY IN.\nPRESS ENTER") 
    print("")
    Ein = float(input("Enter the energy that goes in, in Joules:\nEin= "))
    Eout = float(input("Enter the energy out, in Joules.\nEout= "))
    Eff = ((Eout/Ein)*100)
    print ("If you put " + str(Ein) + " Joules in,")
    print ("and you get out " + str(Eout) + " Joules,")
    print ("The efficiency is " + str(Eff) + "%.")

print (" ")
print ("Have a good day!") 
