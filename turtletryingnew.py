import turtle

voldetort=turtle.Turtle()
voldetort.pensize(10)
voldetort.shape('turtle')
voldetort.color('green')
voldetort.pencolor('blue')
turtle.bgcolor('red')
voldetort.goto(100,0)
id1= voldetort.stamp()
voldetort.goto(100,100)
id2=voldetort.stamp()
a=voldetort.pos()
print(a)
hannah=turtle.clone()
hannah.shape('square')
hannah.pencolor('purple')
hannah.color('light blue')
hannah.pensize(10)
hannah.goto(0,100)
hannah.goto(100,100)


turtle.mainloop()
