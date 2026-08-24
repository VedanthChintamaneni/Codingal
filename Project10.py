def circle_circumference(radius):
    return 2 * 3.14 * radius

user_radius = float(input("Enter the radius of the circle: "))

result = circle_circumference(user_radius)

print("The circumference is:", result)