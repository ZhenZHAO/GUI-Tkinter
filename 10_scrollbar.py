from tkinter import *


def test1(master=None):
    frm1 = Frame(master)
    frm1.pack(fill=X, side=TOP)
    frm2 = Frame(master, height=50, bg='grey')
    frm2.pack(fill=X, side=TOP)

    # scrollbar + text
    Label(frm1, text="Text with Scrollbar", bg='red', fg='white').pack(fill=X, side=TOP)
    tx = Text(frm1, height=5, width=30)
    tx.pack(fill=X, side=LEFT)
    sb = Scrollbar(frm1,
                   orient=VERTICAL,
                   )
    sb.pack(fill=Y, side=LEFT)
    # bind them
    tx.config(yscrollcommand=sb.set)
    sb['command'] = tx.yview

    # scrollbar + listbox
    Label(frm2, text="Listbox with Scrollbar", bg='blue', fg='white').pack(fill=X, side=TOP)
    lbx_var = StringVar()
    lbx_var.set("Python C C++ C# Java Javascript HTML CSS Ruby Perl Assembly Lua")
    lbx = Listbox(frm2, listvariable=lbx_var,
                  selectmode=MULTIPLE,
                  height=5,
                  width=30
                  )
    lbx.pack(fill=X, side='left')
    lbx.see(5)

    sb2 = Scrollbar(frm2, orient=VERTICAL)
    sb2.pack(fill=Y, side=LEFT)
    sb2.set(0.5, 1)
    # bind them
    lbx.config(yscrollcommand=sb2.set)
    sb2.config(command=lbx.yview)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("Use Scroll Bar")
    center_window(root, 300, 300)

    test1(root)

    root.mainloop()

