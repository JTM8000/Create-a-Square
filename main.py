#function to draw a square
import turtle

t = turtle.Turtle()

def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)



# square(100)
# square(50)
# square(200)

#draw multiple squares

def squares(beginning_size,nb):
    for i in range(0,nb):
        size = (i+1) * beginning_size #since range starts at 0 this adds 1 to it
        square(size) #calls square function
        
squares(10,10)

turtle.done()