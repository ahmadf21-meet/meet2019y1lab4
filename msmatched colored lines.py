import turtle

voldetort=turtle.Turtle()
thanus=turtle.Turtle()
voldetort.shape('circle')
voldetort.left(90)
thanus.shape('arrow')
turtle.bgcolor('purple')
thanus.color('blue')
voldetort.color('white')
voldetort.pensize(5)
thanus.pensize(5)
voldetort.pencolor('yellow')
thanus.pencolor('green')
voldetort.goto(0,150)
thanus.goto(0,-150)
thanus.goto(75,-150)
thanus.pencolor('blue')
thanus.goto(75,0)
voldetort.goto(-75,150)
voldetort.pencolor('white')
voldetort.goto(-75,0)

turtle.mainloop()
