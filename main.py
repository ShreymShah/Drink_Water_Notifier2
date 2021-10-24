import pytz
from datetime import datetime
import requests

tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
true_or_not = True

while 8 < now.hour < 22:
    now = datetime.now(tz)
    if str(now.minute) == '01':
        true_or_not = True

    telegram_token = '2058300469:AAFNOABY1Ay5ocvzASNGhgUyuKsQGhEGVHU'
    telegram_chat_id = '773247730'

    def send_msg_telegram(msg):
        url_telegram = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + telegram_chat_id + '&parse_mode=Markdown&text=' + msg
        requests.get(url_telegram)

    if now.minute == 00 and true_or_not == True:
        send_msg_telegram("DRINK WATER")
        send_msg_telegram("DRINK WATER")
        send_msg_telegram("DRINK WATER")
        true_or_not = False






