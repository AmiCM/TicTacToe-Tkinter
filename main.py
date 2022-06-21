import tkinter as tk
from PIL import ImageTk
import settings
import utils

# Create Window
root = tk.Tk()
root.configure(bg=settings.BG_COLOUR)
root.title("Tic Tac Toe Game")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

##root.eval("tk::PlaceWindow . center")
##x = root.winfo_screenwidth() // 2
##y = int(root.winfo_screenheight() * 0.1)
##root.geometry('500x600+' + str(x) + '+' + str(y))

# Frames
top_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(20),
                     bg="red")
top_frame.place(x=0,y=0)

mid_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(20),
                     bg="blue")
mid_frame.place(x=0,y=utils.height_percentage(20))

low_frame = tk.Frame(root,
                     width=utils.width_percentage(100),
                     height=utils.height_percentage(60),
                     bg="green")
low_frame.place(x=0,y=utils.height_percentage(40))

# run app
root.mainloop()
