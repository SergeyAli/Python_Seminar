import requests
import json
from UI import *
from logger import *

def button_click():
    from_what_currency = input_from_currency()
    amount = amount_currency()
    in_what_currency = input_in_currency()
    url = f"https://api.apilayer.com/fixer/convert?to={in_what_currency}&from={from_what_currency}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "5R4rxwCfb1pNf3yFFBDMuWgufpMORVji"  # токен
    }

    response = requests.request("GET", url, headers=headers, data=payload)  # запрос
    result = json.loads(response.text)
    status_code = result['success']

    if status_code:
        answer = f"{result['query']['amount']} {result['query']['from']} = {result['result']} {result['query']['to']}"
        print(answer)
        info_logger(f"Запрос обработан: {answer}")
    else:
        info_logger(f"Запрос не обработан: from = {from_what_currency}, amount = {amount}, to = {in_what_currency}")
        print("\n\033[1mНе верный ввод валюты.\033[0m\nВажно! Вводить необходимо буквенный международный код валюты.\nПовторите ввод.\n")
        button_click()



