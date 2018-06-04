from tkinter import *


def test(master=None):
    main_w = LabelFrame(master,
                        text="Basic Info",
                        fg='red')
    main_w.pack()
    frm1 = Frame(main_w)
    frm1.pack(fill=X, side=TOP)
    frm2 = Frame(main_w)
    frm2.pack(fill=X, side=TOP)

    # 1. 第一个OptionMenu with attribute settings
    Label(frm1, text='Favorite: ').pack(side=LEFT, anchor='nw')
    v = StringVar()
    v.set("JavaScript")  # 注意这个值，几乎决定了OptionMenu的长度。小TICK：把初值设置为最长的
    om = OptionMenu(frm1,
                    v,
                    'Python',
                    'PHP',
                    'CPP',
                    'C',
                    'Java',
                    'JavaScript',
                    'VBScript'
                    )

    om.pack(side=LEFT, anchor='nw')

    # 2. 第一个OptionMenu initialized with list/tuple
    Label(frm2, text='County:').pack(side=LEFT, anchor='nw')
    option = ['China', "USA", "UK", "Canada", "Singapore"]
    var = StringVar()

    # 小trick，自动把初值设置为最长的项
    x = [len(y) for y in option]  # 先获得各项的长度
    init_value = option[x.index(max(x))]
    var.set(init_value)

    om2 = OptionMenu(frm2, var, *option)
    om2.pack(side=LEFT, anchor='nw')

    # 3. 显示/获取OptionMenu的值
    Label(master, textvariable=v, bg='black', fg='red').pack(fill=X, side=TOP, anchor='nw')
    Label(master, textvariable=var, bg='green', fg='red').pack(fill=X, side=TOP, anchor='nw')
    print("Favorite Programming Language is \"%s\"" % v.get())
    print("Come from '%s'" % var.get())


def test2(master=None):
    Lang = ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']
    v = StringVar(root)
    v.set('Tkinter')

    def printOption(event):
        print(v.get())

    # 创建一个OptionMenu控件,使用了apply函数
    # om = apply(OptionMenu, (root, v) + tuple(Lang))
    om = OptionMenu(master, v, *Lang)

    # 事件绑定 (少用)
    # 每次点击OptionMenu程序打印出上次选中的项值
    om.bind('<Button-1>', printOption)
    om.pack()

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("Use Option Menu")
    center_window(root, 300, 300)
    test(root)
    test2(root)
    root.mainloop()
