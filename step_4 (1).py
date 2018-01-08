import turtle
import math
import random
wn=turtle.Screen()
wn.bgcolor('pink')
raspusha=turtle.Turtle()
raspusha.speed(0)
raspusha.color('purple')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range(repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(raspusha,100,10)
norbit=turtle.Turtle()
norbit.speed(0)
norbit.color('white')
rotate=int(90)


