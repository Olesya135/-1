a=int(input())
c=input()
b=int(input())
d=a+b
f=a-b
g=a*b
h=a/b
if c=="+" or c=="сложить":
   print("=",d)
if c=="-" or c=="вычесть":
   print("=",f)
if c=="*" or c=="умножить":
   print("=",g)
if c=="/" or c=="разделить":
   print("=",h)