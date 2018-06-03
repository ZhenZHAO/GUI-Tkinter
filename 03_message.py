from tkinter import *


def test1(master=None):
    v = StringVar()
    v.set('Hello world, hello')
    Message(master, bg='black', fg='red',
            anchor='e',
            textvariable=v,
            aspect=200,
            justify=LEFT).pack()
    msg2 = Message(master, bg='grey', fg='blue',
                   anchor='e',
                   text="Hi, how are you?",
                   width=100,
                   justify=RIGHT)
    msg2.pack()

    def call_back():
        v.set("/Users/shao/Applications/anaconda3/envs/PyAppDev-basic/bin/python "
              "/Users/shao/Developer/PycharmProjects/stu_tkinter/03_message.py")
        msg2["text"] = "We don't talk anymore, we don't love anymore, " \
                       "we don't talk anymore like we use to do"

    Button(master, text="click", bd=10, relief=RIDGE, command=call_back).pack()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title("How To Use Message")
    center_window(root, 300, 200)
    test1(root)
    root.mainloop()
