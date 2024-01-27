import turtle as t 
import random

tim = t.Turtle() 

b = 3
colors = ["red", "blue", "green", "purple", "orange", "yellow", "black"]

# creates first turtles move 
def draw(a):
  for i in range(a):
    tim.forward(50)
    tim.right(360 / a)

#creates turtles move as many times as user wants
for i in range(b, 12):
  tim.color(random.choice(colors))
  draw(b)
  b += 1