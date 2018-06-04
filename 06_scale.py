from tkinter import *


def test(master=None):
    frm1 = Frame(master)
    frm1.pack(anchor=W)
    frm2 = Frame(master)
    frm2.pack(anchor=W)

    def print_info(text):
        print(text)

    var = IntVar()
    Scale(frm1,
          from_=-200,  # 设置最大值
          to=200,  # 设置最小值
          resolution=5,  # 设置步距值
          bigincrement=50,  # 设置大增量
          orient=HORIZONTAL,  # 设置水平方向
          showvalue=True,  # （默认）设置显示值
          digit=5,  # 设置有效数字位数
          tickinterval=150,  # 设置刻度的间隔
          width=10,     # 设置scale的宽度
          length=300,   # 设置scale的长度
          sliderlength=20,  # 设置滑块的长度
          command=print_info,  # 设置回调函数，注意该回调函数必须要有一个参数
          label="X:",  # 设置scale的名称
          variable=var,  # 设置绑定变量
          ).pack()

    sc = Scale(frm1,
               from_=-10, to=10, resolution=2,
               orient=VERTICAL,
               bd=5,
               bg='grey',
               fg='red',
               troughcolor='blue',
               activebackground='black',
               relief=FLAT,  # scale的样式
               sliderrelief=RIDGE,  # 滑块的样式
               repeatdelay=50,  # 点击滚动条凹槽的响应时间
               repeatinterva=50,
               label="Y")
    sc.pack()
    sc.set(7)
    print(sc.get())

    def call_back():
        label_var.set(str(var.get())+"\t"+str(sc.get()))
    Button(frm2, text='click', command=call_back).pack()
    label_var = StringVar()
    Label(frm2, width=300, height=2, bg='black', fg='red', textvariable=label_var).pack()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Scale")
    center_window(root, 300, 300)
    test(root)
    root.mainloop()
