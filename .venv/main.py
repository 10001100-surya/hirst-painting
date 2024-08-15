import random
import turtle

# colorgram module to extract color from image
from turtle import Screen, Turtle
from random import Random
turtle.colormode(255)

rgb_colour =[
 (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),(43, 212, 71),
 (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
 (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
 (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)
]
turtle.colormode(255)
screen = Screen()
screen.title("Hirst painting")
timmy = Turtle()
timmy.hideturtle()
timmy.speed(10)

for _ in range(7):
  # timmy.dot(20, random.choice(rgb_colour))

  timmy.setheading(225)
  timmy.penup()
  timmy.forward(50)

timmy.setheading(0)
timmy.forward(50)

def left_move():
    for _ in range(10):
      timmy.setheading(0)
      timmy.dot(20, random.choice(rgb_colour))
      timmy.forward(50)

    timmy.left(90)
    timmy.forward(50)

def right_move():
    for _ in range(10):
      timmy.setheading(180)
      timmy.forward(50)
      timmy.dot(20, random.choice(rgb_colour))

    timmy.right(90)
    timmy.forward(50)

for _ in range(5):
    left_move()
    right_move()



screen = Screen()
screen.exitonclick()