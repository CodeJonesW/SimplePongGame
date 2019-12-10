# Simple Pong Tutorial Follow-Along


#Part 1


import turtle

wn = turtle.Screen()
wn.title("Will's Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#main game loop
while True:
    wn.update()