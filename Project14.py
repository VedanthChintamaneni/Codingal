import math

angle_in_degrees = 45

angle1 = math.radians(angle_in_degrees)

sin_value = math.sin(angle1)
cosine_value = math.cos(angle1)
tangent_value = math.tan(angle1)

print(f"Trigonometric values for {angle_in_degrees}°:")
print(f"Sine:   {round(sin_value, 4)}")
print(f"Cosine: {round(cosine_value, 4)}")
print(f"Tangent:{round(tangent_value, 4)}")