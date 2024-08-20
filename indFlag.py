import turtle as t

t.speed(0)
t.bgcolor("skyblue")
t.title("Indian Flag: Himalayan Majesty")

flag_width = 150
flag_height = 80
stripe_height = flag_height / 3

def rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def chakra(radius):
    t.penup()
    t.goto(-10, -radius+10)
    t.pendown()
    t.color("blue")
    t.circle(radius)
    #spokes
    for _ in range(24):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(15 * _)
        t.forward(radius)


def flag():
    start_y = stripe_height / 2
    #white
    t.penup()
    t.goto(75, start_y)
    t.pendown()
    rectangle("white", flag_width, stripe_height)

    #saffron
    t.penup()
    t.goto(75, start_y + stripe_height)
    t.pendown()
    rectangle("#FF9933", flag_width, stripe_height)

    #green
    t.penup()
    t.goto(75, start_y - stripe_height)
    t.pendown()
    rectangle("#138808", flag_width, stripe_height)

    #ashokChakra
    t.penup()
    t.goto(0, start_y - stripe_height / 2)
    t.pendown()
    chakra(10)  # Chakra size remains the same

    #flagPole
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

    #base
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


def cloud():
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


def laddoo(x, y):
    t.color("#F7D13D")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(10)


def table():
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

    laddoo(115, -146)
    laddoo(125, -146)
    laddoo(135, -146)
    laddoo(120, -139)
    laddoo(130, -139)
    laddoo(125, -132)


def curve(start, radius, angle):
    t.setheading(start)
    t.circle(radius, angle)


def rect2(width, height, color):
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def circle(radius, color):
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def oval(radius_x, radius_y, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius_x, 90)
        t.circle(radius_y, 90)
    t.end_fill()


def head():
    #head
    t.penup()
    t.goto(-180, -185)
    t.pendown()
    circle(25, "peachpuff")

    #eyes
    t.penup()
    t.goto(-190, -160)
    t.pendown()
    circle(3, "black")
    t.penup()
    t.goto(-170, -160)
    t.pendown()
    circle(3, "black")

    #mouth
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


def body():
    t.penup()
    t.goto(-200, -235)
    t.pendown()
    rect2(40, 50, "white")


def legs():
    #left
    t.penup()
    t.goto(-200, -260)
    t.pendown()
    rect2(10, 25, "#0e98ba")

    #right
    t.penup()
    t.goto(-170, -260)
    t.pendown()
    rect2(10, 25, "#0e98ba")


def arms():
    #left
    t.penup()
    t.goto(-210, -210)
    t.pendown()
    rect2(10, 25, "white")

    #right
    t.penup()
    t.goto(-160, -210)
    t.pendown()
    rect2(10, 25, "white")


def hair():
    t.penup()
    t.goto(-30, 100)
    t.pendown()
    rect2(60, 10, "black")


def shoes():
    #left
    t.penup()
    t.goto(-210, -260)
    t.pendown()
    rect2(20, 8, "#564130")

    #right
    t.penup()
    t.goto(-170, -260)
    t.pendown()
    rect2(20, 8, "#564130")


def balloon():
    # green
    t.penup()
    t.goto(-210, -200)
    t.pendown()
    curve(120, -100, 90)
    t.setheading(30)
    oval(35, 20, "#138808")
    # white
    t.penup()
    t.goto(-210, -200)
    t.pendown()
    curve(140, -100, 90)
    t.setheading(30)
    oval(35, 20, "white")
    # saffron
    t.penup()
    t.goto(-205, -210)
    t.pendown()
    curve(160, -100, 90)
    t.setheading(40)
    oval(35, 20, "#FF9933")


def boy():
    head()
    body()
    legs()
    arms()
    shoes()
    balloon()


#grass
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

#mountains
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

#clouds
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

#sun
t.penup()
t.goto(-500, 350)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(125)
t.end_fill()

flag()
cloud()
table()
boy()

t.penup()
t.pencolor("white")
t.goto(40, -265)
t.write("Indian Flag: Himalayan Majesty", font=("Verdana", 15, "normal"))
t.goto(10, -300)
t.write("Happy Independence Day", font=("Verdana", 20, "normal"))

t.hideturtle()
t.done()
