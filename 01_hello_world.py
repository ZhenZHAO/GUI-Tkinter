import tkinter as tk
import sys


# 1. oop
class MyGUI(object):
    def __init__(self, root):
        self.window = root
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self._init_gui()

    def quit(self):
        self.window.destroy()
        print("Bye Bye")
        sys.exit()

    def _init_gui(self):
        frame_upper = tk.Frame(self.window)
        frame_upper.pack(padx=10, pady=10)
        frame_lower = tk.Frame(self.window)
        frame_lower.pack(padx=10, pady=10)

        self.label1 = tk.Label(frame_upper, text="Hello world.....", fg='blue')
        self.label1.pack(side=tk.LEFT)

        self.textVar = tk.StringVar()
        self.textVar.set("Hello ?")
        self.label2 = tk.Label(frame_upper, textvariable=self.textVar, bg='#FFC0CB', fg='white')
        self.label2.pack()

        self.button = tk.Button(frame_lower, text="click me", command=self.change_text)
        self.switch = True
        self.button.pack()

    def change_text(self):
        if self.switch:
            self.textVar.set("Go for it!")
            # self.button['text'] = 'what'
            self.button.config(text='what')
            self.switch = False
        else:
            self.textVar.set("Hello?")
            self.button['text'] = 'click me'
            self.switch = True


def test():
    root = tk.Tk()
    root.title("Hello world~")
    center_window(root, 200, 100)
    limit_window_size(root, (300, 300), (200, 100))
    # root.iconbitmap('hello.ico')
    # root.iconbitmap('PICS/18.gif')
    # root.iconphoto(True, tk.PhotoImage(file=os.path.join(sys.path[0], "avatar.png")))
    # img = tk.PhotoImage(file='PICS/18.gif')
    # root.tk.call('wm', 'iconphoto', root._w, img)
    my_gui = MyGUI(root)
    root.mainloop()


# 2. process-based
def main(root):
    root = tk.Tk()
    root.title("Hello world~")
    center_window(root, 200, 200)
    label1 = tk.Label(root, text="Hey you~")
    label1.pack()

    root.mainloop()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


def limit_window_size(root, vec_max, vec_min):
    root.maxsize(vec_max[0], vec_max[1])
    root.minsize(vec_min[0], vec_min[1])


if __name__ == "__main__":
    # 面向过程
    # main()

    # oop
    test()
