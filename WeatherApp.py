import tkinter as tk
from tkinter.constants import BOTH

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack

frame = tk.frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidht=0.8, relheight=0.5)

button = tk.Button(frame, text="Test button", bg = 'gray')
button.place(relx=0, rely=0, relwidht=0.25, relheight=0.25)
#button.grid(row=0, column=0)
#button.pack(side='left', fill='both') aotherway

label = tk.Label(frame, text="This is a label", bg='yellow')
label.place(relx=0.3, rely=0, relwidht=0.45, relheight=0.25)

entry = tk.Entry(frame, bg='green')
entry.place(relx=0.8, rely=0.1, relwidht=0.2, relheight=0.25)
root.mainloop()

