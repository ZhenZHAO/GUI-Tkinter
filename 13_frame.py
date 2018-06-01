import tkinter as tk
import sys


class MyGUI(object):
    def __init__(self, root):
        self.window = root
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self._gui_int()

    def quit(self):
        self.window.destroy()
        sys.exit()

    def _gui_int(self):
        i, i_row = 0, 0
        tk.Frame(self.window, bg='#080808', width=300, height=50, bd=2).grid(row=i_row, column=0, columnspan=3)
        for color in ['red', 'blue', 'yellow', 'green', 'white', 'black', '#900977', '#343434', '#199206']:
            i_row = i // 3 + 1
            i_col = i % 3
            tk.Frame(self.window, height=50, width=100, bg=color, bd=2).grid(row=i_row, column=i_col)
            i += 1

        status_bar = tk.Frame(self.window, bg='#080808', width=300, height=50, bd=2)
        status_bar.grid(row=i_row+1, column=0, columnspan=3)
        tk.Label(status_bar, text="Copyright \N{COPYRIGHT SIGN} 2018 Zhen ZHAO", bg='red', fg='white').pack(side='right', anchor='e')


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("How To Use Frame")
    center_window(root, 300, 250)
    my_gui = MyGUI(root)
    root.mainloop()
