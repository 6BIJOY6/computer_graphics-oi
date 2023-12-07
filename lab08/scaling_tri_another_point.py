import turtle


screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Scale Triangle About Pivot Point")


t = turtle.Turtle()
t.penup()


vertex1 = (100, 0)    
vertex2 = (50, 100)   
vertex3 = (0, 0)     


pivot_point = (50, 50)  
t.goto(pivot_point)
t.dot(5, "green")  


scale_x = 2.0  
scale_y = 1.5  


translated_vertices = []
translated_pivot = (pivot_point[0] - vertex1[0], pivot_point[1] - vertex1[1])
for vertex in [vertex1, vertex2, vertex3]:
    translated_vertices.append((vertex[0] - vertex1[0], vertex[1] - vertex1[1]))


scaled_vertices = []
for vertex in translated_vertices:
    x_scaled = vertex[0] * scale_x
    y_scaled = vertex[1] * scale_y
    scaled_vertices.append((x_scaled, y_scaled))


final_vertices = []
for vertex in scaled_vertices:
    x_final = vertex[0] + vertex1[0]
    y_final = vertex[1] + vertex1[1]
    final_vertices.append((x_final, y_final))

t.goto(vertex1)
t.pendown()
t.goto(vertex2)
t.goto(vertex3)
t.goto(vertex1)
t.penup()


t.goto(final_vertices[0])
t.pendown()
t.goto(final_vertices[1])
t.goto(final_vertices[2])
t.goto(final_vertices[0])
t.penup()





screen.exitonclick()
