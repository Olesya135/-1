from random import randint
a=randint(1, 10)
m=0
n=0
while n<3:
  b=int(input())
  n=n+1
  if b==a:
      m=+1
if m>0:
   print("winner")
else:
   print("loser")