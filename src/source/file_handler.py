'''
file_reader.py
读取文件，处理内容
'''
from time import strftime    # 获取当前时间



class SRC_Error:
    def __init__(self, error) -> None:
        self.error = error
    def __len__(self) -> int:
        return 0    # error的长度返回零
    def __repr__(self) -> str:
        return self.error

# SRC标准错误
FileNotFoundError    = SRC_Error(error='FileNotFoundError')
NullStudentNemesList = SRC_Error(error='NullStudentNemesList')

def open_and_readlines(file: str) -> list[str] | SRC_Error:
    ''' 使用readlines()读取utf-8编码文件内容并返回，如没有此文件，
    返回FileNotFoundError'''
    try:
        with open(file, mode='r' ,encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return FileNotFoundError
    else :
        return lines
    
def get_stunames(lines: list[str]) -> list[str] | SRC_Error:
    '''从所给列表的每个字符串元素中读取学生姓名，使用split()
    如果行的第一位为#，则忽略此行'''
    if lines == FileNotFoundError: # 没有此文件
        return lines  # 返回此错误信息
    
    stu_names_l = []
    for line in lines:
        if line[0] == '#':
            pass    # 忽略以#开头的行
        else :
            stu_names = line.split()
            if stu_names:    # stu_name 不为空列表
                stu_names_l += stu_names
            else :    # 空行和只有空格的行
                pass

    return stu_names_l if stu_names_l else NullStudentNemesList

def get_stunames_from_file(file: str, return_error: bool = True) -> list[str] | SRC_Error:
    '''调用open_and_readlines()和get_stunames()，打开文件获取学生姓名，简化调用流程
    如果return_error为False，当获取的姓名为NullStudentNemesList时，不返回SRC_Error，返回空列表。这是为了兼容上次抽取姓名文件'''
    names = get_stunames(open_and_readlines(file=file))
    return [] if (not return_error and names==NullStudentNemesList) else names
    # 当return_error为False时，如names==NullStudentNamesList，返回空列表而非错误
    # 考虑到直接 isinstance(names, SRC_Error) 会导致FileNotFoundError也被过滤，这将会在文件 src-history/last_choiced_names.txt
    # 缺失时程序保持静默，这将导致此函数在处理此文件时始终返回空列表，使记忆功能缺失。与其使用户使用受限制的功能，不如直接崩溃，提醒用户
    # 重新配置SRC

def open_and_read(file: str) -> str:
    '''打开文件并使用read()读取，返回一个字符串'''
    return open(file=file, mode='r', encoding='utf-8').read()

def file_additional(file: str, content: str) -> None:
    '''向文件中追加内容'''
    with open(file, mode='a', encoding='utf-8') as f:
        f.writelines(content)

def clear_file(file: str) -> None:
    '''清空文件'''
    with open(file, mode='w', encoding='utf-8'): pass

def time() -> str:
    '''返回当前时间的格式化字符串'''
    return strftime('%Y/%m/%d/%H:%M')