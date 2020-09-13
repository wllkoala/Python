from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text="用户名")
        self.label01.grid(row=0, column=0)
        v1 = StringVar()
        v1.set("admin")
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1)
        self.label02 = Label(self, text="密码")
        self.label02.grid(row=1, column=0)
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.grid(row=1, column=1)
        Button(self, text="登录", command=self.login).grid(row=2, column=1)

    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()
        print("用户名：" + self.entry01.get())
        print("密码：" + self.entry02.get())
        if username == "admin" and password == "123":
            messagebox.showinfo("登录", "登录成功")
        else:
            messagebox.showinfo("登录", "登陆失败")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+200")
    root.title("一个经典的GUI")
    app = Application(master=root)
    root.mainloop()
