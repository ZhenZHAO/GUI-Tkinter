from tkinter import *


# 鼠标
def test1(master=None):
    global color, line_width
    color = 'green'
    line_width = IntVar()
    line_width.set(2)

    # 1. canvas and event bind
    def call_back(event):
        point_w = line_width.get()
        can1.create_oval((event.x - point_w, event.y - point_w, event.x + point_w, event.y + point_w),
                         fill=color, width=0)

    def clean_all(event):
        can1.delete(ALL)

    can1 = Canvas(master, bg='grey', height=300, width=400)
    can1.pack()
    can1.bind('<B1-Motion>', call_back)
    can1.bind('<Button - 2>', clean_all)

    # 2. set up format
    frm = LabelFrame(master, bg='#A0EEEE', text="Format")
    frm.pack()
    def change_color(clr):
        global color
        color = clr
    m1 = PanedWindow(frm, showhandle=True, sashrelief=SUNKEN, handlepad=0, handlesize=2)
    m1.pack(fill=BOTH, expand=1)
    # left - color
    in_frm = Frame(m1)
    m1.add(in_frm)
    Button(in_frm, text='DarkBlue', command=lambda: change_color('darkblue')).pack(side="left")
    Button(in_frm, text='HotPink', command=lambda: change_color('HotPink')).pack(side="left")
    Button(in_frm, text='Turquoise', command=lambda: change_color('Turquoise')).pack(side="left")
    # right - width
    m1.add(Scale(frm, from_=1, to=8, resolution=2, label="linewidth", variable=line_width))


# 按键
def test2(master=None):
    def callback(event):
        print(event.char)  # 获取当前键盘按下的字符

    frame = Frame(master, width=200, height=200, bg='red')
    frame.bind("<Key>", callback)  # 组件想要响应键盘事件，组件必须获得焦点，组件才会响应键盘来的消息。因为一个窗口可以有很多组件，键盘一次敲击不知道给哪个组件。
    frame.focus_set()  # 通过focus_set方法获得焦点。也可以设置Frame的takefocus选项为True，然后使用Tab将焦点转移上来
    frame.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Event and Bind")
    height, width = 400, 400
    root.geometry("%dx%d+%d+%d" % (width, height,
                                   (root.winfo_screenwidth() - width) // 2,
                                   (root.winfo_screenheight() - height) // 2))

    test1(root)
    test2(root)
    root.mainloop()

