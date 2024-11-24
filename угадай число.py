from random import randint
a=randint(1, 10)
p=3
while p>0:
    b=int(input('угодай число от 1 до 10:'))
    if b==a:
        print("winner")
    else:
        p-=1
        print(f'loser, осталось попыток: {p}',a)