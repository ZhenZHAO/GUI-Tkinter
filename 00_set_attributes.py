import tkinter as tk


class MyTest(object):
    def __init__(self, root=None):
        self.window = root
        self._gui_init()

    def _gui_init(self):

        self.text_var = tk.StringVar()
        self.text_var.set("Hey, hello?")
        self.label = tk.Label(self.window, width=30, height=10, textvariable=self.text_var, fg='red', bg='blue')
        self.label.pack()

        # 设置btn已有属性
        # 方法一：在创建的时候设置 btn的text属性
        self.btn1 = tk.Button(self.window, width=10, height=5, fg='#008080', bg='black', text='click me')
        self.btn1['command'] = self.call_me
        # 判断是否按下
        self.is_clicked = False
        self.btn1.pack()

    def call_me(self):
        if not self.is_clicked:
            # 方法二：通过字典的形式设置btn的text属性
            self.btn1['text'] = 'reset'
            self.is_clicked = True
            self.text_var.set("keep away from me!")
        else:
            # 方法三：通过config函数设置btn的text属性
            self.btn1.config(text='click me')
            self.is_clicked = False
            # 方法四：通过textvariable 来设置text
            self.text_var.set("Hey, hello?")


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Methods to Set Text")
    my_test = MyTest(root)
    tk.mainloop()
