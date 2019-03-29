from turtle import *
from math import *

'''
#test
bgcolor("orange")
pen = Pen()
screensize(200,150)
pen.up()
#pen.setx(-300)
#pen.sety(-200)
pen.down()
pen.speed(0)
pen.color("purple")
pen.fillcolor("red")
'''

#number of lines or squares, circles etc. in the figure
numOfLine = 0


def clearNumOfLine():
    global numOfLine
    numOfLine = 0
#end clearNumOfLine

def drawTree(pen, n ,l):

    global numOfLine
    
    if n==0 or l<2 :
        return
     #endif

    pen.forward(l)
    pen.left(45)
    drawTree(pen, n-1, l/2)
    pen.right(25)
    drawTree(pen, n-1, l/2)
    pen.right(40)
    drawTree(pen, n-1, l/2)
    pen.right(25)
    drawTree(pen, n-1, l/2)
    pen.left(45)
    pen.backward(l)


    numOfLine += 1

    if numOfLine == 1:
        return "There is only " + str(numOfLine) + " line in this figure." + "\nTry to add orders to construct a tree:)"
        
    return "There are " + str(numOfLine) + " lines in this tree."
#end drawTree


def drawFern(pen,n,l):
    #termination:
    if n == 0 or l < 2:
        return
    #end if

    pen.forward(2*l/3)
    pen.right(30); drawFern(pen,n-1, 0.5*l); pen.left(30)

    pen.forward(2*l/3)
    pen.left(45); drawFern(pen,n-1, 0.6*l); pen.right(45)

    pen.forward(2*l/3)
    pen.right(10); drawFern(pen,n-1, 0.7*l); pen.left(10)

    pen.backward(2*l)

    global numOfLine
    numOfLine += 1

    if numOfLine == 1:
        return "There is only " + str(numOfLine) + " line in this figure." + "\nTry to add orders to construct a fern:)"
        
    return "There are " + str(numOfLine) + " lines in this fern."
#end drawFern

    
def drawFlower(pen, n ,l):
    if n==0 or l<2 :
        return
     #endif

    pen.forward(l)
    pen.left(135)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.right(45)
    drawFlower(pen, n-1 ,l/3)

    pen.left(180)
    pen.backward(l)

    global numOfLine
    numOfLine += 1

    if numOfLine == 1:
        return "There is only " + str(numOfLine) + " line in this figure." + "\nTry to add orders to construct a flower:)" 

    return "There are " + str(numOfLine) + " lines in this flower."
#end draw Flower


def drawNestedSquare(pen, n, l):
    
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        numOfLine += 1
        return "There is only " + str(numOfLine) + " square in this figure."
    #end if
    #end termination

    for i in range(4):
        pen.forward(l)
        pen.left(90)

    pen.up()
    pen.left(90)
    pen.forward(l*0.135)
    pen.right(90)
    pen.backward(l*0.02)
    pen.right(10)
    pen.down()
    drawNestedSquare(pen, n-1, l*0.9)

    numOfLine += 1

    return "There are " + str(numOfLine) + " squares in this figure."
#end drawNestedSquare


def drawKochSide(pen, n, l):
    
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        pen.forward(l)
        numOfLine += 1
        return "There is only " + str(numOfLine) + " line in this Koch Side."
    #end if

    drawKochSide(pen, n-1, l/3)
    pen.left(60)
    drawKochSide(pen, n-1, l/3)
    pen.right(120)
    drawKochSide(pen, n-1, l/3)
    pen.left(60)
    drawKochSide(pen, n-1, l/3)    

    return "There are " + str(numOfLine) + " lines in this Koch Side."
#end drawKochSide


def drawKoch(pen, n, l):
    
    for i in range(3):
        drawKochSide(pen, n, l)
        pen.right(120)
        
    return "There is only " + str(numOfLine) + " lines in this Koch ."
#end drawKoch


def drawQuadraticKochSide(pen, n, l):
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        pen.forward(l)
        numOfLine += 1
        return "There is only " + str(numOfLine) + " line in this Q-Koch Side."
    #end if

    drawQuadraticKochSide(pen, n-1, l/4)
    pen.left(90)
    drawQuadraticKochSide(pen, n-1, l/4)
    pen.right(90)
    drawQuadraticKochSide(pen, n-1, l/4)
    pen.right(90)
    drawQuadraticKochSide(pen, n-1, l/2)
    pen.left(90)
    drawQuadraticKochSide(pen, n-1, l/4)
    pen.left(90)
    drawQuadraticKochSide(pen, n-1, l/4)
    pen.right(90)
    drawQuadraticKochSide(pen, n-1, l/4)

    return "There are " + str(numOfLine) + " lines in this Q-Koch Side."
