import turtle


screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Scale Triangle About Origin")

#
t = turtle.Turtle()
t.penup()


vertex1 = (50, 0)    
vertex2 = (0, 100)  
vertex3 = (-50, 0)   


scale_x = 2.0  #
scale_y = 1.5  #


scaled_vertices = []


for vertex in [vertex1, vertex2, vertex3]:
    x_scaled = vertex[0] * scale_x
    y_scaled = vertex[1] * scale_y
    scaled_vertices.append((x_scaled, y_scaled))


t.goto(vertex1)
t.pendown()
t.goto(vertex2)
t.goto(vertex3)
t.goto(vertex1)
t.penup()


t.goto(scaled_vertices[0])
t.pendown()
t.goto(scaled_vertices[1])
t.goto(scaled_vertices[2])
t.goto(scaled_vertices[0])

# Close the Turtle graphics window on click
screen.exitonclick()
