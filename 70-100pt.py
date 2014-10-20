##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#house 
square = drawpad.create_rectangle(100,300,300,500, fill= 'red')
#roof
line1 = drawpad.create_line(200,200,300,300)
line2 = drawpad.create_line(200,200,100,300)

#windows
window1 = drawpad.create_rectangle(110,320,160,370, fill= 'white')
window2 = drawpad.create_rectangle(240,320,290,370, fill= 'white')
window3 = drawpad.create_rectangle(110,410,160,470, fill= 'white')
window4 = drawpad.create_rectangle(240,410,290,470, fill= 'white')

#door
door = drawpad.create_rectangle(170,410,230,500, fill= 'brown')

#doorhandle
doorhandle = drawpad.create_oval(220,450,230,460, fill= 'yellow')
#chimney
firstchmnyln = drawpad.create_line(250,200,280,200)
secondchmnyln = drawpad.create_line(250,200,250,250)
thirdchmnyln = drawpad.create_line(280,200,280,280)

#grass
grass = drawpad.create_rectangle(0,500,800,600, fill= 'green')

root.mainloop()




