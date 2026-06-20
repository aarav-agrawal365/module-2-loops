print("We are going to print a half pyramid of stars!")
n=int(input("Please enter the amount of cloumns you want:"))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()