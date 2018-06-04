import tkinter as tk


def test1(master=None):
    lst =['China', 'USA', "UK", "Canada"]
    lstbox_var = tk.StringVar()
    lstbox1 = tk.Listbox(master,
                         listvariable=lstbox_var,
                         selectmode=tk.MULTIPLE,  # SINGLE, MULTIPLE
                         exportselection=True,
                         bg='grey',
                         fg='blue',
                         bd=20,
                         relief='ridge',
                         font=('Arial', 15, 'bold'),
                         selectbackground='red',
                         selectforeground='white',
                         selectborderwidth=2,
                         # setgrid=True
                         )
    lstbox1.pack()

    # method 1 - 设置/添加 选择项
    lst.append('Singapore')
    lstbox_var.set(lst)
    # lstbox_var.set("Python Ruby Perl Lua")


    # method 2 - 设置/添加 选择项
    # for item in lst:
    #     lstbox1.insert(tk.END, item)

    # method 1 - 删除某些选择项
    # 根据索引用del，根据值用remove
    # del lst[1:3]
    lst.remove('USA')
    lstbox_var.set(lst)

    # method 2 - 删除某些选择项
    # lstbox1.delete(1, 2)
    # print(lstbox_var.get())

    def call_back():

        print(lstbox1.size())

        # method 1 - 获取被选择的项
        # items_chosen = []
        # for index in range(len(lst)):
        #     if lstbox1.select_includes(index):
        #         items_chosen.append(lst[index])
        # if len(items_chosen):
        #     result['text'] = str(items_chosen)
        # else:
        #     result['text'] = ""

        # method 2 - 获取被选择的项
        # try:
        #     print(type(lstbox1.selection_get()))
        #     result['text'] = str(lstbox1.selection_get())
        # except:
        #     # 因为当没有任何选项被选择时候，lstbox1.selection_get会报错
        #     result['text'] = ''

        # method 3 - 获取被选择的项
        choices = [lst[x] for x in lstbox1.curselection()]
        # print(lstbox1.curselection(), choices)
        if len(choices):
            result['text'] = str(choices)
        else:
            result['text'] = ''

    tk.Button(master, text='show', command=call_back).pack()
    result = tk.Label(master, width=100, height=4, bg='black', fg='red')
    result.pack()


def test2(master=None):
    frm1 = tk.Frame(master)
    frm1.pack(side=tk.LEFT, anchor='nw')
    frm2 = tk.Frame(master)
    frm2.pack(side=tk.LEFT, anchor='nw')

    lb = tk.Listbox(frm1)
    sb = tk.Scrollbar(frm1)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    # 下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
    lb['yscrollcommand'] = sb.set
    for i in range(1, 20):
        lb.insert(tk.END, str(i**2))
    # 使用索引为100的元素可见
    lb.see(100)
    lb.pack(side=tk.LEFT)

    def show_info():
        if len(lb.curselection()) > 0:
            lst_item = lb.get(0, tk.END)
            info = "== Items Number:" + str(lb.size())
            info += "\n\n== Item includes:\n" + str(lst_item)
            info += '\n\n%s is selected' % (lst_item[lb.curselection()[0]])
            info += ", and it is the " + str(lb.index(lb.curselection()[0] + 1)) + "th Num."

            tx1.delete(0.0, tk.END)
            tx1.insert(0.0, info)

    btn_frm = tk.Frame(frm2)
    btn_frm.pack(side=tk.TOP, fill=tk.X)
    tk.Button(btn_frm, text='Delete', command=lambda: lb.delete(tk.ACTIVE)).pack(side=tk.LEFT, anchor='nw')
    tk.Button(btn_frm, text='Show', command=show_info).pack(side=tk.LEFT, anchor='nw')

    tx1 = tk.Text(frm2, height=10,); tx1.pack(fill=tk.X, side=tk.TOP)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Use ListBox")
    center_window(root, 360, 360)

    # test1(root)
    test2(root)

    root.mainloop()
