#!/usr/bin/env python3

""" Brief
Description
"""

import tkinter as tk

class App(object):
    """ Brief
    Description
    """

    def __init__(self, master=None):
        self._menu_widget = tk.Frame(master)
        self._menu_widget.pack()

        self._open_button = tk.Button(self._menu_widget)
        self._open_button["text"] = "File"
        self._open_button["font"] = ("Ubuntu", "10")
        self._open_button.pack()

root = tk.Tk()
App(root)
root.mainloop()
