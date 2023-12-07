import turtle


screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Scale Point About Origin")


t = turtle.Turtle()
t.penup()


x = 100  
y = 50   


scale_x = 2.0  #
scale_y = 1.5  

t.goto(x, y)
t.dot(5, "blue")  


x_scaled = x * scale_x
y_scaled = y * scale_y


t.goto(x_scaled, y_scaled)
t.dot(5, "red")  

screen.exitonclick()
