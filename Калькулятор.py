a=int(input())
c=input()
b=int(input())
s=a+b
d=a-b
f=a*b
g=a/b
if c=="+" or c=="сложить":
    print(a,"+",b,"=",s)
if c=="-" or c=="вычесть":
    print(a,"-",b,"=",d)
if c=="*" or c=="умножить":
    print(a,"*",b,"=",f)
if c=="/" or c=="разделить":
    print(a,"/",b,"=",g)
