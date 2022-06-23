import tkinter as tk
import utils

class Cell:

    state = 'x'
    turn_label = None

    def __init__(self):
        self.button = None
        self.state = None

    def make_button(self, location):
        button = tk.Button(
        location,
        text='',
        width=5,
        height=5,
        command=self.change_state
        )
        self.button = button

    def change_state(self):
        if self.state is None:
            self.button.config(text=f'{Cell.state}')
            self.state = Cell.state
            self.change_turn()

    @classmethod
    def change_turn(cls):
        if cls.state == 'x':
            cls.state = 'o'
        else:
            cls.state = 'x'
        cls.turn_label.config(text=f'Turn: {cls.state}')

    @classmethod
    def make_turn_label(cls, location):
        if cls.turn_label is None:
            label = tk.Label(location,
                             text=f'Turn: x')
            cls.turn_label = label
