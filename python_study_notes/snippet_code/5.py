#!/usr/bin/python3

def addNum():
    a=input("a is: ")
    b=input("b is: ")
    print(type(a))
    c=float(a)+float(b)
    print("a+b=%.2f"%(c))
#addNum()

def sqr():
    a=input("a is:")
    sqr=float(a)**0.5
    print("sqr a is:%.2f"%sqr)
#sqr()

def xx():
    print("ax**2+bx+c=0")
    a,b,c=input("a,b,c is: use ',' to split ").split(',')
    a=float(a)
    b=float(b)
    c=float(c)
    d=a**2-4*a*c
    print("d=%.2f"%d)
    if d<0:
        print("not legal")
    elif a==0 and b==0 and c==0:
        print("endless x")
    else:
        d2=d**0.5
        x1=(-b+d2)/2*a
        x2=(-b-d2)/2*a
        print("x1=%.2f x2=%.2f"%(x1,x2))
#xx()

def trS():
    a,b,c=input("a,b,c is: use space to split ").split(' ')
    a=float(a)
    b=float(b)
    c=float(c)
    if a+b>c and a+c>b and c+b>a:
        p=(a+b+c)*0.5
        s_temp=p*(p-a)*(p-b)*(p-c)
        s=s_temp**0.5
        print("The square is %.2f"%s)
    else:
        print("not a triangle")
#trS()

def randnumber(x,y):
    import random
    a=random.randint(x,y)
    b=int(input("input a number between %d and %d:"%(x,y)))
    i=1
    while a!=b:
        print("not right, try again!")
        b=int(input("input the number again:"))
        i+=1
    else:
        print("guess right, congratulations!")
#randnumber(78,71002)

def CtoF():
    CorF=input("choose which kind of temperature to convert, C or F:")
    i=1
    while CorF!="C" and CorF!="F":
        print("please input C or F!")
        CorF=input("input the type again, C or F:")
        i+=1
    else:
        if CorF=='C':
            c=float(input("input the temperature degrees of C:"))
            f=c*1.8+32
            print("C %.2f convert to F is %.2f degrees"%(c,f))
        elif CorF=='F':
            f=float(input("input the temperature degrees of F:"))
            c=(f-32)/1.8
            print("F %.2f convert to C is %.2F degrees"%(f,c))
#CtoF()

def exchange2value():
    x=input("input the value of x:")
    y=input("input the value of y:")
    x,y=y,x
    print("now x is %s, y is %s"%(x,y))
#exchange2value()

def isnumber(x):
    try:
        float(x)
        return True
    except (TypeError, ValueError):
        print("the value is invaild. Try again.")
        return False

def checkNumber():
    x=input("input a number:")
    result=isnumber(x)
    i=1
    while result==False:
        print("It's not a number, try again.")
        x=input("input a number again:")
        result=isnumber(x)
        i+=1
    else:
        x=float(x)
        if x>0:
            print("{0} is postive.".format(x))
        elif x<0:
            print("{0} is negtive.".format(x))
        else:
            print("{0} is zero.".format(x))
#checkNumber()

def oddOrEven():
    x=input("input a number:")
    result=isnumber(x)
    i=1
    while result==False:
        print("It's not a number, try again.")
        x=input("input a number again:")
        result=isnumber(x)
        i+=1
    else:
        x=int(x)
        m=x%2
        if m==0:
            print("{0} is even number.".format(x))
        else:
            print("{0} is odd number.".format(x))
#oddOrEven()
