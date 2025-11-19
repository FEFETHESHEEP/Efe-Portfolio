#asks the user for a currency type
currency_type=input("what currency type would you like to convert?(USD, EUR, JPY, INR, AUD): ")

#ask user for input
ammount=input("enter the ammount of GBP you would like to convert: ")

#translates the inputed ammount into chosen currency
if currency_type=="USD":
    final==ammount//1.20
if currency_type=="EUR":
    final=ammount//1.15
if currency_type=="JPY":
    final=ammount//180
if currency_type=="INR":
    final=ammount//100
if currency_type=="AUD":
    final=ammount//1.9
#prints final ammount
print("the ammount in",currency_type,"is: ", final)

