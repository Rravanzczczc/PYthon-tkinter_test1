import tkinter
import os
from tkinter import ttk
filename = 'student.txt'

class LoginPage:
    def __init__(self, root2):

        self.root = root2

        # 初始化登录界面
        self.login_frame = tkinter.Frame(self.root)
        self.login_frame.grid()

        # 设置标题
        self.root.title('学生信息管理')
        self.root.geometry('600x400')

        # 输入用户名+校验
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.creat_page()

        #self.root.mainloop()
    def creat_page(self):
        # 建立一个规范格式（美观）
        tkinter.Label(self.login_frame, width=15).grid(row=0, column=0)



        tkinter.Label(self.login_frame, text='用户名').grid(row=1, column=0)
        tkinter.Entry(self.login_frame, textvariable=self.username).grid(row=1, column=1)

        tkinter.Label(self.login_frame, text='密码').grid(row=2, column=0)
        tkinter.Entry(self.login_frame, textvariable=self.password).grid(row=2, column=1)

        tkinter.Button(self.login_frame, text='登录', command=self.check_login).grid(row=3, column=0)
        tkinter.Button(self.login_frame, text='退出', command=self.root.quit).grid(row=3, column=1)

    def check_login(self):
        print('检查登录')
        print('用户名：', self.username.get())
        print('密码：', self.password.get())
        if self.username.get() == 'admin' and self.password.get() == 'root':
            print('success')
            self.login_frame.destroy()
            MainPage(self.root)
        else:
            print('false')


class MainPage:
    def __init__(self, root2):
        self.root = root2
        self.root.title('信息管理系统')
        self.root.geometry('600x400')

        self.creat_page()


        #定义组件
        self.insert_frame = insertFrame(self.root)
        #self.insert_frame.pack()

        self.search_frame = searchFrame(self.root)
        #self.select_frame.pack()

        self.about_frame = aboutFrame(self.root)
        #self.about_frame.pack()

        self.change_frame = changeFrame(self.root)
        # self.change_frame.pack()

        self.delete_frame = deleteFrame(self.root)
        # self.delete_frame.pack()


    def creat_page(self):
        menu_bar = tkinter.Menu(self.root)

        menu_bar.add_command(label='录入', command=self.show_insert_frame)
        menu_bar.add_command(label='查询', command=self.show_search_frame)
        menu_bar.add_command(label='删除', command=self.show_delete_frame)
        menu_bar.add_command(label='修改', command=self.show_change_frame)
        menu_bar.add_command(label='关于', command=self.show_about_frame)

        self.root['menu'] = menu_bar

    def show_insert_frame(self):
        self.insert_frame.pack()
        self.search_frame.forget()
        self.about_frame.forget()
        self.change_frame.forget()
        self.delete_frame.forget()

    def show_search_frame(self):
        self.insert_frame.forget()
        self.search_frame.pack()
        self.about_frame.forget()
        self.change_frame.forget()
        self.delete_frame.forget()

    def show_about_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.about_frame.pack()
        self.change_frame.forget()
        self.delete_frame.forget()

    def show_change_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.about_frame.forget()
        self.change_frame.pack()
        self.delete_frame.forget()

    def show_delete_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.about_frame.forget()
        self.change_frame.forget()
        self.delete_frame.pack()


#插入页面
class insertFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.username = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.id = tkinter.StringVar()
        self.status = tkinter.StringVar()

        self.create_page()

    def create_page(self):
        tkinter.Label(self, width=15).grid(row=0, column=0, padx=5, pady=5)

        tkinter.Label(self, text='姓名').grid(row=1, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.username).grid(row=1, column=1, padx=5, pady=5)

        tkinter.Label(self, text='数学').grid(row=2, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.math).grid(row=2, column=1, padx=5, pady=5)

        tkinter.Label(self, text='语文').grid(row=3, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.chinese).grid(row=3, column=1, padx=5, pady=5)

        tkinter.Label(self, text='英语').grid(row=4, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.english).grid(row=4, column=1, padx=5, pady=5)


        tkinter.Button(self, text='录入', command=self.recode).grid(row=6, column=1)
        tkinter.Label(self, textvariable=self.status).grid(row=6, column=1)


    def recode(self):
        student_list = []

        stu = {
            "name": self.username.get(),
            "math": self.math.get(),
            "chinese": self.chinese.get(),
            "english": self.english.get(),
        }

        student_list.append(stu)

        try:
            stu_txt = open(filename, 'a', encoding='UTF-8')
        except:
            stu_txt = open(filename, 'w', encoding='UTF-8')
        for item in student_list:
            stu_txt.write(str(item) + '\n')
        stu_txt.close()

class searchFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.creat_page()


    def creat_page(self):
        columns = ("name", "chinese", "math", "english")
        columns_values = ("姓名", "语文", "数学", "英语")
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        self.tree_view.column('name',width=80, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.heading("name", text="姓名")
        self.tree_view.heading("chinese", text="语文")
        self.tree_view.heading("math", text="数学")
        self.tree_view.heading("english", text="英语")
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)
        self.show_data_frame()

        tkinter.Button(self, text="刷新", command=self.show_data_frame).pack()


    def show_data_frame(self):

        for _ in map(self.tree_view.delete, self.tree_view.get_children()):
            pass
        students = self.get_list()
        index = 0
        for stu in students:
            print(stu)
            self.tree_view.insert('', index + 1, values=(
                stu['name'], stu['math'], stu['chinese'], stu['english'],
            ))

    def get_list(self):
        student_list = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as r_file:
                student_infos = r_file.readlines()
                for item in student_infos:
                    student_list.append(eval(item))

        return student_list


class changeFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.username = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.id = tkinter.StringVar()
        self.status = tkinter.StringVar()

        self.create_page()
    def create_page(self):
        tkinter.Label(self, width=15).grid(row=0, column=0, padx=5, pady=5)

        tkinter.Label(self, text='姓名').grid(row=1, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.username).grid(row=1, column=1, padx=5, pady=5)

        tkinter.Label(self, text='数学').grid(row=2, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.math).grid(row=2, column=1, padx=5, pady=5)

        tkinter.Label(self, text='语文').grid(row=3, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.chinese).grid(row=3, column=1, padx=5, pady=5)

        tkinter.Label(self, text='英语').grid(row=4, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.english).grid(row=4, column=1, padx=5, pady=5)


        tkinter.Button(self, text='修改', command=self.change_user).grid(row=6, column=0)
        tkinter.Button(self, text='查询', command=self.search_user).grid(row=6, column=1)
        tkinter.Label(self, textvariable=self.status).grid(row=6, column=1)
    def search_user(self):
        pass


    def change_user(self):
        pass



class deleteFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.username = tkinter.StringVar()
        self.status = tkinter.StringVar()
        tkinter.Label(self, text='根据名字删除信息').pack()
        tkinter.Entry(self, textvariable=self.username).pack()
        tkinter.Button(self, text='删除', command=self.delete).pack()
        tkinter.Label(self, text=self.status).pack()

    def delete(self):
        student_id = self.username.get()
        if student_id != '':
            # 判断文件是否存在，读取数据
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student_infos = file.readlines()
            else:
                student_infos = []
            # 标记是否删除
            flag = False

            # 判断读取的内容是否为空
            if student_infos:
                with open(filename, 'w', encoding='UTF-8') as w_file:
                    info = {}
                    for item in student_infos:
                        # eval用来执行字符串表达式，dict进行字符串转字典
                        info = dict(eval(item))
                        # 查询出来的值 不等于给定删除的值，则进行覆盖写
                        if info['name'] != student_id:
                            w_file.write(str(info) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生')



class aboutFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        tkinter.Label(self, text='关于').pack()
        tkinter.Label(self, text='关于').pack()
        tkinter.Label(self, text='关于').pack()
        tkinter.Label(self, text='关于').pack()


root = tkinter.Tk()

#login_Page = LoginPage(root)
MainPage(root)

root.mainloop()