#end drawQuadraticKochSide


def drawQuadraticKoch(pen, n ,l):
    for i in range(4):
        drawQuadraticKochSide(pen, n, l)
        pen.right(90)
    #end for
    return "There are " + str(numOfLine) + " lines in this Q-Koch ."
#end drawQuadraticKoch
        

def drawSnowFlowerSide(pen, n, l):
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        pen.forward(l)
        numOfLine += 1
        return "There is only " + str(numOfLine) + " line in this Snow Flower Side."
    #end if

    drawSnowFlowerSide(pen, n-1, l/3)
    pen.left(90)
    drawSnowFlowerSide(pen, n-1, l/3)
    pen.right(90)
    drawSnowFlowerSide(pen, n-1, l/3)
    pen.right(90)
    drawSnowFlowerSide(pen, n-1, l/3)
    pen.left(90)
    drawSnowFlowerSide(pen, n-1, l/3)

    return "There are " + str(numOfLine) + " lines in this Snow Flower Side."
#end draw


def drawSnowFlower(pen, n, l):
    pen.begin_fill()
    for i in range(4):
        drawSnowFlowerSide(pen, n, l)
        pen.left(90)
    #end for
    pen.end_fill()
    
    if numOfLine == 4:
        return "There are " + str(numOfLine) + " lines in this figure. \nAdd more orders to draw a S-Flower."
        
    return "There are " + str(numOfLine) + " lines which construct " + str(numOfLine//4) + "\nsquares in this Snow Flower."
#end drawGalahadStar


def drawPaperCutSide(pen, n, l):
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        pen.forward(l)
        numOfLine += 1
        return "There is only " + str(numOfLine) + " line in this Paper Cut Side." + "\n add more orders to draw a P-Cut."
    #end if

    drawPaperCutSide(pen,n-1,l/2)
    pen.left(85)
    drawPaperCutSide(pen,n-1,l/2)
    pen.right(170)
    drawPaperCutSide(pen,n-1,l/2)
    pen.left(85)
    drawPaperCutSide(pen,n-1,l/2)

    return "There are " + str(numOfLine) + " lines in this Paper Cut Side."
#end drawCesaroSide



def drawPaperCut(pen, n, l):
    pen.begin_fill()
    for i in range(4):
        drawPaperCutSide(pen, n, l)
        pen.left(90)
    #end for
    pen.end_fill()

    if numOfLine == 4:
        return "There are " + str(numOfLine) + " lines with 1 square in this \nfigure. Add more orders to draw a P-Cut."
    
    return "There are " + str(numOfLine) + " lines in this Paper Cut."
#end drawPaperCut
        


def dCircle(pen, n, r):
    global numOfLine
    
    #termination:
    if n == 0 or r < 2:
        pen.circle(r)
        numOfLine += 1
        return "There is only " + str(numOfLine) + " circle."
    #end if

    #draw an outter circle
    pen.circle(r)

    #draw an inner under circle
    dCircle(pen,n-1,r/2)

    #draw an inner up circle
    pen.up()
    pen.left(90)
    pen.forward(r)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/2)

    #draw a right inner circle
    pen.up()
    pen.forward(2*r/3)
    pen.left(90)
    pen.backward(r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3)

    #draw a right inner under circle
    pen.up()
    pen.left(90)
    pen.backward(r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3/2)

    #draw a right inner up circle
    pen.up()
    pen.left(90)
    pen.forward(2*r/3/2 + 2*r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3/2)

    #draw a left inner circle
    pen.up()
    pen.left(90)
    pen.backward(r/3)
    pen.right(90)
    pen.backward(2*2*r/3)
    pen.left(90)
    pen.backward(r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3)

    #draw a left inner under circle
    pen.up()
    pen.left(90)
    pen.backward(r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3/2)

    #draw a left inner up circle
    pen.up()
    pen.left(90)
    pen.forward(2*r/3/2 + 2*r/3)
    pen.right(90)
    pen.down()
    dCircle(pen,n-1,r/3/2)

    #back
    pen.up()
    pen.left(90)
    pen.backward(r/3 + r)
    pen.right(90)
    pen.forward(2*r/3)
    pen.down()

    numOfLine+=1

    return "There are " + str(numOfLine) + " circles."
    
#end dCircle

