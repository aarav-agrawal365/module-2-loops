num=int(input("Please enter a number..."))

sum=0

temp=num

while temp>0:
    digit=temp%10
    sum=digit+sum
    temp//=10

print("the sum is,",sum)