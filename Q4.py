import turtle

def draw_2_spirals(t,p,sz,angle):
    t.penup()
    t.goto((-2*sz-10,0))
    p.penup()
    p.goto((2*sz+10,0))
    t.pendown()
    p.pendown()
    for i in range(sz+1):
        t.forward(2*(i))
        t.right(90)
        p.forward(2*(i))
        p.right(angle)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Drawing Spirals")
alex = turtle.Turtle() # Create alex
joe=turtle.Turtle() #creates joe
alex.speed(speed=10)
joe.speed(speed=10)
alex.pencolor('blue')
joe.pencolor('blue')
draw_2_spirals(alex,joe,99,89)
wn.mainloop()
#drawing squares