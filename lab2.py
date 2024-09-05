#part 1: variables and assignments

name = 'ashly'
age = 20
height = 5.7
favorite_color = 'black'

#part 1.2.1

print(name)
print(age)
print(height)
print(favorite_color)

#part 1.2.2

print(name,age,height,favorite_color)

# part 1.2.3

print(f"Hello {name} I like the color {favorite_color}. I'm {age} years old and I'm {height} ft.")

#part 1.2.4

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}
""")

#part 1.3

from math import pi

radius = 5
area = pi * radius ** 2
print(f'circle_area is {area:.1f}')  # 1 decimal

#part 2: statements and modules

from math import sqrt
sq = sqrt(age)
print(sq)

from math import sin
sine = sin(height)
print(f'The answer is {sine:.2f}')  #only allowed 2 decimals

from math import cos
cosine = cos(height)
print(f'The answer is {cosine:.3f}')  # only allowed 3 decimals

#part 3 Expressions and operators

addition = age + 5
print(addition)

difference = height - 4
print(difference)

product = age * height
print(product)

remain = age % 3
print(remain)

power = age ** 2
print(power)

from math import pow
to_the = pow(age, 2)
print(f'{to_the:.0f}')

#part 4 temperature conversion

fahrenheit = float(input(f"Temperature (F): "))
celsius = (fahrenheit - 32) * 5/9
print(f'The temperature is {celsius:.1f}°C')