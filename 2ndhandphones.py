price=(float(input("Enter price of new phone: ")))
cond=input("condition of phone(excellent,good,ok,poor): ")
if cond=="poor":
    resale=0.2
elif cond=="ok":
    resale=0.4
elif cond=="good":
    resale=0.55
elif cond=="excellent":
    resale=0.7
    
print(resale,"%")


final=price * (1-resale)
print(final)
