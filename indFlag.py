import turtle as t

# Setting up the environment
t.speed(0)
t.bgcolor("skyblue")
t.title("Indian Flag: Himalayan Majesty")

flag_width = 150
flag_height = 80
stripe_height = flag_height / 3


def draw_rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()


def draw_chakra(radius):
    t.penup()
    t.goto(-10, -radius+10)
    t.pendown()
    t.color("blue")
    t.circle(radius)
    # Draw 24 spokes
    for _ in range(24):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(15 * _)
        t.forward(radius)


def draw_flag():
    # Center the white stripe on the screen
    start_y = stripe_height / 2

    # Draw the white stripe (centered)
    t.penup()
    t.goto(75, start_y)
    t.pendown()
    draw_rectangle("white", flag_width, stripe_height)

    # Draw the saffron stripe above the white stripe
    t.penup()
    t.goto(75, start_y + stripe_height)
    t.pendown()
    draw_rectangle("#FF9933", flag_width, stripe_height)

    # Draw the green stripe below the white stripe
    t.penup()
    t.goto(75, start_y - stripe_height)
    t.pendown()
    draw_rectangle("#138808", flag_width, stripe_height)

    # Draw the Ashoka Chakra in the center of the white stripe
    t.penup()
    t.goto(0, start_y - stripe_height / 2)
    t.pendown()
    draw_chakra(10)  # Chakra size remains the same

    # Draw the flagpole
    t.penup()
    t.goto(-flag_width / 2 - 6, start_y + stripe_height - 2)
    t.pendown()
    t.color("gray")
    t.width(3)
    t.setheading(270)
    t.forward(flag_height + 120)

    t.penup()
    t.goto(-flag_width / 2 - 5, start_y + stripe_height)
    t.pendown()
    t.color("black")
    t.width(2.5)
    t.setheading(270)
    t.forward(flag_height + 120)

    # Add a decorative base for the flagpole
    t.width(1)
    t.penup()
    t.goto(-flag_width / 2 - 12, start_y - flag_height - 90)
    t.pendown()
    t.color("#4B5320")
    t.begin_fill()
    t.fillcolor("#4B5320")
    t.setheading(0)
    for _ in range(2):
        t.forward(15)
        t.right(90)
        t.forward(8)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(-flag_width / 2 - 17, start_y - flag_height - 97)
    t.pendown()
    t.color("#4B5320")
    t.begin_fill()
    t.fillcolor("#4B5320")
    t.setheading(0)
    for _ in range(2):
        t.forward(25)
        t.right(90)
        t.forward(8)
        t.right(90)
    t.end_fill()


def draw_cloud():
    t.color("white")

    t.penup()
    t.goto(100, 250)
    t.pendown()
    t.dot(30)

    t.penup()
    t.goto(125, 260)
    t.pendown()
    t.dot(55)

    t.penup()
    t.goto(150, 255)
    t.pendown()
    t.dot(45)

    t.penup()
    t.goto(-200, 250)
    t.pendown()
    t.dot(30)

    t.penup()
    t.goto(-175, 260)
    t.pendown()
    t.dot(55)

    t.penup()
    t.goto(-150, 262)
    t.pendown()
    t.dot(52)

    t.penup()
    t.goto(-125, 255)
    t.pendown()
    t.dot(40)


def draw_laddoo(x, y):
    t.color("#F7D13D")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(10)


def draw_table():
    t.width(1)
    t.penup()
    t.goto(103, -150)
    t.pendown()
    t.color("#564130")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(5)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(142, -150)
    t.pendown()
    t.color("#564130")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(5)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(100, -150)
    t.pendown()
    t.color("#453427")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(50)
        t.right(90)
        t.forward(5)
        t.right(90)
    t.end_fill()

    draw_laddoo(115, -146)
    draw_laddoo(125, -146)
    draw_laddoo(135, -146)
    draw_laddoo(120, -139)
    draw_laddoo(130, -139)
    draw_laddoo(125, -132)


def draw_curve(start, radius, angle):
    t.setheading(start)
    t.circle(radius, angle)


def draw_rectangle2(width, height, color):
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_circle(radius, color):
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_oval(radius_x, radius_y, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius_x, 90)  # Draw one half of the oval
        t.circle(radius_y, 90)  # Draw the other half
    t.end_fill()


