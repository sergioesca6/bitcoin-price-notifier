# bitcoin-price-notifier

Script that will notify you with bitcoin price updates

## App Details 

For this project we used the requests package. Webhooks are used to connect the Python app to external services, such as phone notifications or Telegram messages.

It is a full-fledged Bitcoin price notification service that will be easily extendable to other cryptocurrencies and services.

## Notification Details

Bitcoin Price Notifications With Python

I used the popular automation website IFTTT. IFTTT (“if this, then that”) is a web service that bridges the gap between different apps and devices.

The two IFTTT applets created:

    -Emergency notification when Bitcoin price falls under a certain threshold
    -Regular Telegram updates on the Bitcoin price.

Both will be triggered by our Python app which will consume the data from the Coinmarketcap API.

An IFTTT applet is composed of two parts: a trigger and an action.

## How it works

This Python app will make an HTTP request to the webhook URL which will trigger an action. Now, you could choose almost anything you want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.
