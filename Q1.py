import turtle

def draw_square(t, sz):
#Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.colormode(255)
wn.title("Drawing multiple squares")
alex = turtle.Turtle() # Create alex
alex.pencolor((251,72,196))
alex.width(2)
alex.pendown()
for i in range(4):
    draw_square(alex,20*(i+1))
    alex.penup()
    alex.right(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(10)
    alex.right(180)
    alex.pendown()
#drawing squares

wn.mainloop()