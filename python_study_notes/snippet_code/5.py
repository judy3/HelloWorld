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

def getmax():
    s=input("please input a list of numbers, use comma to split:")
    l=s.split(',')
    m=max(l)
    print("The max in {0} is {1}.".format(s,m))
#getmax()

def primeNumCheck():
    a=int(input("input a number:"))
    if a>1:
        for c in range(2,a):   #range(2,2) no result
            b=a%c
            if b==0:
                print("Not prime number.")
                print("{0} can be devided by {1}.".format(a,c))
                break
        else:  ##如果for循环未被break终止，则执行else块中的语句或者for循环中不满足的条件执行else语句
            print("yes, prime number.")
    else:
        print("not prime number")
#primeNumCheck()

def primeOut(a,b):
    if a<1 or a==1:
        a=2
    c=b+1
    l=[]
    for d in range(a,c):
        for e in range(a,d):
            if d%e==0:
                break
        else:
            l.append(d)
    print(l)

#primeOut(0,100)

def factorial():
    a=int(input("input a number:"))
    b=a+1
    d=1
    if a==0:
        d=1
        print("factorial of {0} is {1}.".format(a,d))
    elif a<0:
        print("negetive number doesn't have factorial.")
    else:
        for i in range(1,b):
            d=d*i
        print("factorial of {0} is {1}.".format(a,d))
#factorial()

def showTimesTable():
    for a in range(1,10):
        for b in range(1,a+1):
            c=a*b
            print('{0}*{1}={2}\t'.format(a,b,c),end='')
        print() #一定要有这一行
#showTimesTable()

# 1,2,3,4,5,6,7,8...
# 0,1,1,2,3,5,8,13...
def qiebo(n):
    c1=0
    c2=1
    count=2
    if n==1:
        print("the list is: {}".format(c1))
    elif n==0 or n<0:
        print("no list")
    else:
        print("the list is {0} {1}".format(c1,c2),end=' ')
        while count<n:
            c=c1+c2
            print(c,end=' ')
            c1=c2
            c2=c
            count+=1
#qiebo(50)

#2
def checkAmster(n):
    length=len(str(n))
    if n<0:
        print("negetive number is not Amster")
    else:
        i=1
        c=0
        while i<length+1:
            a=n%(10**i)//(10**(i-1))
            b=a**length
            d=c+b
            i=i+1
            c=d
        if d==n:
            print("a Amster")
        else:
            print("not a Amster")
#checkAmster(153)

def getAmster(min,max):
    for n in range(min,max+1):
        sum=0
        length=len(str(n))
        temp=n
        while temp>0:
            d=n%10
            sum=d**length+sum
            temp=temp//10
        if sum==n:
            print(n)
#getAmster(0,500)

def checkAmster2(num):
    strnum=str(num)
    length=len(strnum)
    i=0
    sum=0
    while i<length:
        sum=int(strnum[i])**length+sum
        i=i+1
    if sum==num:
        print("{} is Amster".format(num))
    else:
        print("{} not Amster".format(num))
#checkAmster2(153)

def exchangeNum():
    number=int(input("input a number:"))
    print("decimal:{0}, binary:{1}, octonary:{2}, hexademical:{3}".format(number,bin(number),oct(number),hex(number)))
#exchangeNum()

def asiiToChr():
    x=input("input a character:")
    print("{0} ascii is: {1}".format(x,ord(x)))
    y=int(input("input a ascii number:"))
    print("{0} character is:{1}".format(y,chr(y)))
#asiiToChr()

def GCD(a,b):
    if a>b:
        smaller=b
        bigger=a
    else:
        smaller=a
        bigger=b
    for i in range(1,smaller+1):
        if smaller%i==0 and bigger%i==0:
            gcd=i
    print("the biggest common divisor for {0} and {1} is {2}.".format(a,b,gcd))
    return int(gcd)
#GCD(14,24)

def lcm(a,b):
    lcm=int(a*b/GCD(a,b))
    print("least common multiple for {0} and {1} is {2}.".format(a,b,lcm))
#lcm(4,6)

def lcm2(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while True:
        if (greater%a==0) and (greater%b==0):
             lcm=greater
             break
        greater+=1
    return lcm
#print(lcm2(4,6))

def showmonth():
    import calendar
    year=int(input("input the year:"))
    month=int(input("input the month:"))
    print(calendar.month(year,month))
#showmonth()

def recur_fibo_number(n):
    if n<=1:
        return n
    else:
        return recur_fibo_number(n-2)+recur_fibo_number(n-1)
def recur_fibo_list():
    nterms=int(input("how many numbers you'd like to print out? "))
    if nterms<=0:
        print("must be postive.")
    else:
        for i in range(nterms):
            print(recur_fibo_number(i),end=' ')
#recur_fibo_list()

def iofile():
    with open("20180307.txt","wt") as outfile:
        outfile.write("This line will be written to the file.")
    with open("20180307.txt","rt") as infile:
        out=infile.read()
        print(out)
#iofile()

def checkStr():
    str=input("input a string:")
    print(str.isalnum())
    print(str.isdigit())
    print(str.isalpha())
    print(str.islower())
    print(str.isupper())
    print(str.istitle())
    print(str.isspace())
#checkStr()

def exchangeStr():
    str=input("input a string:")
    print(str.upper())
    print(str.lower())
    print(str.capitalize())
    print(str.title())
#exchangeStr()

def daysOfMonth():
    year=int(input("input the year:"))
    month=int(input("input the month:"))
    import calendar
    print(calendar.monthrange(year,month))
#daysOfMonth()

def getDateBeforeToday():
    import datetime
    today=datetime.date.today()
    duration=int(input("how many days ago of the date?"))
    date1=datetime.timedelta(duration)
    date2=today-date1
    return date2
print(getDateBeforeToday())
