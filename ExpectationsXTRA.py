try:
    marks = int(input("Enter your amount of marks :"))
    print("Your marks are :", marks)
    if marks < 0 or marks > 100:
        raise ValueError ("Marks must be between 0-100")
except ValueError as ex:
    print("Exception :", ex) 
finally:
    print("Checking completed")w
