from tkinter import *


def test1(master=None):
    w = Canvas(master, width=200, height=400, bg='grey')
    w.pack()
    # 1. 创建各种组件
    # 1.1 画线
    start = {'x': 0, 'y': 50}; end = {'x': 200, 'y': 50}
    line1 = w.create_line(start['x'], start['y'],
                          end['x'], end['y'],
                          fill='blue',
                          width=1,
                          capstyle=ROUND,
                          joinstyle=BEVEL,
                          )
    line_tmp = w.create_line(0, 0, 200, 200, fill='red')
    line2 = w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
    # 1.2 画矩形
    rect1 = w.create_rectangle(50, 25, 150, 75,
                               fill='yellow',  # 填充色
                               outline='hotpink',  # 边框色
                               width=2,  # 线宽
                               dash=(4, 10),  # 虚线框
                               )
    # 1.3 画椭圆
    circle1 = w.create_oval((10, 75, 190, 155), fill='#287393')
    # 1.3 画圆
    circle2 = w.create_oval((0, 0, 50, 50), fill='#9370DB')

    # 1.4 画多边形
    poly1 = w.create_polygon((50, 0, 0, 50, 25, 100, 75, 100, 100, 50), fill='red')

    # 1.5 添加文字
    txt = w.create_text((90, 110), text="Hello World")
    w.select_from(txt, 6)
    w.select_to(txt, 10)

    # 1.6 画弧线
    arc1 = w.create_arc((50,10,110,110),
                        fill='darkblue',
                        extent=30,
                        start=90,
                        outline='red')

    # 2. 创建的画布对象会一直存在，通过一下四个方法修改
    w.coords(line1, 0, 25, 200, 25)  # 用coords方法把对象移动到一个新的位置
    w.itemconfig(rect1, fill='green')  # 用itemconfig设置对象的选项
    w.move(circle2, 75, 25)  # 使用move方法移动该画布对象
    w.move(poly1, 50, 155)
    w.move(arc1, -50, 150)
    w.delete(line_tmp)  # 直接将对象的名字放进去就可以实现删除

    # ALL是一个tag，表示所有的对象
    # Button(master, text='删除全部对象', command=(lambda: w.delete(ALL))).pack()
    Button(master, text='删除全部对象', command=(lambda x=ALL: w.delete(x))).pack()

    # 3. 绑定对象，鼠标在画布上画画
    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, fill="red")

    w.bind("<B1-Motion>", paint)


def test2(master=None):
    pass


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Canvas")
    center_window(root, 300, 300)

    test1(root)
    test2(root)
    test3(root)

    root.mainloop()
