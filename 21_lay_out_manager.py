from tkinter import *


def test_pack(master=None):
    frm1 = Frame(master, bg='grey', height=100, width=200)
    frm1.pack(side='right', padx=20, anchor='ne')

    frm2 = Frame(master, bg='blue', height=100, width=200)
    frm2.pack(side='left', anchor='nw', ipadx=20, ipady=20)
    Label(frm2, text="Red", bg="red", fg="white").pack(fill=X, expand=True, padx=10)
    Label(frm2, text="Green", bg="green", fg="black").pack(fill=X, expand=True, pady=10)
    Label(frm2, text="Blue", bg="blue", fg="white").pack(fill=X)


def test_grid(master=None):
    Label(master, text="用户名").grid(row=0, sticky=W)
    Label(master, text="密码").grid(row=1, sticky=W)

    Entry(master).grid(row=0, column=1)
    Entry(master, show="*").grid(row=1, column=1)

    photo = PhotoImage(file="PICS/18.gif")
    lb = Label(master, image=photo)
    lb.image = photo
    lb.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

    Button(text="提交", width=10).grid(row=2, columnspan=3, pady=5)

    # 设置使得网格可伸缩
    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)
    master.grid_columnconfigure(2, weight=1)


def test_place(master=None):
    lb1 = Label(master, text='hello Place', bg='blue')
    btn1 = Button(master, text="Click me", bg='yellow')

    # 绝对坐标位置
    lb1.place(x=200, y=200, anchor=NW)
    # 相对坐标位置 relx, rely
    btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
    # 相对尺寸
    frm1 = Frame(master, bg='red')
    frm1.place(x=10, y=10, relheight=0.3, relwidth=0.3, anchor='nw')
    Label(frm1, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
    Label(frm1, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
    Label(frm1, bg="green").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)

    frm2 = Frame(master, bg='darkblue')
    frm2.place(x=300, y=300, relwidth=0.3, relheight=0.1, anchor='nw')
    lb2 = Label(frm2, text='hello world', fg='green')
    lb2.place(in_=frm2)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Layout Manager")
    height, width = 400, 400
    root.geometry("%dx%d+%d+%d" % (width, height,
                                   (root.winfo_screenwidth() - width) // 2,
                                   (root.winfo_screenheight() - height) // 2))

    # 如果父组件同时使用两种布局方法，那么程序会死循环出错
    # 例如在此次同时执行前两个test，那么程序永远不会结束
    # test_pack(root)
    # test_grid(root)
    test_place(root)

    root.mainloop()
