def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x,y):
    return x/y

print("Choose an operation :")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")

choice = int(input("Choose a number, 1,2,3 or 4"))

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
elif choice == 4:
    print(divide(num1, num2))