def draw_head():
    t.penup()
    t.goto(-180, -185)
    t.pendown()
    draw_circle(25, "peachpuff")

    # eyes
    t.penup()
    t.goto(-190, -160)
    t.pendown()
    draw_circle(3, "black")
    t.penup()
    t.goto(-170, -160)
    t.pendown()
    draw_circle(3, "black")

    # mouth
    t.penup()
    t.goto(-180, -165)
    t.pendown()
    t.color("red")
    t.dot(15)
    t.penup()
    t.goto(-180, -162)
    t.pendown()
    t.color("peachpuff")
    t.dot(15)


def draw_body():
    t.penup()
    t.goto(-200, -235)
    t.pendown()
    draw_rectangle2(40, 50, "white")


def draw_legs():
    # Left leg
    t.penup()
    t.goto(-200, -260)
    t.pendown()
    draw_rectangle2(10, 25, "#0e98ba")

    # Right leg
    t.penup()
    t.goto(-170, -260)
    t.pendown()
    draw_rectangle2(10, 25, "#0e98ba")


def draw_arms():
    # Left arm
    t.penup()
    t.goto(-210, -210)
    t.pendown()
    draw_rectangle2(10, 25, "white")

    # Right arm
    t.penup()
    t.goto(-160, -210)
    t.pendown()
    draw_rectangle2(10, 25, "white")


def draw_hair():
    t.penup()
    t.goto(-30, 100)
    t.pendown()
    draw_rectangle2(60, 10, "black")


def draw_shoes():
    t.penup()
    t.goto(-210, -260)
    t.pendown()
    draw_rectangle2(20, 8, "#564130")

    t.penup()
    t.goto(-170, -260)
    t.pendown()
    draw_rectangle2(20, 8, "#564130")


def draw_balloon():
    #green
    t.penup()
    t.goto(-210, -200)
    t.pendown()
    draw_curve(120, -100, 90)
    t.setheading(30)
    draw_oval(35, 20, "#138808")
    #white
    t.penup()
    t.goto(-210, -200)
    t.pendown()
    draw_curve(140, -100, 90)
    t.setheading(30)
    draw_oval(35, 20, "white")
    #saffron
    t.penup()
    t.goto(-205, -210)
    t.pendown()
    draw_curve(160, -100, 90)
    t.setheading(40)
    draw_oval(35, 20, "#FF9933")


def draw_boy():
    draw_head()
    draw_body()
    draw_legs()
    draw_arms()
    # draw_hair()
    draw_shoes()
    draw_balloon()


# Drawing the grass
t.penup()
t.goto(-400, -100)
t.pendown()
t.color("limegreen")
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

# Drawing mountains
t.penup()
t.goto(-400, -100)
t.pendown()
t.color("dimgray")
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.left(120)
t.end_fill()

t.penup()
t.goto(100, -100)
t.pendown()
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-160, -100)
t.pendown()
t.color("gray")
t.begin_fill()
for i in range(3):
    t.forward(400)
    t.left(120)
t.end_fill()

# Drawing the clouds
t.penup()
t.goto(-35, 120)
t.pendown()
t.color("white")
t.begin_fill()
t.left(35)
t.forward(60)
t.right(90)
t.forward(30)
t.left(100)
t.forward(45)
t.right(85)
t.forward(65)
t.left(160)
t.forward(150)
t.end_fill()

t.penup()
t.goto(-215, 100)
t.pendown()
t.color("snow")
t.begin_fill()
t.forward(70)
t.left(120)
t.forward(75)
t.left(150)
t.forward(45)
t.right(90)
t.forward(45)
t.left(120)
t.end_fill()

t.penup()
t.goto(203, 80)
t.pendown()
t.begin_fill()
t.forward(95)
t.right(120)
t.forward(80)
t.right(150)
t.forward(50)
t.left(70)
t.end_fill()

t.left(50)

# Drawing the sun
t.penup()
t.goto(-500, 350)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(125)
t.end_fill()

draw_flag()
draw_cloud()
draw_table()
draw_boy()

t.hideturtle()
t.done()
