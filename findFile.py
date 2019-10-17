import os

'''
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

def findFile(str, path = '.'):
    for x in os.listdir(path):
        sub_path = os.path.join(path, x)
        if os.path.isdir(sub_path):
            findFile(str, sub_path)
        elif str in x:
            print(sub_path)

findFile('judy', '.')
