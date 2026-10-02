test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:", test_dict)

search_value = int(input("Enter the value to check its frequency: "))

frequency = list(test_dict.values()).count(search_value)

print(f"The frequency of value {search_value} is: {frequency}")