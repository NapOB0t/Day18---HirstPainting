# import colorgram
import random
import turtle
from turtle import Turtle, Screen
from random import Random

# colors = colorgram.extract('Hirst.jpg', 110)
# list_colors = []
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     new_color = (r, g, b)
#     list_colors.append(new_color)
#
# print(list_colors)
jim = Turtle()
screen = Screen()
jim.ht()
jim.speed(20)
turtle.colormode(255)
color_list = [(230, 224, 217), (231, 206, 86), (217, 228, 218), (231, 221, 225), (227, 147, 81), (212, 224, 231),
              (121, 167, 185), (36, 109, 155), (157, 14, 22), (230, 83, 49), (125, 175, 144), (169, 21, 16),
              (195, 65, 31),
              (32, 127, 48), (9, 97, 38), (185, 185, 28), (13, 41, 75), (16, 63, 40), (137, 81, 95), (86, 15, 22),
              (243, 201, 4), (52, 165, 77), (45, 27, 23), (172, 134, 148), (8, 65, 135), (232, 169, 160),
              (53, 149, 190),
              (212, 71, 75), (77, 134, 184), (168, 207, 172), (222, 174, 178), (164, 201, 211), (173, 191, 215),
              (50, 70, 73), (247, 10, 23)]


def random_color():
    rgb_color = random.choice(color_list)
    return rgb_color


def positioning():

    y = jim.ycor()
    up = y + 50

    return jim.setposition(-255, up)


jim.penup()
dot_hor = 0
jim.setposition(-255, -200)

while dot_hor < 10:
    dot_vert = 0
    while dot_vert < 10:
        jim.dot(20, random_color())
        jim.forward(50)
        dot_vert += 1
    dot_hor += 1
    positioning()


screen.exitonclick()
