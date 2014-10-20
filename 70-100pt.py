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
window1 = drawpad.create_rectangle(120,320,170,370, fill= 'white')
window2 = drawpad.create_rectangle(230,320,280,370, fill= 'white')
window3 = drawpad.create_rectangle(120,410,170,460, fill= 'white')
window4 = drawpad.create_rectangle(230,410,280,460, fill= 'white')



root.mainloop()
