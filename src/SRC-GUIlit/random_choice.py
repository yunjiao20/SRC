from random import choice  # 随机抽取函数
from webbrowser import open as browser_open  # 打开默认浏览器
import os

import file_reader as frd

class Students:
    '''用于传指针引用'''
    def __init__(self, names: list[str]) -> None:
        self.names = names
    def choice_and_remove(self) -> str|None:
        '''随机抽取学生姓名并从列表中删除，如果列表为空（抽完了），返回None'''
        if len(self.names) == 0:
            return None
        name = choice(self.names)
        self.names.remove(name)
        return name

############### 全局变量 ###############
stu_names = frd.get_stunames(
                frd.open_and_readlines(file='../src-config/student_names.txt')
                )
print('学生列表 stu_names 创建完成')
studnet = Students(names = stu_names[::])  # 保存的是stu_names的副本
print('学生名副本创建完成')

def open_document(url: str, file=True) -> None:
    '''打开本地html文档及网站，如需打开网站，需指定file=Flase以关闭url处理'''
    if file:    # 是本地文件
        abs_path = os.path.abspath(url)  # 获取绝对地址
        url = f'file://{abs_path}'
    browser_open(url = url)

