from tkinter import *
#from tkinter.ttk import OptionMenu, Style
from turtle import *
from turtlefigures import *
from tkinter import messagebox
import datetime


#make a traffic between scorllbar and listbox
#Reference begins: 
class DebugScrollbar(Scrollbar):
    def set(self, *figures):

        Scrollbar.set(self, *figures)

class DebugListbox(Listbox):
    def yview(self, *figures):

        Listbox.yview(self, *figures)
#Reference ends
#Fredrik Lundh. (2003). Tkinter Scrollbar Patterns. Retrived from http://effbot.org/zone/tkinter-scrollbar-patterns.htm


figures = ["1. Tree","2. Fern","3. Flower","4. Snow Flower","5. Paper-Cut","6. Koch Side","7. Koch","8. Quadratic Koch Side","9. Quadratic Koch","10. Circular Gasket","11. Gasket Art One","12. Gasket Art Two","13. Spinning Nested Square", "14. Sierpinski Triangle","15. Rect Carpet"]

bgColour = ["White", "Gray", "LightGray", "AntiqueWhite", "Honeydew"]
bgColourValue = ["#fff","#808080", "#d3d3d3", "#faebd7", "#f0fff0"]

drawingColour = ["Black", "LightPink", "OrangeRed", "Olive", "LightSteelBlue"]
drawingColourValue = ["#000000", "#FFB6C1", "#FF4500", "#808000", "#B0C4DE"]

def changeBG(event):
    turtleScreen.bgcolor(bgColourValue[bgColour.index(bgDropDownStr.get())])
#end changeBG


def changeDrawingColour(event):
    turtle.color(drawingColourValue[drawingColour.index(drawingDropDownStr.get())])
#end changeDrawingColour

def changeSpeed(event):
    turtle.speed(speedValue.get())
#end changeSpeed

def clearInput():
    orderInput.set(0)
    lengthInput.set(0)
#end clearInput

def clearCanvas():

    turtle.reset()

    clearNumOfLine()
    
    labelText.set("")
#end clearCanvas

def screenshot():
    try:
        time = datetime.datetime.now()
        fileName = listbox.get(ANCHOR)+"-"+str(time.year)+"-"+str(time.month)+"-"+str(time.day)+"_"+str(time.hour)+":"+str(time.minute)+":"+str(time.second)
        
        screen = turtle.getscreen()
        psFile = screen.getcanvas().postscript(file="ScreenShot/"+fileName)

        messagebox.showinfo("Screen Shot Saved", "Screen Shot saved in the ScreenShot folder", parent = root)
    except:
        messagebox.showwarning("Sorry", "The screen shot is not saved", parent = root)

        
#end screenshot
    

    

