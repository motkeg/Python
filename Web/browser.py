import webbrowser as browser

import turtle

def squre(t):
    for i in range(4):
        t.forward(150)
        t.right(90)
        
       
    
def drew():
    window= turtle.Screen()
    window.bgcolor("red")
        
    t=turtle.Turtle()
    t.shape("turtle")
    t.color("yellow")
    t.speed(2)
    
    for i in range(18):
        squre(t)
        t.right(20)
    
drew()    



#browser.open("https://www.youtube.com/watch?v=UbQR9dG1g-Y")
