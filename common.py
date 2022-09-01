from urllib import parse, request
from credentials import TOKEN, CHAT_ID


def notify_tg(message):
    bot_url = f"https://api.telegram.org/{TOKEN}/sendMessage?chat_id={CHAT_ID}" \
              f"&text={parse.quote(message)}" \
              f"&parse_mode=html"

    request.urlopen(bot_url)
