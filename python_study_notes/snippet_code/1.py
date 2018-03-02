#!/usr/bin/python3

class ClassStudy:
    id=0 #类变量
    ttt="afgdsg"
    __weight="45" #私有属性，不能在外部调用

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        ClassStudy.id+=1
    def displayLatest(self):
        print("The latest id is %d" %ClassStudy.id)

    def displayInfo(self):
        print("grade:%d name:%s" %(self.grade, self.name))

emp1=ClassStudy("a",1)
emp2=ClassStudy("b",2)

emp1.displayInfo()
emp2.displayInfo()

print("latest id is %d" %(ClassStudy.id)) #引用类变量 ClassStudy.id

class Student(ClassStudy):
    age=''
    def __init__(self,name,grade,age):
        ClassStudy.__init__(self,name,grade)
        self.age=age

    def speak1(self):
        print("%s is %d years old and at %d" %(self.name,self.age,self.grade))

s=Student('ken',9,15)
s.speak1()

class speaker():
    def __init__(self,name,topic):
        self.test=True
        self.name=name
        self.topic=topic
    def speak2(self):
        print("The topic is %s for %s" %(self.topic,self.name))

class girl(speaker,Student):
    topic=''
    def __init__(self,name,grade,age,topic):
        Student.__init__(self,name,grade,age)
        speaker.__init__(self,name,topic)

g=girl('anna',8,13,"py")
g.speak1()
g.speak2()

class parent():
    def tet(self):
        print("parent")
class child(parent):
    def tet(self):
        print("child")

c=child()
c.tet()
super(child,c).tet()  #super()用来调用父类方法

class strPrint():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "two items are %d %d " %(self.a,self.b)
    def __add__(self,other):
        return strPrint(self.a+other.a, self.b+other.b)

s1=strPrint(1,5)
s2=strPrint(2,8)
print(s1,s2)
sAll=s1+s2
print(sall)
