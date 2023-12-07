import turtle
import math


screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Rotate Line About a Point")


t = turtle.Turtle()
t.penup()


line_start = (50, 0)  
line_end = (100, 0)   

# Define the pivot point's coordinates
pivot_point = (40, 40)  # x-coordinate and y-coordinate of the pivot point


t.goto(pivot_point)
t.dot(5, "green")  


t.goto(line_start)
t.pendown()
t.goto(line_end)
t.penup()


dx_start = line_start[0] - pivot_point[0]
dy_start = line_start[1] - pivot_point[1]
dx_end = line_end[0] - pivot_point[0]
dy_end = line_end[1] - pivot_point[1]


angle_degrees = 45  
angle_radians = math.radians(angle_degrees)


x_start_rotated = pivot_point[0] + dx_start * math.cos(angle_radians) - dy_start * math.sin(angle_radians)
y_start_rotated = pivot_point[1] + dx_start * math.sin(angle_radians) + dy_start * math.cos(angle_radians)
x_end_rotated = pivot_point[0] + dx_end * math.cos(angle_radians) - dy_end * math.sin(angle_radians)
y_end_rotated = pivot_point[1] + dx_end * math.sin(angle_radians) + dy_end * math.cos(angle_radians)


t.goto(x_start_rotated, y_start_rotated)
t.pendown()
t.goto(x_end_rotated, y_end_rotated)


screen.exitonclick()
