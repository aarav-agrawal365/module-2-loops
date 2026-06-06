print("select your ride")
print(1,(".car"))
print(2,(".bike"))

choice=int(input("please enter your choice..."))

if choice==1:
    print("great choice, which car do you want?")
    print(1,".sedan")
    print(2,(".XUV"))
    choice2=int(input("please enter your choice.."))
    if choice2==1:
        print("you have selected sedan")
    else:
        print("you have selected XUV ")
elif choice==2:
    print("great choice, which bike do you want?")
    print(1,".scooty")
    print(2,(".sport bike"))
    choice3=int(input("please enter your choice.."))
    if choice3==1:
        print("you have selected scooty")
    else:
        print("you have selected sport bike ")

else:
    print("wrong choice")
    