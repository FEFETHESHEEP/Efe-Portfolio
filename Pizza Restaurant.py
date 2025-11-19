SMALL_COST = 3.25
MEDIUM_COST = 5.50
LARGE_COST = 7.15

EXTRA_TOPPING1 = 0.75
EXTRA_TOPPING2 = 1.35
EXTRA_TOPPING3 = 2.00
EXTRA_TOPPING4_OR_MORE = 2.50

DISCOUNT_RATE = 0.1
DELIVERY_CHARGE = 2.50

name = input("Enter name: ")
address = input("Enter address: ")
phoneNumber = input("Enter phone number: ")

def validate_quantity_range(qty):
    while qty < 1 or qty > 6:
        print("Not in range, please re-enter number of pizzas.")
        qty = int(input("Enter number of pizzas from 1-6: "))
    return qty

quantity = int(input("Enter number of pizzas from 1-6: "))
quantity = validate_quantity_range(quantity)

totalCost = 0

for i in range(1, quantity + 1):
    print("Pizza", i, ":")
    size = input("Enter size (Small/Medium/Large): ").capitalize()
    numToppings = int(input("Enter number of toppings: "))

    if size == "Small":
        baseCost = SMALL_COST
    elif size == "Medium":
        baseCost = MEDIUM_COST
    elif size == "Large":
        baseCost = LARGE_COST
    else:
        print("Invalid size entered, the default (Medium) has been chosen.")
        baseCost = MEDIUM_COST

    if numToppings == 1:
        toppingCost = EXTRA_TOPPING1
    elif numToppings == 2:
        toppingCost = EXTRA_TOPPING2
    elif numToppings == 3:
        toppingCost = EXTRA_TOPPING3
    elif numToppings >= 4:
        toppingCost = EXTRA_TOPPING4_OR_MORE
    else:
        toppingCost = 0

    pizzaCost = baseCost + toppingCost
    totalCost += pizzaCost

discount = 0
if quantity >= 3:
    discount = totalCost * DISCOUNT_RATE

deliveryCost = 0
delivery = input("Delivery required (Yes/No): ").capitalize()
if delivery == "Yes":
    deliveryCost = DELIVERY_CHARGE
 
finalcost = totalCost - discount + deliveryCost

print("---Order Summary---")
print("Name:", name)
print("Address:", address)
print("Phone number:", phoneNumber)
print("Subtotal: £", round(totalCost, 2))
print("Discount: £", round(discount, 2))
print("Delivery Charge :£", round(deliveryCost, 2))
print("Total: £", round(finalcost, 2))
print("-----------------")
