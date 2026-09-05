numbers = [12, 45, 2, 89, 34, 67, 10]
sum = 0
for i in numbers:
    sum = sum + i
print(sum)
avg = sum / len(numbers)
largest_num = max(numbers)
smallest_num = min(numbers)
    
print(f"Sum: {sum}")
print(f"Average: {avg}")
print(f"Largest Number: {largest_num}")
print(f"Smallest Number: {smallest_num}")