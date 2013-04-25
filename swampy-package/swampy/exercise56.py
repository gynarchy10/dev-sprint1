# This is where Exercise 5.6 goes
# Name: Jenna Gopilan 

from TurtleWorld import *         

world = TurtleWorld()            
bob = Turtle()
bob.delay = 0.01

        
def koch_curve(t, length):
    if length < 3:
        return fd (t, length)
    koch_curve(t, length / 3)
    lt (t, 60)
    koch_curve(t, length / 3)
    rt (t, 120)
    koch_curve(t, length / 3)
    lt (t, 60)
    koch_curve(t, length / 3)
        

#koch_curve (bob, 100)

def snowflake(t, length):
    for i in range (3):
        koch_curve(t, length)
        rt (t, 120)

snowflake(bob, 100)

wait_for_user()
