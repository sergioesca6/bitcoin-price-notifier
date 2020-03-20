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



## IFTTT

Sending a Test IFTTT Notification

Set up a new account https://ifttt.com/join  
install  mobile app (if you want to notifications to your phone)

To create a new test applet follow these steps:

1. Click on the “this” button
2. Search for the “webhooks” service and select the “Receive a web request” trigger
3. Let’s name the event test_event
4. Now select the “that” button
5. Search for the “notifications” service and select the “Send a notification from the IFTTT app”
6. Change the message to I just triggered my first IFTTT action! and click on “Create action”
7. Click on the “Finish” button

To see the documentation on how to use the IFTTT webhooks go to https://ifttt.com/maker_webhooks and click on the “Documentation” button in the top right corner. The documentation page contains the webhook URL and it looks like this:

https://maker.ifttt.com/trigger/{event}/with/key/{your-IFTTT-key}

Substitute the {event} part with whatever name you gave our event in step 3, when you created the applet. The {your-IFTTT-key} part is already populated with your IFTTT key.



## How it works

This Python app will make an HTTP request to the webhook URL which will trigger an action. Now, you could choose almost anything you want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.
