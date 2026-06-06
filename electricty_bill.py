unit=int(input("Please enter the amount of units consumed "))

if(unit<=50):
    amount=unit*5
    tax=34

elif(unit<=100):
    amount=250+((unit-50)*5)
    tax=68

elif(unit<=200):
    amount=1000+((unit-100)*5)
    tax=102
    
else:
    amount=2000
    tax=204

total=amount+tax
print("hence the total is....",total)