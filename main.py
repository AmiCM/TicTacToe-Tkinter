import tkinter as tk
from PIL import ImageTk
import settings
import utils
from Classes import *

# Create Window
root = tk.Tk()
root.configure(bg=settings.BG_COLOUR)
root.title("Tic Tac Toe Game")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

# Making Parent Frames
top_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(20),
                     bg=settings.BG_COLOUR)
top_frame.place(x=0,y=0)

title = tk.Label(top_frame,
                 text="Tic Tac Toe Game")
title.place(relx=0.5,rely=0.5,anchor="c")

mid_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(20),
                     bg=settings.BG_COLOUR)
mid_frame.place(x=0,y=utils.height_percentage(20))

Cell.make_turn_label(mid_frame)
Cell.turn_label.place(relx=0.5,rely=0.5,anchor="c")

low_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(60),
                     bg=settings.BG_COLOUR)
low_frame.place(x=0,y=utils.height_percentage(40))

low_center_frame = tk.Frame(low_frame,
                            width=120,
                            height=120,
                            bg=settings.BG_COLOUR)
low_center_frame.place(relx=0.5,rely=0.5,anchor="c")

for i in range(3):
    for j in range(3):
        c = Cell()
        c.make_button(low_center_frame)
        c.button.grid(column=i,row=j)

# run app
root.mainloop()
