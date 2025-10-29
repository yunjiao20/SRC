from random import randint, choice  # 随机抽取函数
import os
from sys import argv, exit
from webbrowser import open as browser_open  # 打开默认浏览器

import file_handler as frd

class Students:
    '''用于传指针引用'''
    def __init__(self, names: list[str]) -> None:
        self.names = names
    def choice_and_remove(self) -> str|None:
        '''随机抽取学生姓名，将其从列表中删除，并追加到历史文件last_choiced_names.txt，
        如果列表为空（抽完了），返回None'''
        if len(self.names) == 0:
            return None
        name = choice(self.names)
        frd.file_additional(file='../src-history/last_choiced_names.txt',
                            content=name+'\n')# 追加
        self.names.remove(name)
        return name

############### 全局变量 ###############
stu_names = frd.get_stunames_from_file(file='../src-config/student_names.txt') 
print(f'学生姓名列表:\n{stu_names}\n共{len(stu_names)}人\n')

if isinstance(stu_names, str):    # 如果stu_names是一个字符串
    pass
    student = Students(names=[stu_names])  # 防止因没有student而报错
elif (
    frd.get_stunames_from_file(file='../src-config/student_names.txt') \
    == frd.get_stunames_from_file(file='../src-history/stu_names_copy.txt')
  ):    # 如果学生姓名文件没有更改
    print('您未修改学生姓名文件，为你删去上次抽取姓名')
    # 此种方式会丢失重复的学生名
    student = Students(list(
        set(stu_names) - set(frd.get_stunames_from_file(
                                file='../src-history/last_choiced_names.txt'))
    ))# 移除last_choiced_names.txt里上次抽到的学生名，创建Students的实例
    
    if len(student.names) == 0:
        # 如果学生姓名已抽完，清空历史记录，重置学生姓名副本实例的names属性
        student.names = stu_names
        with open('../src-history/last_choiced_names.txt', mode='w', encoding='utf-8'): pass # 清空文件

else :    # 学生姓名列表被更改 
    with open('../src-history/last_choiced_names.txt', mode='w', encoding='utf-8'): pass # 清空文件
    with open('../src-history/stu_names_copy.txt', mode='w', encoding='utf-8') as f:
        # 更新副本文件
        for n in stu_names:
            f.writelines(n+'\n')
    student = Students(names = stu_names[::])  # Students的实例，保存的是stu_names的副本

print(f'\n历史记录:\n{student.names}\n剩余{len(student.names)}人')

import gui  # 防止循环引用时全局变量被忽视，放在全局变量定义之后

############### 功能实现 ###############
def run_pyfile_if_argv() -> None:
    '''如果传入了参数，将最后一个参数作为文件名，尝试运行此Python文件'''
    if len(argv) >= 2:
        exec(frd.open_and_read(argv[-1]))
        exit()

def print_SRC() -> None:
    print(r'''
                  _______  ______      _____
                 /  ____ \|   __  \  /  _____\
                /  /____\/|  |  \  \/  /     \|
                \______  \|   _   ./  /
                /\____/  /|  | \  \\  \____. /
               /________/ |__|  \__\\.______/
---------------------Student Random Choice-------------------------
Welcome to src, base of Python3.14.0
主要随机抽取学生姓名的程序，项目地址：https://github.com/yunjiao20/SRC
''')
    
def print_help_msg() -> None:
    print('''
1  --随机抽取学生姓名
2  --不放回随机抽取学生姓名
3  --随机抽学号
q  --终止程序
clear  --重置不放回随机抽取的学生姓名，并清空上次抽取的历史记录

docs    --打开SRC的HTML文档
paddr   --打开项目地址
gui     --打开图形化界面
guilit  --打开guilit，一个轻量化的SRC-GUI
          
eval  --执行Python表达式，用于进行简单的数学计算和单行Python代码注入
exec  --多行Python代码注入
run   --运行Py文件
''')

