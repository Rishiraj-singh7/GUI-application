import tkinter as tk
from tkinter.constants import ANCHOR, BOTH

HEIGHT = 500
WIDTH = 600

def test_function():
    print("This is the entry:", entry)

#138dd139ed444a6fc62fa8610d1a22ea

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_image = tk.Lable(root, image=background_image)
background_image.pack(relwidth=1, relheight=1)

frame = tk.frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidht=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place( relwidht=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: test_function(entry.get))
button.place(relx=0.7, relwidht=0.3, relheight=1)
#button.grid(row=0, column=0)
#button.pack(side='left', fill='both') aotherway

lower_frame = tk.Frame(root,bg='#80c1ff',bd=10 )
lower_frame.place(relx=0.5, rely=0.25, relwidht=0.75, relheight=0.6 anchor= 'n')

label = tk.Label(lower_frame)
label.place( relwidht=1, relheight=1)

root.mainloop()

