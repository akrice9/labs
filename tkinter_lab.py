from tkinter import *
window = Tk()
window.title("Stick Figure Drawing")
canvas = Canvas(window, width=300, height=300)
canvas.pack()
window.mainloop(30)

canvas.create_oval(125,25,175,75)#head
canvas.create_line(150,75,100,175)#skirt left
canvas.create_line(150,75,200,175)#skirt right
canvas.create_line(100,175,200,175)#skirt bottom
canvas.create_line(130,115,90,145)#arm left
canvas.create_line(170,115,210,145)#arm right
canvas.create_line(135,175,100,245)#left leg
canvas.create_line(165,175,200,245) #right leg
canvas.create_oval(135,40,143,48)#left eye
canvas.create_oval(165,40,157,48)#right eye
canvas.create_line(100,245,80,245)#left foot
canvas.create_line(200,245,220,245)#right foot
canvas.create_arc(140, 65, 160, 55, start=170, extent=200, style="chord") #mouth
canvas.create_oval(137,42,141,46, fill='black') #left pupil
canvas.create_oval(163,42,159,46, fill='black') #right pupil
canvas.create_line(150,48,150,54)#nose line
