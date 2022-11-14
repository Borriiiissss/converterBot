from config import keys
import requests
import json

class convertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convertExceptions (values):
        quote, base, amount = values           
        if quote == base:
            return convertionException ('вы ввели одинаковые валюты')
        if not amount.isdigit() or int(amount) < 1:
            return convertionException ('вы некорректно указали количество валюты')
        if quote not in keys:
            return convertionException ('вы ввели некорректное название валюты 1')
        if base not in keys:
            return convertionException ('вы ввели некорректное название валюты 2')

class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return float(total_base)*float(amount)
