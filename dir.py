import os
import time
import stat
import grp
import pwd

'''
用python实现和命令 dir -l 的相同输出
$ python dir.py
-rw-r--r-- 1 ec2-user users 1320 Oct 16 17:06 test.py
drwxr-xr-x 2 ec2-user users 4096 Sep 21 22:07 bin
drwxr-xr-x 3 ec2-user users 4096 Aug 01 11:43 temp_judy
-rw-r--r-- 1 ec2-user users 0 Oct 16 14:53 ttt.txt
'''

class Info(object):
    def __init__(self, name):
        statinfo = os.stat(name)
        mode = statinfo.st_mode
        self.permission = 'd' if stat.S_ISDIR(mode) else '-'
        permissions = [{'r':stat.S_IRUSR, 'w':stat.S_IWUSR, 'x':stat.S_IXUSR},
                       {'r':stat.S_IRGRP, 'w':stat.S_IWGRP, 'x':stat.S_IXGRP},
                       {'r':stat.S_IROTH, 'w':stat.S_IWOTH, 'x':stat.S_IXOTH}]

        for perm in permissions:
            self.permission += 'r' if mode & perm['r'] else '-'
            self.permission += 'w' if mode & perm['w'] else '-'
            self.permission += 'x' if mode & perm['x'] else '-'

        self.nlink = statinfo.st_nlink
        self.user = pwd.getpwuid(statinfo.st_uid).pw_name
        self.group = grp.getgrgid(statinfo.st_gid).gr_name
        self.size = statinfo.st_size
        self.filetime = time.strftime('%b %d %H:%M',time.localtime(statinfo.st_mtime))
        self.name = name

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.permission, self.nlink, self.user, self.group, self.size, self.filetime, self.name)


if __name__ == '__main__':
    path = '.'
    files = [x for x in os.listdir(path) if not x.startswith('.')]
    for file in files:
        print(Info(file))
