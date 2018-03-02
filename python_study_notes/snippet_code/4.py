#!/usr/bin/python3
import math

content=dir(math)
#print(content)

if __name__=='__main__':
    money=100
    def addm():
        global money
        money+=1
        print(globals())
        print(locals())
        print(money)

addm()
