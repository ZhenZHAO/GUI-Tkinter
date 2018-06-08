from tkinter import *
import random

win_number = 1


def test(master=None):
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    def call_back():
        global win_number
        tp_tmp = Toplevel(master)
        tp_tmp.title("No.%d Window" % win_number)
        win_number += 1
        size = '%dx%d+%d+%d' % (300, 100,
                                (screenwidth - random.randint(50, 1000)) // 2,
                                (screenheight - random.randint(50, 1000)) // 2 - 20)
        tp_tmp.geometry(size)
        color = '#%d%d%d' % (random.randint(10, 99), random.randint(10, 99), random.randint(10, 99))
        Label(tp_tmp, text='Hello world', bg=color, fg='black').pack()

    Button(master, text="Create New Window", bg='black', fg='red', command=call_back).pack()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Top Level")
    center_window(root, 300, 300)
    test(root)
    root.mainloop()
