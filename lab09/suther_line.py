import turtle as t

inside = 0 
left = 1
right = 2
top = 8
bottom = 4

def r_code(x, y, xmax, ymax, xmin, ymin):
    code = inside
    if x < xmin:
        code |= left
    elif x > xmax:
        code |= right
    if y > ymax:
        code |= top
    elif y < ymin:
        code |= bottom
    
    return code

def cohn_sutherland(x1, y1, x2, y2, xmin, xmax, ymax, ymin, m):
    code1 = r_code(x1, y1, xmax, ymax, xmin, ymin)
    code2 = r_code(x2, y2, xmax, ymax, xmin, ymin)

    accept = False

    while True:
        if code1 == code2 == inside:
            accept = True
            break
        elif code1 & code2 != 0:
            print("completely outside")
            break
        else:
            code_outside = code1 if code1 != inside else code2

            if code_outside & top:
                y = ymax 
                x = x1 + m * (ymax - y1)
            elif code_outside & bottom:
                y = ymin
                x = x1 + m * (ymin - y1)
            elif code_outside & left:
                x = xmin
                y = y1 + (xmin - x1) / m
            elif code_outside & right:
                x = xmax
                y = y1 + (xmax - x1) / m

            if code_outside == code1:
                x1, y1 = x, y
                code1 = r_code(x1, y1, xmax, ymax, xmin, ymin)
            else:
                x2, y2 = x, y
                code2 = r_code(x2, y2, xmax, ymax, xmin, ymin)

    if accept:
        draw_c_line(x1, y1, x2, y2)

def draw_c_line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pencolor("green")
    t.goto(x2, y2)

# Value input
x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y1: "))
x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))
xmax = float(input("Enter the value of xmax: "))
ymax = float(input("Enter the value of ymax: "))
xmin = float(input("Enter the value of xmin: "))
ymin = float(input("Enter the value of ymin: "))

m = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')

t.penup()
t.goto(xmin, ymin)
t.pendown()
t.goto(xmax, ymin)
t.goto(xmax, ymax)
t.goto(xmin, ymax)
t.goto(xmin, ymin)

t.penup()
t.goto(x1, y1)
t.pendown()
t.pencolor("red")
t.goto(x2, y2)

cohn_sutherland(x1, y1, x2, y2, xmin, xmax, ymax, ymin, m)

t.done()
