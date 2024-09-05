from math import pi, sqrt as sq
radius = int(input('give me the radius:'))
area = pi * radius ** 2
print(sq(area))
print(area)

try:
    radius = int(input('give me the radius:'))
except ValueError as e:
    pass
