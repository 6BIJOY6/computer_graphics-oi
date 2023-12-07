import turtle as t


def l_b(x1,y1,x2,y2,xmax,ymax,xmin,ymin):
    dx= x2-x1;
    dy=y2-y1;
    p = [0]*4
    q= [0]*4
    p[0]=-dx
    p[1]=dx
    p[2]=-dy
    p[3]=dy
    q[0]=x1-xmin
    q[1]=xmax-x1
    q[2]=y1-ymin
    q[3]=ymax-y1


    for i in  range(4):
        if p[i] == 0:
            if q[i]<0:
                print("line is parallel and outside the window")
                return None
        
        elif p[i]<0:
            t1=max(0,q[i]/p[i])
        else:
            t2=min(1,q[i]/p[i])
    
    if t1>t2:
        print("line already outside the window")
        return None
    

    x_start=x1+t1*dx
    y_start=y1+t1*dy
    x_end=x1+t2*dx
    y_end= y1+t2*dy
    

    drw(x_start,y_start,x_end,y_end)


def drw(x_start,y_start,x_end,y_end):
    t.penup()
    t.pencolor("blue")
    t.goto(x_start,y_start)
    t.pendown()
    t.goto(x_end,y_end)





    



x1=float(input("enter the value of x1: "))
y1=float(input("enter the value of y1: "))
x2=float(input("enter the value of x2: "))
y2=float(input("enter the value of y2: "))
xmax=float(input("enter the value of xmax: "))
ymax=float(input("enter the value of ymax: "))
xmin=float(input("enter the value of xmin: "))
ymin=float(input("enter the value of ymin: "))


t.penup()
t.goto(xmin,ymin)
t.pencolor("green")
t.pendown()
t.goto(xmax,ymin)
t.goto(xmax,ymax)
t.goto(xmin,ymax)
t.goto(xmin,ymin)


t.penup()
t.goto(x1,y1)
t.pencolor("red")
t.pendown()
t.goto(x2,y2)


l_b(x1,y1,x2,y2,xmax,ymax,xmin,ymin)
t.done()


