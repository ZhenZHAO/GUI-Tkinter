from tkinter import *


def test1(master=None):
    # index的使用方法

    text = Text(master)
    text.pack()

    # 行号以 1 开始，列号则以 0 开始
    text.insert(INSERT, "Hello world")
    print(text.get("1.2", 1.6))

    tmp_str = "\n\nI love china, I love python\n\n"
    text.insert(INSERT, tmp_str)
    print(text.get(3.2, "3.end"))

    text.insert(INSERT, tmp_str[::-1])
    text.insert(INSERT, tmp_str)
    lst = list(tmp_str); lst.reverse()
    text.insert(INSERT, str(lst))

    # line.col (line从1开始，col从0开始)
    text.tag_config('a', foreground='red')
    text.insert("%d.%d" % (2, 0), 'ABCDEFGHIJ', 'a')

    text.tag_config('b', foreground='green')
    text.insert("4.end", 'ABCDEFGHIJ', 'b')

    text.tag_config('c', foreground='blue')
    text.insert(END, 'ABCDEFGHIJ', 'c')



def test2(master=None):
    # text 中可以插入 文本，组件， 图片

    text = Text(master, width=30, height=50)
    text.pack()
    # 1. 插入文本
    text.insert(INSERT, "hello world.")
    text.insert(END, "Go for it.")
    # 2. 插入图像
    photo_img = PhotoImage(file='PICS/bg.gif')

    # 3. 插入组件
    def show():
        print("hey, python!")
        text.image_create(END, image=photo_img)
    bnt1 = Button(text, text="click", command=show)
    text.window_create(INSERT, window=bnt1)

    # 4. 获取/删除 TEXT组件内容
    def clear_all():
        print('INPUT:')
        print(text.get(1.0, END))
        print("\nNOTE: all the content will be deleted.")
        text.delete(0.0, END)
    bnt2 = Button(text, text="clear", command=clear_all)
    text.window_create(0.0, window=bnt2)


def test3(master=None):
    # 通过校检 Text 组件中文本的 MD5 摘要来判断内容是否发生改变：
    import hashlib
    text = Text(master, width=20, height=5)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")
    contents = text.get(1.0, END)

    def getSig(contents):
        m = hashlib.md5(contents.encode())
        return m.digest()

    global sig
    sig = getSig(contents)

    def check():
        contents = text.get(1.0, END)
        global sig
        if sig != getSig(contents):
            print("警报：内容发生变动！")
            label_var.set("sth changed!")
            # sig = getSig(contents)
        else:
            print("风平浪静~")
            label_var.set("Nothing changed!")

    label_var = StringVar()
    Button(master, text="检查", command=check).pack()
    Label(master, bg='black', fg='red', textvariable=label_var).pack()


def test4(master=None):
    pass


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Text")
    center_window(root, 300, 300)

    test1(root)
    # test2(root)
    # test3(root)
    # test4(root)

    root.mainloop()