def draw():

    turtle.speed(speedValue.get())
    turtle.color(drawingColourValue[drawingColour.index(drawingDropDownStr.get())])
    
    try:
        order = orderInput.get()
    except:
        messagebox.showwarning("Warning", "Invalid Order Input \n\nPlease enter a number in the Order", parent = root)
        return

    try:
        length = lengthInput.get()
    except:
        messagebox.showwarning("Warning", "Invalid Length Input \n\nPlease enter a number in the Length", parent = root)
        return

    if order < 0:
        messagebox.showwarning("Warning", "Invalid Order Input \n\nPlease enter a postive order number", parent = root)
        return

    if length < 0:
        messagebox.showwarning("Warning", "Invalid Length Input \n\nPlease enter a postive length number", parent = root)
        return

    if length == 0:
        messagebox.showwarning("Warning", "Invalid Length Input \n\nPlease enter a length number (not 0)", parent = root)
        return


    select = listbox.get(ANCHOR)
    
    if select == "":
        
        messagebox.showwarning("Warning", "Please select a figure to draw", parent = root)
        
    elif select == "1. Tree":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.sety(-250)
        turtle.left(90)
        turtle.down()
        
        labelText.set(drawTree(turtle, order, length))

    elif select == "2. Fern":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-250)
        turtle.sety(-250)
        turtle.left(45)
        turtle.down()

        labelText.set(drawFern(turtle, order, length))

    elif select == "3. Flower":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.sety(-250)
        turtle.left(90)
        turtle.down()

        labelText.set(drawFlower(turtle, order, length))
        
        
    elif select == "4. Snow Flower":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-150)
        turtle.sety(-150)
        turtle.down()

        labelText.set(drawSnowFlower(turtle, order, length))

    elif select == "5. Paper-Cut":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-150)
        turtle.sety(-150)
        turtle.down()

        labelText.set(drawPaperCut(turtle, order, length))
        
    elif select == "6. Koch Side":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.down()
        
        labelText.set(drawKochSide(turtle, order, length))

    elif select == "7. Koch":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.down()

        labelText.set(drawKoch(turtle, order, length))
        
    elif select == "8. Quadratic Koch Side":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.sety(100)
        turtle.down()

        labelText.set(drawQuadraticKochSide(turtle, order, length))

    elif select == "9. Quadratic Koch":

        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.sety(100)
        turtle.down()

        labelText.set(drawQuadraticKoch(turtle, order, length))
        
    elif select == "10. Circular Gasket":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.sety(-200)
        turtle.down()
        
        labelText.set(dCircle(turtle, order, length))
        
    elif select == "11. Gasket Art One":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-150)
        turtle.sety(-150)
        turtle.down()
        
        labelText.set(drawGasket(turtle, order, length))
        
    elif select == "12. Gasket Art Two":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-150)
        turtle.sety(-150)
        turtle.down()
        
        labelText.set(drawGasket2(turtle, order, length))
        
    elif select == "13. Spinning Nested Square":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-150)
        turtle.sety(-150)
        turtle.down()
        
        labelText.set(drawNestedSquare(turtle, order, length))

    elif select == "14. Sierpinski Triangle":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.sety(-100)
        turtle.down()
        
        labelText.set(drawSierpinski(turtle, order, length))

    elif select == "15. Rect Carpet":
        
        #set the begin point of the turtle and some attribures of it
        turtle.up()
        turtle.setx(-100)
        turtle.sety(-100)
        turtle.down()
        
        labelText.set(drawRectCarpet(turtle, order, length))
        
#end draw
        
    

#make UI frame
root = Tk()
root.geometry("703x505")
root.resizable(width = False, height = False)
root.title("Let's draw!")

##make UI widgets
#make canvas, turtle window and turtle
canvas = Canvas(root, width = 500, height = 500, highlightbackground = "black", highlightthickness = 3)
turtleScreen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.speed(0)
canvas.grid(row = 0, rowspan = 3, column = 0)

#make listBox
scrollbar = Scrollbar(root)
scrollbar.grid(row = 0, column = 2, sticky=N+S)

listbox = Listbox(root, width = 20, exportselection=False, relief=SUNKEN, font= "System", yscrollcommand=scrollbar.set)
listbox.grid(row = 0, column = 1)

scrollbar.config(command=listbox.yview)

for elem in figures:
    listbox.insert(END, elem)
#end for

#make frames(Operation Panel, entryFrame, setting frame, buttons frame) and Layouts
operationPanel = Frame(root, relief=SUNKEN, borderwidth = 1, width = 197, height = 335)
operationPanel.grid(row = 1, rowspan = 2, column = 1,columnspan = 2, sticky = W)
operationPanel.grid_propagate(0)

figureOLLabel = Label(operationPanel, text = "Figure Setting", font= "Verdana 9 underline", pady = 7)
figureOLLabel.grid(row = 0, column = 0, sticky = W)

entryFrame = Frame(operationPanel,width = 197,height = 47)
entryFrame.grid(row = 1, column = 0, columnspan = 10)
entryFrame.grid_propagate(0)

canvasSettingLabel = Label(operationPanel, text = "Canvas & Drawing Setting", font= "Verdana 9 underline", pady = 7)
canvasSettingLabel.grid(row = 2, column = 0, sticky = W)

