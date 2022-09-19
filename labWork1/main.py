import requests #библиотека для работы с запросами
import json #библиотека для работы с json

data = {'city':'Минск','ATM_currency':'USD'}

response = requests.get('https://belarusbank.by/api/atm/',params=data)
response = json.loads(response.text)
counter = 0 
for x in response:
  print(response[counter]['address'])
  counter += 1