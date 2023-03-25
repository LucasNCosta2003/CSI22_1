import turtle
def draw_poly(t,n,sz):
    angle=360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)

#test
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Drawing Polygon")
wn.colormode(255)
alex = turtle.Turtle() # Create alex
alex.width(2)
alex.pencolor((251,72,196))
alex.pendown()
draw_poly(alex,8,50)
#drawing squares

wn.mainloop()