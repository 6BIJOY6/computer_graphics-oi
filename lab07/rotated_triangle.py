import turtle
import math


screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Rotate Triangle About a Point")


t = turtle.Turtle()
t.penup()


vertex1 = (50, 0)    
vertex2 = (100, 0)   
vertex3 = (75, 50)   


pivot_point = (75, 75)  


t.goto(pivot_point)
t.dot(10, "green")  


t.goto(vertex1)
t.pendown()
t.goto(vertex2)
t.goto(vertex3)
t.goto(vertex1)
t.penup()


vertices = [vertex1, vertex2, vertex3]
rotated_vertices = []

for vertex in vertices:
    dx = vertex[0] - pivot_point[0]
    dy = vertex[1] - pivot_point[1]


    angle_degrees = 45  
    angle_radians = math.radians(angle_degrees)

    
    x_rotated = pivot_point[0] + dx * math.cos(angle_radians) - dy * math.sin(angle_radians)
    y_rotated = pivot_point[1] + dx * math.sin(angle_radians) + dy * math.cos(angle_radians)

    rotated_vertices.append((x_rotated, y_rotated))


t.goto(rotated_vertices[0])
t.pendown()
t.goto(rotated_vertices[1])
t.goto(rotated_vertices[2])
t.goto(rotated_vertices[0])


screen.exitonclick()
