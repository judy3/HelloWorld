import os
class Findfile(object):
    def __init__(self, str, path = '.'):
        for x in os.listdir(path):
            sub_path = os.path.join(path, x)
            if os.path.isdir(sub_path):
                Findfile(str, sub_path)
            elif str in x:
                print(sub_path)


if __name__ == '__main__':
    Findfile('ho')
