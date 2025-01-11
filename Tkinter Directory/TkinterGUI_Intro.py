from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("600x500") # height and width of GUI
window.title("Tkinter GUI") # GUI Title

# Error in setting a photo
# icon = PhotoImage(file='images/icon.jpg')  # icon of GUI
# window.iconphoto(True, icon)    # set icon of the Gui
window.config(background="black")       # Set background of GUI

window.mainloop()   # Place window on computer screen. Listen for events
