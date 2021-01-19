import turtle

tim = turtle.Turtle()
screen = tim.getscreen()
wn = turtle.Screen()
wn.title("Turtle")
wn.bgcolor("light green")


def init():
    #global tim
    #tim = turtle.Turtle()

    stations = []

    num_stations = 10
    for x in range(num_stations):
        stations.append(turtle.Turtle())
        stations[x].penup()

    stations[0].setpos(20, 70)
    stations[1].setpos(-30, -100)
    stations[2].setpos(-150, 70)
    stations[3].setpos(300, 100)
    stations[4].setpos(-200, 150)
    stations[5].setpos(-300, -220)
    stations[6].setpos(-230, -20)
    stations[7].setpos(180, 170)
    stations[8].setpos(-30, 200)

    for i in range(num_stations):
        stations[i].color('#ff964f')
        stations[i].shape('circle')

    goal = turtle.Turtle()
    goal.color('#800080')
    goal.penup()
    goal.setpos(250, 250)
    goal.shape('circle')

    timDefault()


    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.onkey(reset, 'r')

def reset():
    print('reset')
    tim.reset()
    timDefault()

def timDefault():
    tim.penup()
    tim.setpos(-350, 0)
    tim.speed(0)
    tim.resizemode("user")
    tim.shapesize(3, 3, 1)
    tim.pendown()


def up():
    print("Move Forward!")
    #distance = int(input('enter distance'))
    distance = int(screen.numinput('Moving Forward!', 'enter distance', minval=0, maxval=180))
    for i in range(distance):
        tim.forward(1)
    turtle.listen()


def left():
    #angle = int(input('enter angle in degrees'))
    angle = int(screen.numinput('Turning left', 'enter angle in degrees', minval=0))
    for i in range(angle):
        tim.left(1)
    turtle.listen()


#  turtle.shapesize(15, 15, 5)

def right():
    angle = int(screen.numinput('Turning right', 'enter angle in degrees', minval=0))
    for i in range(angle):
        tim.right(1)
    turtle.listen()


#   turtle.shapesize(15, 15, 5)

#turtle.speed(0)

init()

turtle.done()
