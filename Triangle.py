import math
from math import sqrt, cos
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
angle = float(input("Введите угол (в градусах) между сторонами: "))

angle_rad = math.radians(angle)

c = sqrt(a**2 + b**2 - 2 * a * b * cos(angle_rad))

print("Длина третьей стороны равна:", round(c, 2))