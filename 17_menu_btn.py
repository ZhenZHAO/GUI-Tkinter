from tkinter import *
root = Tk()
mbLang = Menubutton(root,text = 'Language')

mbLang.menu = Menu(mbLang)
#生成菜单项
for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    mbLang.menu.add_command(label = item)
mbLang['menu'] = mbLang.menu
mbLang.pack(side = LEFT)
#分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令

#添加向菜单中添加checkbutton项
mbOS = Menubutton(root,text = 'OS')
mbOS.menu = Menu(mbOS)
for item in ['Unix','Linux','Soloris','Windows']:
    mbOS.menu.add_checkbutton(label = item)
mbOS['menu'] = mbOS.menu
mbOS.pack(side = LEFT)

#向菜单中添加radiobutton项
mbLinux = Menubutton(root,text = 'Linux')
mbLinux.menu = Menu(mbLinux)
for item in ['Redhat','Fedra','Suse','ubuntu','Debian']:
    mbLinux.menu.add_radiobutton(label = item)
mbLinux['menu'] = mbLinux.menu
mbLinux.pack(side = LEFT)

#对菜单项进行操作
#向Language菜单中添加一项"Ruby",以分隔符分开
mbLang.menu.add_separator()
mbLang.menu.add_command(label = 'Ruby')

#向OS菜单中第二项添加"FreeBSD",以分隔符分开
mbOS.menu.insert_separator(2)
mbOS.menu.insert_checkbutton(3,label = 'FreeBSD')
mbOS.menu.insert_separator(4)

#将Linux中的“Debian”删除
mbLinux.menu.delete(5)

root.mainloop()