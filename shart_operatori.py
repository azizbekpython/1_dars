import math

a = 2.5

def y(x):
    if x < 1:
        return 1.5 * (math.cos(x) ** 2)
    elif 1 <= x <= 2:
        return (x - 2) ** 2 + 6
    else:  # x > 2
        return 3 * math.tan(x)

# Misol uchun, a = 2.5 bo‘lganda y(a) ni hisoblaymiz:
result = y(a)
print(f"y({a}) = {result}")