def open_document(url: str, file=True) -> None:
    '''打开本地html文档及网站，如需打开网站，需指定file=Flase以关闭url处理'''
    if file:    # 是本地文件
        abs_path = os.path.abspath(url)  # 获取绝对地址
        url = f'file://{abs_path}'
    browser_open(url = url)

def check_names_list(l: list|str = stu_names) -> None:
    '''检查stu_names是否为"FileNotFoundError" or "NullStudentNemesList" '''
    if l == 'FileNotFoundError':  # 没有../src-config/student_names.txt文件 
        print('!!!  FileNotFoundError  !!!')
        print('文件 SRC/src-config/student_names.txt 不存在，请检查是否删除或移动此文件')
        input('Enter打开帮助文档')
        open_document('../docs/SRC问题排查.html')
        exit()
    if l == 'NullStudentNemesList':  # 学生列表为空
        print('!!!  NullStudentNemesList  !!!')
        print('学生姓名列表为空，您没有在文件  SRC/src-config/student_names.txt 提供学生名')
        input('Enter打开SRC配置文档')
        open_document('../docs/SRC基本配置和使用.html')
        exit()

def get_several_line_input() -> str:
    '''获取多行输入'''
    null_line_num = 0
    input_msg     = ''
    while True:
        i = input('code> ')
        if null_line_num >= 2:
            return input_msg
        elif i == '':
            null_line_num += 1
        else :
            input_msg += f'{i}\n'
            null_line_num = 0

############### 主要函数 ###############

def 随机抽取模式() -> None:
    print('随机有放回抽取，这可能回返回重复的学生姓名，输入“q”终止')
    while True:
        i = input('"q"终止> ')
        match i:
            case 'q':
                print_help_msg()
                return
            case _:
                print(choice(stu_names))
                print()

def 不放回随机抽取(student: Students = student) -> None:
    print('不放回随机抽取，前缀为剩余的学生数量，输入数字进行多次抽取，“q”终止')
    while True:        
        i = input(f'{len(student.names)}> ')
        if i == 'q':
            print_help_msg()
            return
        else:
            try: 
                if isinstance(eval(i), int):  # 保护代码
                    for _ in range(int(i)):
                        print(student.choice_and_remove())
                print()
            except SyntaxError:
                print(student.choice_and_remove())
                print()

def 随机抽学号(l = stu_names) -> None:
    print('随机抽学号，范围为1到学生列表的长度')
    while input('"q"终止> ') != 'q':
        print(randint(1, len(l)))
        print()
    else:
        print_help_msg()

def command_line():
    '''SRC command-line 的主函数, input-handle-output loop'''
    run_pyfile_if_argv()
    print_SRC()
    check_names_list()
    print_help_msg()
    while True:
        i = input('mode> ')
        match i:
            case 'q':
                print('\nSRC Quit\n')
                return
            case 'h':
                print_help_msg()
            case '1':
                随机抽取模式()
            case '2':
                不放回随机抽取()
            case '3':
                随机抽学号()
            case 'clear':
                student.names = stu_names
                with open('../src-history/last_choiced_names.txt', mode='w'): pass # 清空文件
            case 'docs':
                open_document('../docs/SRC基本配置和使用.html')
            case 'paddr':
                open_document(url='github.com/yunjiao20/SRC', file=False)
            case 'gui':
                gui.main()
            case 'guilit': 
                os.system(r'..\SRC-GUIlit\SRCGUIlit.exe')
            case 'eval':
                print(eval(input('eval> ')))
            case 'exec':
                exec(get_several_line_input())
            case 'run':
                exec(frd.open_and_read(input('file> ')))
            case _:
                print(f'!!!ERROR INPUT!!!  "{i}" not a legal command, pleas input "h" to watch help message')
                print(f'!!!错误输入!!!  "{i}"不是合法指令，请输入"h"以查看帮助信息')

if __name__ == '__main__':
    command_line()