import requests
rub=int(input("Введите сумму в рублях: "))
import requests
data = requests.get('https://openexchangerates.org/api/latest.json?app_id=bb82b241eb69478fab1b3c37c42601ff&base=USD&symbols=RUB').json()
print ("курс доллара: ",data['rates']['RUB'])
b=data['rates']['RUB']
d=rub/b
h=round(d,4)
print(f"{rub} рублей = {h} долларов")