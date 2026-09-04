try:
    user_input = input("Enter your age: ")
    age = int(user_input)
    
    if age % 2 == 0:
        print(f"The age {age} is an even number.")
    else:
        print(f"The age {age} is an odd number.")

except ValueError:
    print("Enter a whole number")