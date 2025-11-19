#Read parcel weight
weight = float(input("Enter the weight of the parcel (in kg): "))

#Determine charge based on weight
if weight <= 1:
    charge = 3.99
elif weight <= 5:
    charge = 6.99
elif weight <= 10:
    charge = 9.99
elif weight <= 20:
    charge = 15.99
else:
    charge = 25.00

#Print the result
print("The delivery charge is: £", charge)
