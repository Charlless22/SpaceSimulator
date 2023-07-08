#!/usr/bin/env python3

# doing the imort

import turtle, math, random

# creating the values

sizePlanet = [4, 0.4, 0.9, 1, 0.6, 2.5, 2, 1.6, 1.5, 0.2]
sizeOrbit = [2, 60, 80, 100, 140, 200, 250, 300, 400, 500]
orbitSpeed = 8000
planetColours = [['yellow', 'orange'], ['grey', 'white'], ['orange', 'yellow'], ['blue', 'green'], ['red', 'orange'], ['orange', 'brown'], ['yellow', 'brown'], ['turquoise', 'blue'], ['blue', 'turquoise'], ['grey', 'brown']]
starColour = [['white', 'white']]

# creating the window

screen = turtle.Screen()
screen.bgcolor('black')

# activate turtle

Sun = turtle.Turtle()
Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()
Uranus = turtle.Turtle()
Neptune = turtle.Turtle()
Pluto = turtle.Turtle()
Star = turtle.Turtle()
Comet = turtle.Turtle()
BlackHole = turtle.Turtle()

# giving planet values

Planets = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
for i in range(len(Planets)):
    Planets[i].speed(orbitSpeed / sizeOrbit[i])
    Planets[i].shape('circle')
    Planets[i].shapesize(stretch_wid=sizePlanet[i])
    Planets[i].fillcolor(planetColours[i][0])
    Planets[i].pencolor(planetColours[i][0])
    Planets[i].left(random.randint(0, 360))
    Planets[i].up()
    Planets[i].forward(sizeOrbit[i])
    Planets[i].down()
    Planets[i].left(90)

# creating stars

Star.speed(0)
Star.hideturtle()
Star.penup()

for _ in range(50):
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    Star.goto(x, y)
    Star.dot(2, 'white')

# enable black hole values and create them

BlackHole.speed(0)
BlackHole.shape('circle')
BlackHole.shapesize(3)
BlackHole.fillcolor('pink')
BlackHole.up()
BlackHole.hideturtle()

def show_black_hole():
    if BlackHole.isvisible():
        return

    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    BlackHole.up()
    BlackHole.goto(x, y)
    BlackHole.showturtle()
    turtle.ontimer(hide_black_hole, 1000)

def hide_black_hole():
    BlackHole.hideturtle()

# simulation code

while True:
    for i in range(len(Planets)):
        if i != 0:
            if BlackHole.isvisible():
                angle = Planets[i].towards(BlackHole.position())
                Planets[i].setheading(angle)
                Planets[i].forward(10)
            else:
                Planets[i].forward((sizeOrbit[i] * math.pi / 0.4 / sizeOrbit[i]))
                Planets[i].left(450 / sizeOrbit[i])
                if random.random() < 0.001:
                    show_black_hole()

    turtle.update()

turtle.done()
