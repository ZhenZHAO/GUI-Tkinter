import tkinter as tk
import numpy as np
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
        # check button 1
        info_label_1 = tk.Label(self.window, text='Choose your Script Language:', bg='green', fg='red')
        info_label_1.pack(anchor='w')

        self.check_var = []
        for lang in ['Python', 'Ruby', 'Perl', 'Lua']:
            self.check_var.append(tk.IntVar())
            tk.Checkbutton(self.window, text=lang, variable=self.check_var[-1], command=self.check_call).pack(anchor='w', padx=20)

        self.text_1 = tk.Text(self.window, height=2)
        self.text_1.pack(anchor='w')

        # check button 2
        tk.Label(self.window, text='Choose your Compiling Language:', bg='yellow', fg='red').pack(anchor='w')

        check_item = ['C', 'C++', 'C#', 'Java']
        self.check_dict = dict().fromkeys(check_item)
        for lang in check_item:
            self.check_dict[lang] = tk.BooleanVar()
            tk.Checkbutton(self.window, text=lang, variable=self.check_dict[lang],
                           onvalue='True', offvalue='False').pack(anchor='w', padx=20)
        tk.Button(self.window, text="show", command=self.show_choice).pack(anchor='w')
        self.text_2 = tk.Text(self.window, height=2)
        self.text_2.pack()

        # radio button
        tk.Label(self.window, text='Choose your favorite country:', bg='green', fg='red').pack(anchor='w')
        self.radio_lst = ['China', 'USA', 'Canada', 'UK']
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        for index in range(len(self.radio_lst)):
            tk.Radiobutton(self.window, text=self.radio_lst[index], variable=self.radio_var, value=index, command=self.radio_call).pack(anchor='w')
        # for index in range(len(self.radio_lst)):
        #     tk.Radiobutton(self.window,
        #                    text=self.radio_lst[index],
        #                    variable=self.radio_var,
        #                    value=index,
        #                    indicatoron=False).pack(anchor='w')

        self.text_var = tk.StringVar()
        self.text_var.set(self.radio_lst[self.radio_var.get()])
        show_frame = tk.Frame(self.window)
        show_frame.pack(anchor='center')
        tk.Label(show_frame, textvariable=self.radio_var, bg='red', fg='white').grid(row=0, column=0)
        tk.Label(show_frame, textvariable=self.text_var, bg='black', fg='white').grid(row=0, column=1)


    def radio_call(self):
        self.text_var.set(self.radio_lst[self.radio_var.get()])

    def show_choice(self):
        self.text_2.delete(0.0, tk.END)
        bool_lst = [x.get() for x in self.check_dict.values()]

        # 获取选择的内容，方法1
        bool_lst_1 = np.array(bool_lst)
        choose_lst_1 = np.array(list(self.check_dict.keys()))
        info = 'you have chose:' + str(choose_lst_1[bool_lst_1])

        # 获取选择的内容，方法2
        # option_lst = self.check_dict.keys()
        # choose_lst_2 = [x for x, y in zip(option_lst, bool_lst) if y==True]
        # info = 'you have chose:' + str(choose_lst_2)

        self.text_2.insert(0.0, info)

    def check_call(self):
        self.text_1.delete(0.0, tk.END)
        info = [x.get() for x in self.check_var]
        self.text_1.insert(0.0, str(info))


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Use Check and Radio button")
    center_window(root, 500, 500)
    my_gui = MyGUI(root)
    root.mainloop()
