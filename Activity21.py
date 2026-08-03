med=input("Do you have a medical cause ? (Y for Yes and N for No)")
att=int(input("What is your attendance ?"))
if med=='Y':
    print("You are allowed into the exam")
else:
    if att > 75:
        print("You are allowed into the exam")
    else:
        print("You are not allowed into the exam")
