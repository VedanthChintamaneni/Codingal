print("Select your mode of transport:  ")
print("1. Bike")
print("2. Car")
choice=int(input("Enter your choice :  "))
if(choice == 1):
    print("What type of bike ?")
    print("1. Scooty")
    print("2. Motorbike")
    choice2=int(input("Enter your second choice :"))
    if choice2==1:
        print("You have selected the Scooty")
    else:
        print("You have selected the Motorbike")
elif(choice==2):
    print("What type of car ?")
    print("1. Toyota")
    print("2. BMW")
    choice3=int(input("Enter your second choice :"))
    if choice3==1:
        print("You have selected the Toyota")
    else:
        print("You have selected the BMW")
 
