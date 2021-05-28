from turtle import Turtle
from random import randint

bob = Turtle()
cat = Turtle()
dom = Turtle()
eve = Turtle()

bob.color("green")
cat.color("red")
dom.color("orange")
eve.color("yellow")

bob.shape("turtle")
cat.shape("turtle")
dom.shape("turtle")
eve.shape("turtle")

bob.penup()
bob.goto(-160, 100)
bob.pendown()

cat.penup()
cat.goto(-160, 70)
cat.pendown()

dom.penup()
dom.goto(-160, 40)
dom.pendown()

eve.penup()
eve.goto(-160, 10)
eve.pendown()

for movement in range(100):
    bob.forward(randint(1,5))
    cat.forward(randint(1,5))
    dom.forward(randint(1,5))
    eve.forward(randint(1,5))

input("Press Enter to close")