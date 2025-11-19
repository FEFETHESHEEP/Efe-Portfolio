spent=(float(input("Enter ammount spent:£")))
if spent<=50:
    discount=0
elif spent<=100:
    discount=2
elif spent<=5000:
    discount=5
elif spent<=10000:
    discount=7
if spent>10000:
    discount=10
    
print(discount,
      "%")
