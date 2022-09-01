import json
from urllib import request

URL_MONO = "https://api.monobank.ua/bank/currency"
URL_PRIVAT = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def unify_courses(target_note) -> str:
    message = f"Currency {target_note['currencyCodeA']} to {target_note['currencyCodeB']} rate: \n " \
              f"rate buy: {target_note['rateBuy']} \n rate sell: {target_note['rateSell']}"

    return message


def get_courses(url):
    content = request.urlopen(url=url).read()
    content_decoded = json.loads(content.decode("utf-8"))

    return content_decoded[0]


def get_exchange_rate(bank='mono') -> list:
    courses = get_courses(URL_MONO)
    message = unify_courses(courses)

    return [message, message]
