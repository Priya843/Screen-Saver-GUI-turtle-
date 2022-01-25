from turtle import Turtle,Screen

import random 
colours=["cornflowerblue","darkorchid","indianred","deepskyblue","lightseagreen","wheat","slategray","seagreen","yellow","pink"]


directions=[0,90,180,270]

tim=Turtle()

for _ in range(1,200):
 tim.color(random.choice(colours))
 tim.forward(30)
 tim.setheading(random.choice(directions))
 tim.width(10)
 Screen().bgcolor('black')
 
 # to generate all colours that exist randomly instead of only colours we have listed 
# we use .colormode()

tim.colormode(255)

def random_colour():
  r=random.randint(0,255)
  b=random.randint(0,255)
  g=random.randint(0,255)
  #creating a tuple 
  random_color=(r,b,g)
  return random_color

#and in line 12 change to random color 
tim.color(random_color())