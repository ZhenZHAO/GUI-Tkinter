from tkinter import *
import sys

def test1(root=None):
    def call_me():
        label['text'] = e.get() + entry2.get()
        # print(entry.get())

    def clear_all():
        entry1.delete(0, END)
        entry2.delete(0, END)
        label['text'] = ''

    e = StringVar()
    entry1 = Entry(root,
                   textvariable=e,
                   justify='center',
                   insertbackground='red',
                   insertontime=200,
                   insertofftime=200,
                   highlightcolor='red',
                   highlightbackground='black',
                   highlightthickness=4,
                   selectbackground='red',
                   selectforeground='white')
    e.set('input your text here')
    entry1.pack()

    entry2 = Entry(root, show='!*!')
    entry2.pack()

    Button(root, width=5, height=2, command=call_me, text='show').pack()
    Button(root, width=5, height=2, command=clear_all, text='clear').pack()
    label = Label(root, height=3)
    label.pack()


def test2(master=None):
    def get_info():
        if var1.get() != '' and var2.get() != '':
            info = "Accout: " + var1.get() + "\nPasswd: " + var2.get()
            result['text'] = info

    def quit_win():
        master.destroy()
        sys.exit()

    var1, var2 = StringVar(), StringVar()

    Label(master, text='账户: ', width=8, state='disable',
          font=('黑体', 15, 'bold'), justify='left').grid(row=0, column=0)
    Entry(master, textvariable=var1, width=10).grid(row=0, column=1)
    Label(master, text='密码: ', width=8, state='disable',
          font=('黑体', 15, 'bold'), justify='left').grid(row=1, column=0)
    Entry(master, textvariable=var2, width=10, show='*').grid(row=1, column=1)

    Button(master, text="获取信息", command=get_info).grid(row=2, column=0, sticky='w')
    Button(master, text="退出", command=quit_win).grid(row=2, column=1, sticky='e')

    result = Label(master, bg='black', fg='red', height=4, justify='left', wraplength=400)
    result.grid(row=3, column=0, columnspan=2)


def test3(master=None):
    v = StringVar()

    def test():
        if e1.get() == "python":
            t1.delete(0.0, END)
            t1.insert(0.0, "Bingo!")
            return True
        else:
            t1.delete(0.0, END)
            t1.insert(0.0, "Don't u love python?")
            return False

    e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=test)
    t1 = Text(master, width=50, height=2, bg='black', fg='red', state='normal')
    e1.pack(padx=10, pady=10, anchor='nw')
    t1.pack(padx=10, pady=10, anchor='nw')


def test4(master=None):
    v = StringVar()

    def test(content, reason, name):
        if content == "python":
            print("Bingo!")
            print(content, reason, name)
            return True
        else:
            print("Don't u love python?")
            print(content, reason, name)
            return False

    test_cmd = master.register(test)
    e1 = Entry(master, textvariable=v, validate="focusout",
               validatecommand=(test_cmd, '%P', '%v', '%W'))
    e2 = Entry(master)
    e1.pack(padx=10, pady=10)
    e2.pack(padx=10, pady=10)


def test5(master=None):
    frame = Frame(master)
    frame.pack(padx=10, pady=10)

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()

    def test(content):
        return content.isdigit()

    test_cmd = master.register(test)
    Entry(frame, width=10, textvariable=v1, validate="key",
          validatecommand=(test_cmd, '%P')).grid(row=0, column=0)

    Label(frame, text="+").grid(row=0, column=1)

    Entry(frame, width=10, textvariable=v2, validate="key",
          validatecommand=(test_cmd, '%P')).grid(row=0, column=2)

    Label(frame, text="=").grid(row=0, column=3)

    Entry(frame, width=10, textvariable=v3, state="readonly").grid(row=0, column=4)

    def calc():
        if v1.get().isdigit() and v2.get().isdigit():
            result = int(v1.get()) + int(v2.get())
            v3.set(str(result))
        else:
            v3.set(0)

    Button(frame, text="计算结果", command=calc, takefocus=True).grid(row=1, column=2, pady=5)


if __name__ == '__main__':
    root = Tk()
    # test1(root=root)
    # test2(root)
    test3(root)
    # test4(root)
    # test5(root)
    root.mainloop()
