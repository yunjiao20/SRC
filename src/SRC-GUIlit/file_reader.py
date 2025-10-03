'''
file_reader.py
读取文件，处理内容
'''

def open_and_readlines(file: str) -> list[str] | str:
    ''' 使用readlines()读取utf-8编码文件内容并返回，如没有此文件，
    返回字符串'FileNotFoundError' '''
    try:
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return 'FileNotFoundError'
    else :
        return lines
    
def get_stunames(lines: list[str]) -> list[str] | str:
    '''从所给列表的每个字符串元素中读取学生姓名，使用split()
    如果行的第一位为#，则忽略此行'''
    if lines == 'FileNotFoundError': # 没有此文件
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

    return stu_names_l if stu_names_l else 'NullStudentNemesList'