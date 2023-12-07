import turtle
import math

screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Rotate Point About Another Point")


t = turtle.Turtle()
t.penup()


point_x = 100  # Initial x-coordinate of the point
point_y = 0    # Initial y-coordinate of the point


pivot_x = 50   # x-coordinate of the orgin point
pivot_y = 50   # y-coordinate of the orgin point


t.goto(pivot_x, pivot_y)
t.dot(5, "green")  

# Draw the original point
t.goto(point_x, point_y)
t.dot(5, "blue")  # Original point in blue


dx = point_x - pivot_x
dy = point_y - pivot_y


angle_degrees = 45  
angle_radians = math.radians(angle_degrees)

# Calculate the new coordinates after rotation
x_rotated = pivot_x + dx * math.cos(angle_radians) - dy * math.sin(angle_radians)
y_rotated = pivot_y + dx * math.sin(angle_radians) + dy * math.cos(angle_radians)

# Draw the rotated point
t.goto(x_rotated, y_rotated)
t.dot(5, "red")  

# Close the Turtle graphics window on click
screen.exitonclick()
