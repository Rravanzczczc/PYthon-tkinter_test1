




filename = "student.txt"

def main():
    while True:
        menu()
        choice = int(input('选择:'))  ##出现过错误这里”=“开始写成了”==“报错过
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("请确定是否需要退出，回复Y/N:")
                if answer = Y:
                   continue


            elif choice == 1:
                insert()


    pass


#菜单目录
def menu():
    print("=================管理系统==================")
    print("----------------1.录入信息-----------------")
    print("----------------2.查找信息-----------------")
    print("----------------1.录入信息-----------------")
    print("----------------1.录入信息-----------------")
    print("----------------1.录入信息-----------------")
    print("----------------1.录入信息-----------------")
    print("----------------1.录入信息-----------------")

#添加学生信息
def insert():
    student_list = []
    while True:
        id = input("输入用户id:")
        if not id:
            break
        name = input("输入用户姓名:")
        if not name:
            break
        try:
            eng_level = int(input("请输入英语成绩:   "))
            c_level = int(input("请输入C语言成绩:    "))
            py_level = int(input("请输入python成绩: "))
        except ValueError / TypeError:
            print("需要重新输入")
            continue

        student = {'id': id ,'name' : name,'eng_level':eng_level,"c_level": c_level,"py_level":py_level}
        student_list.append(student)
        answer = input('是否继续添加？Y/N： \n')
        if answer == Y or answer == y:
            continue
        else:
            break
    save(student_list)
    print("该次录入完毕")

#保存学生信息
def sava(list):
    try:
        stu_txt = open(filename,'a',encoding = "UTF-8")
    except:
        stu_txt = open(filename,'w',encoding = 'UTF-8')
    for item in list:



#查询学生信息
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        eng_level = ''
        c_level = ''
        py_level = ''
        if os.path.exists(filename):
            conditions = int(input("按照id查询请按1: \n 按照姓名查询请按2:"))
            if conditons == 1:
                id = input('请输入用户的ID:')
            if conditions == 2:
                name = input("请输入用户的姓名")
            else:
                print("非法的输入，请重新输入")
                search()

            with open(filename, 'r', encoding='UTF-8') as r_file:
                student_infos = r_file.readlines()
                for item in student_infos:
                    info = dict(eval(item))
                    if id != '':
                        if id == info['id']:
                            student_query.append(info)
                    elif name != '':
                        if name == info['name']:
                            student_query.append(info)


                    #显示查询结果
            show_student(student_query)

             #清空列表

            student_query.clear()
            answer = input('是否继续查询？Y/N： \n')
            if answer == Y or answer == y:
                continue
            else:
                break

        else:
            print("暂时没有保存任何学生信息")
            return

#显示学生信息
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到该学生的信息')
        return
    #定义标题显示格式
    show_title = '{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t'
    print(show_title.format('ID','姓名','英语成绩','C语言成绩','python成绩','总成绩'))
    #定义内容格式
    show_content = '{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t{:^6,}\t'
    print(show_content.format)

# 删除学生信息
def delete():
    while True:
        student_id = input('请输入用户的ID:')
        if student_id != '':

            if os.path.exists(filename):
                with open(filename,'r',encoding = 'UTF-8') as file:
                    student_infos = file.readlines()
            else:
                student_infos = []
            #标记是否删除
            flag == False

            #判断内容是否为空
            if student_infos:
                    with open(filename,'w',encoding = 'UTF-8') as w_file:
                        info = {}
                    for item in student_infos:
                        info = dic(eval(item))
                        if info['id'] != student_id:
                            w_file.write(str(info))
                        else:
                            flag = True

                    if flag:
                        print(f"学生的信息已经删除")
                    else:
                        print(f"没有找到ID为{student_id}的学生")
            else:
                print("无学生信息")
                break

#查询所有信息
def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename,'r',encoding = 'UTF-8') as r_file:
            student_infos = r_file.readlines()
            for item in student_infos:
                student_list.append(eval(item))
                if student_list:
                    show_student(student_list)


# 修改用户信息
def modify():
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as r_file:
            student_infos = r_file.readlines()
    else:
        return
    student_id = input('请输出需要修改的用户ID')
    with open(filename,'w',encoding ='UTF-8') as w_file:
        info = dict(eval(item))
        if info['id'] == student_id:
            print('找到指定学生信息，允许修改')
            while True:
                try:
                    info['name'] = input("输入姓名:")
                    info['name'] = input("输入姓名:")
                    info['name'] = input("输入姓名:")
                except:
                    print("输入有误，请重新输入")
                else:
                    break
            w_file。write(str(info) + "\n")
            print("修改成功")
            a = 1
        if a != 1:
            print("未找到该学生信息")


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as r_file:
            student_list = r_file.readlines()
            student_sort = []

            for item in student_list:
                student_info = dict(eval(item))
                student_sort.append(student_info)     ##有点问题 已经解决
    else:
        return
    asc_or_desc = input("请选择(0.升序，1.降序)")
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入错误，请重新输入')
        sort()

    choice = input ('请输入排序内容（1,按英语成绩排序,2,按python成绩排序,3.按照C语言，0.按照总成绩）')
    if choice == '1':
        #默认升序
        #list.sort(key = None,reverse = False)
        #key 为接受的参数为函数形式
        #reverse 排序规则，默认升序 reverse = True 降序， reverse =False 升序
        student_sort.sort(key=lambda s:int(s['英语成绩']),reverse = asc_or_desc_bool)
    if choice == '2':
        student_sort.sort(key=lambda s: int(s['Python']), reverse=asc_or_desc_bool)
    if choice == '3':
        student_sort.sort(key=lambda s: int(s['C语言']), reverse=asc_or_desc_bool)
    if choice == '0':
        student_sort.sort(key=lambda s: int(s['英语成绩'])+int(s['Python'])+int(s['C语言']), reverse=asc_or_desc_bool)
    else:
        print("你输入有误，重新输入")
        sort()
    show_student()


if __name__=="__main__":
    main()



## 打包程序 安装 pip install PyInstaller

## puinstaller -F D:\python\pycharmproject\learning\testdir\Finaltest\DictorySystem.py


