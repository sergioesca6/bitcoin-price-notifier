import requests
import time
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
BITCOIN_PRICE_THRESHOLD = 10000
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{your-IFTTT-key}'

def get_latest_cryptocurrency_price():
    coin = input('which cryptocurrency would you like to be notified about (full name)? ')
    concat = BITCOIN_API_URL + coin + '/'
    response = requests.get(concat)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    data = {'value': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)   
    return '<br>'.join(rows)

def main():
    bitcoin_history = []
    while True:
        price = get_latest_cryptocurrency_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        if len(bitcoin_history) == 5: 
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            bitcoin_history = []

        time.sleep(5 * 60)  

if __name__ == '__main__':
    main()