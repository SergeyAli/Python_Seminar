import requests



url = f"https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers= {
"apikey": "E8EOH0EStKYKLHTYh0K5SqoRu2YEbdLN"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text





# for i in stroka:
# if i in d.keys():
# print(d[i], end='')
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
#
# dict.items() - возвращает пары (ключ, значение).




# url = f"https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}"
#
# payload = {}
# headers= {"apikey": "E8EOH0EStKYKLHTYh0K5SqoRu2YEbdLN"}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text


# {
#   "change": true,
#   "end_date": "2010-01-01",
#   "quotes": {
#     "USDAUD": {
#       "change": -0.1726,
#       "change_pct": -13.4735,
#       "end_rate": 1.108609,
#       "start_rate": 1.281236
#     },
#     "USDEUR": {
#       "change": -0.0389,
#       "change_pct": -5.2877,
#       "end_rate": 0.697253,
#       "start_rate": 0.73618
#     },
#     "USDMXN": {
#       "change": 1.9594,
#       "change_pct": 17.5741,
#       "end_rate": 13.108757,
#       "start_rate": 11.149362
#     }
#   },
#   "source": "USD",
#   "start_date": "2005-01-01",
#   "success": true
# }