settingFrame = Frame(operationPanel)
settingFrame.grid(row = 3, column = 0, columnspan = 10)

buttonLabel = Label(operationPanel, text = "Operation", font= "Verdana 9 underline", pady = 7)
buttonLabel.grid(row = 4, column = 0, sticky = W)

buttonContainer = Frame(operationPanel)
buttonContainer.grid(row = 5, column = 0, columnspan = 10)

infoLabel = Label(operationPanel, text = "Figure Info", font= "Verdana 9 underline")
infoLabel.grid(row = 6, column = 0, sticky = W)

infoFrame = Frame(operationPanel, relief=SUNKEN, borderwidth = 1, width = 192, height = 35)
infoFrame.grid(row = 7, column = 0, columnspan = 10)
infoFrame.grid_propagate(0)

#make labels
orderLabel = Label(entryFrame, text = "Order", font= "Verdana 11 ")
lengthLabel = Label(entryFrame, text = "Length", font= "Verdana 11 ")

bgLabel = Label(settingFrame, text = "Canvas Colour", font= "Verdana 11 ")
drawingLabel = Label(settingFrame, text = "Drawing Colour", font= "Verdana 11 ")

speedLabel = Label(settingFrame, text = "Drawing Speed", font= "Verdana 11 ")


orderLabel.grid(row = 0, column = 0, sticky = W)
lengthLabel.grid(row = 1, column = 0, sticky = W)

bgLabel.grid(row = 0, column = 0, sticky = W)
drawingLabel.grid(row = 1, column = 0, sticky = W)

speedLabel.grid(row = 2, column = 0, sticky = W)

labelText = StringVar()
figureInfo = Label(infoFrame, textvariable=labelText, font= ("Comic Sans MS", 9))
figureInfo.grid(row = 0, column = 0)

#make entries
orderInput = IntVar()
lengthInput = IntVar()
orderEntry = Entry(entryFrame, width = 14, textvariable = orderInput, relief=RAISED, highlightthickness=0)
lengthEntry = Entry(entryFrame, width = 14, textvariable = lengthInput, relief=RAISED, highlightthickness=0)

orderEntry.grid(row = 0, column = 1, sticky=E)
lengthEntry.grid(row = 1, column = 1, sticky=E)


#make aoption menu
bgDropDownStr = StringVar()
bgDropDownStr.set(bgColour[0])
bgDropDown = OptionMenu(settingFrame, bgDropDownStr, *bgColour, command=changeBG)
bgDropDown.config(width = 8, font= "Verdana 8 ")
bgDropDown.grid(row = 0, column = 1)

drawingDropDownStr = StringVar()
drawingDropDownStr.set(drawingColour[0])
drawingDropDown = OptionMenu(settingFrame, drawingDropDownStr, *drawingColour, command=changeDrawingColour)
drawingDropDown.config(width = 8, font= "Verdana 8 ")
drawingDropDown.grid(row = 1, column = 1)

speedValue = IntVar()
speedScale = Scale(settingFrame, width = 8, from_= 11 , to = 1, orient=HORIZONTAL, length = 120, variable = speedValue, resolution=1, showvalue=0, command=changeSpeed, font= "Verdana 8 ", label="Fastest                Slowest")
speedScale.grid(row = 3, column = 0, columnspan = 2)

#make buttons
drawButton = Button(buttonContainer, text = "Draw", command=draw, width = 10, font= "Verdana 10 ")
screenShotButton = Button(buttonContainer, text="Screen Shot", command=screenshot, width = 10, font= "Verdana 10 ")
clearInputButton = Button(buttonContainer, text="Clear Input", command=clearInput, width = 10, font= "Verdana 10 ")
clearCanvasButton = Button(buttonContainer, text="Clear Canvas", command=clearCanvas, width = 10, font= "Verdana 10 ")


drawButton.grid(row = 0, column = 0)
screenShotButton.grid(row = 0, column = 1)
clearInputButton.grid(row = 1, column = 0, pady = 5, padx = 3)
clearCanvasButton.grid(row = 1, column = 1)





root.mainloop()



