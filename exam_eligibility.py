medical_cause=input("was your absense due to some medical issue? Please enter Y or N...")
atten= int(input("enter attendence of student...."))
if medical_cause=="Y":
    print("you are allowed")

else:
    if atten >=70:
        print("allowed")

    else:
        print("not allowed")