def drawSierpinski(pen, n, l):
     global numOfLine
    
     #termination:
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l)
               pen.left(120)
               numOfLine += 1
          #end for
          return "There are " + str(numOfLine) + " lines."
     #end if

     for i in range(3):
          drawSierpinski(pen, n-1,l/2)
          pen.forward(l)
          pen.left(120)
     #end for
     return "There are " + str(numOfLine) + " lines."
#end drawSierpinski

def drawRectCarpet(pen,n,l):
    global numOfLine
    
    #termination:
    if n == 0 or l < 2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
            numOfLine += 1
        #end for
        return "There are " + str(numOfLine) + " lines."
    #end if

    for i in range(4):
        drawRectCarpet(pen,n-1,l/3)
        pen.forward(l)
        pen.left(90)
    #end for
    return "There are " + str(numOfLine) + " lines."
#end drawRectCarpet


def drawGasket(pen,n,l):
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        pen.up()
        pen.forward(l/2)
        pen.down()
        pen.circle(l/2)
        pen.up()
        pen.backward(l/2)
        pen.down()
        
        numOfLine += 1
        return "There is only " + str(numOfLine) + " circle in the gasket."
    #end if

    for i in range(4):
        pen.forward(l)
        pen.left(90)
    #end for
    
    pen.up()
    pen.forward(l/2)
    pen.down()
    pen.circle(l/2)
    pen.up()
    pen.backward(l/2)
    pen.down()
    
    drawGasket(pen,n-1,l/2)

    pen.up()
    pen.forward(l/2)
    pen.down()
    drawGasket(pen,n-1,l/2)

    pen.up()
    pen.left(90)
    pen.forward(l/2)
    pen.right(90)
    pen.down()
    drawGasket(pen,n-1,l/2)
    
    pen.up()
    pen.backward(l/2)
    pen.down()
    drawGasket(pen,n-1,l/2)

    pen.up()
    pen.left(90)
    pen.backward(l/2)
    pen.right(90)
    pen.down()

    numOfLine += 1
    return "There are " + str(numOfLine) + " circles in the gasket."
#end drawGasket


def drawGasket2(pen, n, l):
    
    global numOfLine
    
    #termination
    if n == 0 or l < 2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        pen.up()
        pen.forward(l/4)
        pen.down()
        pen.circle(l/4)
        
        pen.up()
        pen.forward(l/2)
        pen.down()
        pen.circle(l/4)

        pen.up()
        pen.left(90)
        pen.forward(l/2)
        pen.right(90)
        pen.down()
        pen.circle(l/4)

        pen.up()
        pen.backward(l/2)
        pen.down()
        pen.circle(l/4)

        pen.up()
        pen.forward(l/4)
        pen.left(90)
        pen.backward(l/10)
        pen.right(90)
        pen.down()
        pen.circle(l/10)

        pen.up()
        pen.backward(l/2)
        pen.left(90)
        pen.backward(l/2-l/10)
        pen.right(90)
        pen.down()
        
        numOfLine += 5
        return "There are " + str(numOfLine) + " circles in the gasket."
    #end if
    
    for i in range(4):
        pen.forward(l)
        pen.left(90)
    #end for
        
    pen.up()
    pen.forward(l/4)
    pen.down()
    pen.circle(l/4)
    
    pen.up()
    pen.forward(l/2)
    pen.down()
    pen.circle(l/4)

    pen.up()
    pen.left(90)
    pen.forward(l/2)
    pen.right(90)
    pen.down()
    pen.circle(l/4)

    pen.up()
    pen.backward(l/2)
    pen.down()
    pen.circle(l/4)

    pen.up()
    pen.forward(l/4)
    pen.left(90)
    pen.backward(l/10)
    pen.right(90)
    pen.down()
    pen.circle(l/10)

    pen.up()
    pen.backward(l/2)
    pen.left(90)
    pen.backward(l/2-l/10)
    pen.right(90)
    pen.down()

    
    drawGasket2(pen, n-1, l/2)

    pen.up()
    pen.forward(l/2)
    pen.down()
    drawGasket2(pen, n-1, l/2)

    pen.up()
    pen.left(90)
    pen.forward(l/2)
    pen.right(90)
    pen.down()
    drawGasket2(pen, n-1, l/2)

    pen.up()
    pen.backward(l/2)
    pen.down()
    drawGasket2(pen, n-1, l/2)

    pen.up()
    pen.left(90)
    pen.backward(l/2)
    pen.right(90)
    pen.down()

    numOfLine += 5
    return "There are " + str(numOfLine) + " circles in the gasket."
#end drawGasket2
    
    
    




    
    

    





    





    

            

    

    

    

