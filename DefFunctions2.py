num = int(input("Enter a positive integer : "))

if num % 20 == 0:
        print("TWIST")
        
elif num % 15 == 0:
        pass 
        
elif num % 5 == 0:
        print("FIZZ")
        
elif num % 3 == 0:
        print("BUZZ")

else:
        print(num)