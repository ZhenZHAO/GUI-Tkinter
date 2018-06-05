from tkinter import *


def test(master=None):
    m1 = PanedWindow(master, showhandle=True, sashrelief=SUNKEN, handlepad=0, handlesize=2)
    m1.pack(fill=BOTH, expand=1)

    # 1. 最左边的插件
    left = Label(m1, text="left pane")
    m1.add(left)
    # 2. 中间的插件
    m1.add(Label(m1, text='middle pane'))
    # 3. 最右边的penal
    m2 = PanedWindow(m1, orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
    m1.add(m2)
    # 给右边penal添加组件
    top = Label(m2, text="top pane")
    m2.add(top)
    middle = PanedWindow(m2, orient=HORIZONTAL, showhandle=True)
    middle.add(Label(middle, text="middle-left", bg='red', fg='white'))
    middle.add(Label(middle, text="middle-right", bg='red', fg='white'))
    m2.add(middle)
    bottom = Label(m2, text="bottom pane")
    m2.add(bottom)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Paned window")
    center_window(root, 300, 300)
    test(root)
    root.mainloop()
