import turtle as t
import math




t.penup()
x = 50  
y = 50
angle_degrees = 45  



t.goto(x, y)
t.dot(10, "blue")  


angle_radians = math.radians(angle_degrees)


x_rotated = x * math.cos(angle_radians) - y * math.sin(angle_radians)
y_rotated = x * math.sin(angle_radians) + y * math.cos(angle_radians)


t.goto(x_rotated, y_rotated)
t.dot(10, "green")  # Rotated point in red


t.done()
