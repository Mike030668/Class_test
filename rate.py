import requests
import json

url = 'https://www.cbr-xml-daily.ru/latest.js'  # сайт с валютами
response = requests.get(url)  # запрос
data = json.loads(response.text)  # грузим

# выводим курсы валют
for rate in data['rates']:
    print(rate, data['rates'][rate])
