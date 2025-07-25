"""
Chapter 3 challenge.
The world is your Turtle! 

"""
import turtle
import random

screen = turtle.Screen()
screen.setup(600,600)
screen.title('Turtle race')
screen.bgcolor('blue')

cand1 = turtle.Turtle(visible=False)
cand1.shape("square")
cand1.color("black")
cand1.speed(10)
cand1.penup()
cand1.goto(200,200)
cand1.pendown()
cand1.setheading(270)

for i in range(20):
    cand1.stamp()
    cand1.forward(20)
    if i % 2 == 0:
        cand1.color('white')
    else:
        cand1.color('black')

# first
judy = turtle.Turtle()
judy.shape("turtle")
judy.color("red")
judy.penup()
judy.goto(-200,-100)    

for i in range(10):
    judy.right(36)

# second
sally = turtle.Turtle()
sally.shape("turtle")
sally.color("purple")
sally.penup()
sally.goto(-200, 100)    

for i in range(10):
    sally.right(36)

# race
while judy.xcor() < 200 and sally.xcor() < 200:
    judy.forward(random.randint(1, 10))
    sally.forward(random.randint(1, 10))

turtle.done()