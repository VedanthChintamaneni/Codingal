def tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

second_tuple = (2, 3, 4, 5)
result = tuple(second_tuple)

print(f"The answer is:", result)