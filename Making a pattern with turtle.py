import turtle
x = 0
turtle.goto(x,0)
for i in range (0,5): #This loop is going to move the turtle after it draws a shape
    for shape in range(0,8): #This loop draws the pattern
        turtle.down()
        turtle.forward(40)
        turtle.left(180)
        turtle.forward(40)
        turtle.left(45)
    
    turtle.up() #stops the pen drawing while turtle moves across
    x+=100
    turtle.goto(x,0)#moves the turtle to it's new starting point




    
