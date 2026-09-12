weather = (1, 0, 0, 0, 1, 1, 0)

rainy = 0
sunny = 0

for element in weather:
    if element == 1:
        rainy += 1
    else:
        sunny += 1

print(f"Rainy days: {rainy}")
print(f"Sunny days: {sunny}")

if rainy > sunny:
    print("The weather is rainy")
elif sunny > rainy:
    print("The wether is sunny")