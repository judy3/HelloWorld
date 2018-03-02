#!/usr/bin/python3
class ClassStudy:
    id=0 #类变量
    ttt="afgdsg"
    __weight="45" #私有属性，不能在外部调用

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        ClassStudy.id+=1
        self.test=True
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
print(s.test)
