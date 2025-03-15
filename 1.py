import math
x = 3
y = 4
z = 5
a = (1 + math.sin(x + y)**2) / (2 + abs(x + (2 * x) / (1 + x**2 * y**2))) + x
b = math.cos(math.atan(1 / z))**2
print(f"a = {a}")
print(f"b = {b}")
