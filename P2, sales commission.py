sales=(float(input("Enter Monthly sale ammount: ")))
if sales<=1000:
    commission=0
if sales>=3000:
    commission=2
if sales <=5000:
    commission=5
if sales <=10000:
    commission=7
if sales>10000:
    commission=10
    
print(commission,"%")
