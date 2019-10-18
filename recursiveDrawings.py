import turtle

def spiral(initialLength, angle, multiplier):
    """ This function creates a spiral from outside to inside. """
# Base case: recursion stops when the length becomes less than 1.
    if initialLength < 1:
        pass

    else:
# Recursive part of the program; repeatedly reduces the length by
# multiplying the length by the multiplier; also shifts the angle so that
# it goes in a spiral.
        chaz.forward(initialLength * multiplier)
        chaz.right(angle)
        spiral(initialLength * multiplier, angle, multiplier)


chaz = turtle.Turtle()
chaz.speed(5)
spiral(100, 90, 0.9)

#this creates the tree function, which recursively draws branches of a tree 
def tree(trunkLength, height):
    """ This function recursively draws branches to a tree"""
    if height == 0:
        pass
    else:
# Recursive steps to the drawing of the tree branches; the trunkLength
# parameter is divided by 2 every time a new branch is made, since the 
# branches get smaller as the tree expands. The height parameter is
# reduced by 1 each time a branch is made, since the parameter
# represents a fork in the tree, in which a new branch is made each
# time it reaches a new fork
        t.forward(trunkLength)
        t.left(45)
        t.forward(trunkLength / 2)
        t.backward(trunkLength / 2)
        tree(trunkLength / 2, height - 1)
        t.right(90)
        t.forward(trunkLength / 2)
        t.backward(trunkLength / 2)
        tree(trunkLength / 2, height - 1)
        t.left(45)
        t.backward(trunkLength)

t = turtle.Turtle()
t.speed(1)
#this left turn starts the turtle off in the right direction to make this tree
t.left(90)
tree(200, 4)

# this snowflake function creates three sides to the snowflake
def snowflake(sideLength, levels):
    snowflakeSide(sideLength, levels)
    s.left(120)
    snowflakeSide(sideLength, levels)
    s.left(120)
    snowflakeSide(sideLength, levels)

# this snowflakeSide function recursively draws the different snowflakes depending on the levels and length of the sides

def snowflakeSide(sideLength, levels):
# this basically says if there are no levels to the snowflake, a basic 
# triangle is made
    if levels == 0:
        s.forward(sideLength)
# else, if there are levels to the triangle, it creates the different snowflakes
# that corrlate to each level
    else:
        snowflakeSide(sideLength / 3, levels - 1)
        s.right(60)
        snowflakeSide(sideLength / 3, levels - 1)
        s.left(120)
        snowflakeSide(sideLength / 3, levels - 1)
        s.right(60)
        snowflakeSide(sideLength / 3, levels - 1)

s = turtle.Turtle()
s.speed(5)
snowflake(280, 4)

# this command here at the end keeps the screen up after the code is ran, so 
# that it doesn't close right when it finishes
k = input("press close to exit")
