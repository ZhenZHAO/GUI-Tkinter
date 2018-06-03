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
        frm1 = tk.Frame(self.window)
        frm1.pack(anchor='w')
        frm2 = tk.Frame(self.window)
        frm2.pack(anchor='w')
        frm3 = tk.Frame(self.window)
        frm3.pack(anchor='w')
        # 1. spinbox 的基本用法
        def call_back():  # 当上下的按钮被触发的时候调用
            print(spb.get())
        spb = tk.Spinbox(frm1, bg='red', fg='white',
                         from_=20, to=30, increment=2, command=call_back)
        spb.pack(side=tk.RIGHT)
        spb['text'] = '25'
        tk.Label(frm1, text="Age:", justify='right',
                 anchor='e', width=10, bg='grey').pack(side=tk.LEFT)

        values_in = ('perl', 'python', 'ruby', 'lua')

        # 2. 输入验证
        def validate_input(contents):
            # print(contents)
            return contents in values_in
        validate_cmd = self.window.register(validate_input)

        def invalidate_input():
            # method 1
            spb2.delete(0, tk.END)
            print(spb2['validate'])

            # method 2
            # var.set('python')
            # print(spb2['validate'])
            # spb2['validate']='focusout'

        var = tk.StringVar()
        spb2 = tk.Spinbox(frm2, bg='red', fg='white',
                          wrap=True,
                          value=values_in,
                          textvariable=var,
                          validate='focusout',
                          validatecommand=(validate_cmd, '%P'),
                          invalidcommand=invalidate_input)
        spb2.pack(side=tk.RIGHT)
        var.set("python")
        tk.Label(frm2, text="Party:", justify='right', anchor='e', width=10, bg='grey').pack(side=tk.LEFT)
        def show_info():
            info = "age: " + spb.get()
            info += '\nSupport:' + var.get()
            t1.delete(0.0, tk.END)
            t1.insert(0.0, info)

        tk.Button(frm3, bg='green', text='show info', command=show_info).pack(anchor='nw')
        t1 = tk.Text(frm3, width=100, height=3, bg='black', fg='red')
        t1.pack(anchor='nw')

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Use SpinBox")
    center_window(root, 300, 300)
    my_gui = MyGUI(root)
    root.mainloop()

