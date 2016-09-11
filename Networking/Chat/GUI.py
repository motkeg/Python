from Tkinter import *
from server import * 




class MainGUI(): #main GUI
    def __init__(self):
        
        root = Tk()
        root.title("Chat Server")
        root.geometry("400x400")
      
        self.lbl= Label(root,text="Hello and Wellcom!" ,fg="red").pack()
        self.btn1=Button(root,text="start server",bg="red",fg="white",command=Main).pack(side=LEFT)
        self.btn2=Button(root,text="Stop server",bg="black",fg="white",command=Stop).pack(side=RIGHT)
        self.text = Text(root, state='disabled', width=44, height=5).pack()
        self.text.Insert(END,"Hello")
        
        root.mainloop()


main = MainGUI()