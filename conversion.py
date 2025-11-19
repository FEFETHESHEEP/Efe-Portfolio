POUND_TO_DOLLAR = 1.40
POUND_TO_EURO = 1.14
POUND_TO_REAL = 4.77
POUND_TO_YEN = 203.80
POUND_TO_LIRA = 55.76

ammount = str(input("enter the ammount you'd like to convert: £"))


def validate_range(ammount):
    while ammount < 0 or ammount > 2500:
        print("Not in range, please re-enter ammount.")
        ammount = str(input("enter the ammount you'd like to convert between 0 and 2500: £"))
    return ammount

discount = input("do you work with us?(Yes/No): ")
if discount == "Yes":
    discount = 0.95
else:
    discount = 1
def currency():
    currency = input("would you like to convert to USD, EUR, BRL, JPY, or TRY: ")

def ConversionRate():

    print("would you like to convert to USD, EUR, BRL, JPY, or TRY: ")
    if currency == "USD":
        ConversionRate = POUND_TO_DOLLAR
    elif currency == "EUR":
        ConversionRate = POUND_TO_EURO
    elif currency == "BRL":
        ConversionRate == POUND_TO_REAL
    elif currency == "JPY":
        ConversionRate == POUND_TO_YEN
    elif currency == "TRY":
        ConversionRate == POUND_TO_LIRA
    else:
        print("Invalid currency entered, please re-enter.")
        currency = input("would you like to convert to USD, EUR, BRL, JPY, or TRY: ")

def transactionFee():
    if ammount <= 300:
        transactionFee = 0.35
    elif ammount > 300:
        translactionFee = 0.3
    elif ammount > 750:
        transactionFee = 0.25
    elif ammount > 1000:
        transactionFee = 0.2
    elif ammount > 2000:
        transactionFee = 0.1

    finalAmmount = ammount * ConversionRate*Discount*transactionFee

print("------Summary------")
print("ammount to be converted:", ammount)
print("Conversion Rate:", ConversionRate)
print("discount?:", discount)
print("Currency: £", currency)
print("Transaction Fee :£", transactionFee)
print("final ammount: £", finalAmmount)
print("-----------------")


