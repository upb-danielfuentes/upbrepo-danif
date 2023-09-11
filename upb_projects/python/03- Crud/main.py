from tkinter import *

Windows = Tk()
Windows.title("Proyecto UNO")
ancho=1024
alto=768
x_windows = Windows.winfo_screenwidth() // 2 - ancho //2
y_windows = Windows.winfo_screenheight() // 2 - alto //2
tamano = str(ancho)+"x"+str(alto)+"+"+str(x_windows)+"+"+str(y_windows)
Windows.geometry(tamano)
Windows.mainloop()
