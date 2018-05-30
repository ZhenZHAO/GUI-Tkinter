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
        # 1. set call back func
        tier_1 = tk.Frame(self.window, height=100)
        tier_2 = tk.Frame(self.window, height=100)
        tier_3 = tk.Frame(self.window, height=100)
        tier_1.pack(side='top')
        tier_2.pack(side='top')
        tier_3.pack(side='top')
        # different button relief
        # relief: flat, groove, raised, ridge, solid, or sunken
        # bitmap: error, info, question, warning, questhead, hourglass, gray12, gray25, gray50, gray75
        # compound: left, right, top, bottom, center
        self.btn_1 = tk.Button(tier_1,
                               text="say hi",
                               command=lambda: self.print_with("Hello, "),
                               bg="#080808",
                               fg='red',
                               padx=10,
                               pady=5,
                               bitmap='info',
                               compound='left',
                               relief=tk.FLAT)
        self.btn_1.pack(side=tk.LEFT)

        # set width, height
        # justify: left, right, top, bottom
        # wraplength: set length to auto-wrap
        # borderwidth(bd): by default, 1/2 pixel
        # anchor: 'n','s','e','w','ne','nw','se','sw',center
        self.btn_2 = tk.Button(tier_1,
                               text='say \nbye',
                               width=10,
                               height=3,
                               justify='left',
                               wraplength=10,
                               bd=10,
                               anchor='s',
                               command=lambda: self.print_with("Bye, ")
                               )
        self.btn_2.pack(side=tk.RIGHT)

        self.label = tk.Label(tier_2,
                              text="How are you doing?",
                              bitmap='questhead',
                              width=200,
                              height=50,
                              compound='left',)
        self.label.pack()
        self.output = tk.Text(tier_3, height=5)
        self.output.pack()

        # state: normal, active, disabled
        # tk.StringVar() to set the textvariable
        # bind()
        tier_4 = tk.Frame(self.window, height=20)
        tier_4.pack(side='top')

        self.btn_3 = tk.Button(tier_4, text='like', command=lambda: self.print_with("I like "), state='normal')
        self.btn_3.pack(side=tk.LEFT)
        self.btn_4 = tk.Button(tier_4, text='hate', command=lambda: self.print_with("I hate "), state='disabled')
        self.btn_4.pack(side=tk.LEFT)
        self.btn_var = tk.StringVar()
        self.btn_5 = tk.Button(tier_4, textvariable=self.btn_var)
        self.btn_var.set('~Like~')
        # self.btn_5.bind("<Enter>", self.change_text)
        self.btn_5.bind("<Return>", self.change_text)
        self.btn_5.pack(side=tk.LEFT)

    def change_text(self, event):
        # if self.btn_var.get() == 'click':
        if self.btn_5['text'] == '~Like~':
            self.btn_var.set('~Hate~')
        else:
            self.btn_var.set('~Like~')

    def print_with(self, _str):
        # print(str(_str), "world!")
        self.output.delete(0.0, tk.END)
        self.output.insert(0.0, str(_str) + " world")


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("How To Use Label")
    center_window(root, 300, 300)
    my_gui = MyGUI(root)
    root.mainloop()
