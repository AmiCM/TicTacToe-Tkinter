import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

# initialize app
root = tk.Tk()
root.title("Recipe Picker")
bg_colour="#3d6466"

def load_frame2():
    print("Hello Marya")

## root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

# Create a Frame Widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# Frame 1 Widgets
logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(
    frame1,
    text="Random Recipe",
    bg=bg_colour,
    fg="white",
    font=("TkMenuFont",14)
).pack()

# Button widget
tk.Button(
    frame1,
    text="shuffle",
    font=("TkHeadingFont",20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:load_frame2()
).pack(pady=20)


# run app
root.mainloop()
