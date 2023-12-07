import turtle

def inside(p, edge):
    return (edge[1][0] - edge[0][0]) * (p[1] - edge[0][1]) > (edge[1][1] - edge[0][1]) * (p[0] - edge[0][0])

def intersection(p1, p2, edge):
    dc = [p1[0] - p2[0], p1[1] - p2[1]]
    dp = [edge[0][0] - edge[1][0], edge[0][1] - edge[1][1]]
    n1 = p1[0] * p2[1] - p1[1] * p2[0]
    n2 = edge[0][0] * edge[1][1] - edge[0][1] * edge[1][0]
    n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
    return [(n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3]

def clip(subject_polygon, clip_polygon):
    output_polygon = subject_polygon.copy()

    for edge in clip_polygon:
        input_polygon = output_polygon.copy()
        output_polygon = []

        s = input_polygon[-1]
        for e in input_polygon:
            if inside(e, edge):
                if not inside(s, edge):
                    output_polygon.append(intersection(s, e, edge))
                output_polygon.append(e)
            elif inside(s, edge):
                output_polygon.append(intersection(s, e, edge))
            s = e

    return output_polygon

def draw_polygon(polygon, color="black"):
    turtle.penup()
    turtle.goto(polygon[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for point in polygon:
        turtle.goto(point)
    turtle.end_fill()

def main():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.title("Sutherland-Hodgman Polygon Clipping")

    subject_polygon = [(100, 100), (200, 100), (200, 200), (100, 200)]
    clip_polygon = [(150, 50), (250, 50), (250, 150), (150, 150)]

    draw_polygon(subject_polygon, "blue")
    draw_polygon(clip_polygon, "red")

    clipped_polygon = clip(subject_polygon, clip_polygon)

    draw_polygon(clipped_polygon, "green")

    turtle.exitonclick()

if __name__ == "__main__":
    main()
