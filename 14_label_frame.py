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
        group = tk.LabelFrame(self.window, text="Where are you from:", fg='red', bd=20, relief=tk.RIDGE)  # bg='grey'
        group.pack(padx=10, pady=10)
        self.radio_lst = ['China', 'USA', 'Canada', 'UK']
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        for index in range(len(self.radio_lst)):
            tk.Radiobutton(group, text=self.radio_lst[index], variable=self.radio_var, value=index,
                           command=self.radio_call).pack(anchor='w')
        self.text_var = tk.StringVar()
        self.text_var.set(self.radio_lst[self.radio_var.get()])
        show_frame = tk.Frame(group)
        show_frame.pack(anchor='center')
        tk.Label(show_frame, textvariable=self.radio_var, bg='red', fg='white').grid(row=0, column=0)
        tk.Label(show_frame, textvariable=self.text_var, bg='black', fg='white').grid(row=0, column=1)

    def radio_call(self):
        self.text_var.set(self.radio_lst[self.radio_var.get()])


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Use Label Frame")
    center_window(root, 300, 200)
    my_gui = MyGUI(root)
    root.mainloop()
