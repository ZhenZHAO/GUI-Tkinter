import tkinter as tk
import sys


class MyGUI(object):
    def __init__(self, root):
        self.window = root
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self._gui_int()

    def quit(self):
        self.window.destroy()
        sys.exit()

    def _gui_int(self):
        # show multiple lines in single Label
        top_frame = tk.Frame(self.window)
        bottom_frame = tk.Frame(self.window)
        top_frame.pack(side=tk.TOP)
        bottom_frame.pack(side=tk.BOTTOM)

        self.text_label = tk.Label(top_frame,
                                   text="You need to contact manager to obtain enough rights",
                                   bg='red',
                                   fg='white',
                                   # width=50,
                                   padx=10,
                                   pady=10,
                                   justify=tk.LEFT,  # 用于控制多行的对齐
                                   anchor=tk.CENTER,  # 用于控制整个文本块在Label中的位置
                                   wraplength=200
                                   )
        self.text_label.pack(side=tk.LEFT)
        # show a image (PhotoImage: .gif, .pgm, .ppm; BitmapImage: .xbm)
        photo_img = tk.PhotoImage(file='PICS/18.gif')
        self.img_label = tk.Label(top_frame, image=photo_img)
        self.img_label.image = photo_img  # keep a reference!
        self.img_label.pack(side=tk.RIGHT)

        # compound image and text
        bg_img = tk.PhotoImage(file='PICS/bg.gif')
        self.bg_img_label = tk.Label(bottom_frame,
                                     image=bg_img,
                                     text='I love programming!',
                                     justify=tk.LEFT,
                                     compound=tk.CENTER,
                                     font=('Arial', 20),
                                     fg='white')
        self.bg_img_label.image = bg_img
        self.bg_img_label.pack()



def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    # print(size)
    root.geometry(size)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("How To Use Label")
    center_window(root, 300, 200)
    my_gui = MyGUI(root)
    root.mainloop()

