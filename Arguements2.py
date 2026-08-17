def cube(number):
    return number*number*number

def divisible(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
        
print(divisible(8))
