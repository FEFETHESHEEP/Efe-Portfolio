#ask user for input
ammount=int(input("enter the ammount you would like to convert: "))
USD=ammount * 1.20
EUR=ammount * 1.15
JPY=ammount * 180
INR=ammount * 100
AUD=ammount * 1.9

print("input in $",USD)
print("input in €",EUR)
print("input in ¥",JPY)
print("input in ₹",INR)
print("input in A$",AUD)
