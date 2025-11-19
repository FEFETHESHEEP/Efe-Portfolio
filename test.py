import string
import time
text = "HelLo World"
temp = " "
for ch in text:
    for i in string.printable:
        if i == ch or ch:
            time.sleep(0.42)
            print(temp+i)
            temp +=ch
            break
        else:
            time.sleep(0.42)
            print(temp+i)
