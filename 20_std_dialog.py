import tkinter as tk
from tkinter import messagebox as mgb
from tkinter.messagebox import *
from tkinter import colorchooser
from tkinter import filedialog


def test_messagebox(master=None):
    mgb.showinfo(title="InfoWindow", message='What the fuck')
    mgb.showwarning("Spam", "Egg Warning")
    mgb.showerror("Spam", "Egg Alert")
    # print("info", showinfo("Spam", "Egg Information"))
    # print("warning", showwarning("Spam", "Egg Warning"))
    # print("error", showerror("Spam", "Egg Alert"))
    # print("question", askquestion("Spam", "Question?"))
    # print("proceed", askokcancel("Spam", "Proceed?"))
    # print("yes/no", askyesno("Spam", "Got it?"))
    print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
    print("try again", askretrycancel("Spam", "Try again?"))


def test_filedialog(master=None):
    def callback():
        print("fileName: ", filedialog.askopenfilename())

    tk.Button(master, text="打开文件", command=callback).pack()


def test_colorchooser(master=None):
    def callback():
        print("color:", colorchooser.askcolor())

    tk.Button(master, text="选择颜色", command=callback).pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("3 Standard Dialog")
    height, width = 300, 300
    root.geometry("%dx%d+%d+%d" % (width, height,
                                   (root.winfo_screenwidth() - width) // 2,
                                   (root.winfo_screenheight()- height) // 2))
    # test_messagebox(root)
    # test_colorchooser(root)
    test_filedialog(root)

    root.mainloop()

