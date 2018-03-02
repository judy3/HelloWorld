#!/usr/bin/python3
class Z():
    def __init__(self):
        self.__x=None
    def getx(self):
        print("getter method")
        return self.__x
    def setx(self,value):
        print("setter method")
        self.__x=value
    def delx(self):
        print("deleter method")
        del self.__x

    x=property(getx,setx,delx,"jhsdfjhweu")

if __name__=="__main__":
    z=Z()
    print(z.x)
    z.x="new"
    print(z.x)
    del z.x

class Y():
    def __init__(self):
        self.__a=100000
    @property
    def a(self):
        print("get info with decorator")
        return self.__a
    @a.setter
    def a(self,value):
        print("setter method with decorator")
        self.__a=value
    @a.deleter
    def a(self):
        del self.__a

if __name__=="__main__":
    y=Y()
    print(y.a)
    y.a=500
    print(y.a)
