from tkinter import *


def test1(master=None):
    def callback():
        print("Hello world")

    # 1. 创建一个顶级菜单
    menubar = Menu(master)
    master.config(menu=menubar)

    # # 2. 创建二个普通菜单 (no good)
    # https://stackoverflow.com/questions/16847584/how-do-i-get-the-mac-command-symbol-in-a-tkinter-menu
    # menubar.add_command(label="Hello", command=callback,  accelerator="F5")
    # menubar.add_command(label="Quit", command=root.quit,  accelerator="Escape")

    # 2. 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
    filemenu = Menu(menubar, tearoff=True)
    filemenu.add_command(label="打开", command=callback, accelerator="Escape")
    filemenu.add_command(label="保存", command=callback, accelerator='Cmd-S')
    # accelerator='Command-P',# Cmd-p
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=master.quit)
    menubar.add_cascade(label="文件", menu=filemenu)

    # 3. 创建另一个下拉菜单“编辑”，然后给该菜单再添加一个子菜单
    editmenu = Menu(menubar, tearoff=False)
    editmenu.add_command(label="剪切", command=callback)
    editmenu.add_command(label="拷贝", command=callback)
    editmenu.add_command(label="粘贴", command=callback)
    menubar.add_cascade(label="编辑", menu=editmenu)
    editmenu.add_separator()
    helpmenu = Menu(editmenu, tearoff=False)
    helpmenu.add_command(label='Help', command=callback)
    helpmenu.add_command(label='Hello', command=callback)
    editmenu.add_cascade(label='WTF', menu=helpmenu)

    # 4. 显示菜单
    # master.config(menu=menubar)

    # 5. 创建一个弹出菜单
    pop_menu = Menu(master, tearoff=False, bg='grey')
    pop_menu.add_command(label="撤销", command=callback)
    pop_menu.add_command(label="重做", command=callback)

    frame = Frame(master, width=512, height=512, bg='blue')
    frame.pack()

    # 设置事件，并绑定鼠标右键
    def popup(event):
        pop_menu.post(event.x_root, event.y_root)

    frame.bind("<Button-2>", popup)
    # master.bind("<Button-2>", popup)


def test2(master=None):
    def call_back(contents):
        print(contents)

    # 1. define the top menu
    menuroot = Menu(master)
    master['menu'] = menuroot
    # 2. define a cascaded menu
    menusp = Menu(menuroot)
    menuroot.add_cascade(label='lang', menu=menusp)
    # add radio button
    radio_var = StringVar()
    for x in ['linux', 'unix', 'opoos']:
        menusp.add_radiobutton(label=x, variable=radio_var, command=lambda: call_back(radio_var.get()))
    menusp.add_separator()
    # add check button

    def check_call():
        select = [var.get() for var in check_dic.values()]
        lst = [x for x, y in zip(check_dic.keys(), select) if y is True]
        print(lst)

    lst = ['python', 'c++', 'vb', 'php']
    check_dic = dict.fromkeys(lst)
    for x in lst:
        check_dic[x] = BooleanVar()
        menusp.add_checkbutton(label=x, variable=check_dic[x], command=check_call)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Menu")
    center_window(root, 300, 300)
    # test1(root)
    test2(root)
    root.mainloop()


