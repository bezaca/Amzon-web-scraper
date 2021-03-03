# Env Config and Scrap Config
from bs4 import BeautifulSoup
import requests
import smtplib
import os
import ast
from dotenv import load_dotenv

load_dotenv()


# Initializing variables

URL = os.getenv('URL')
HEADERS = ast.literal_eval(os.getenv('HEADERS'))
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_EMAIL_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
WANTED_PRICE = os.getenv('WANTED_PRICE')


def send_email(product_title):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(f'{SENDER_EMAIL}', f'{SENDER_EMAIL_PASSWORD}')

    # Mail Creation
    #  Modify the mail content as you own needs

    subject = 'Price fell down!'

    body = f'Check the amazon link {URL} , for you product {product_title}'

    message = f'Subject: {subject}\n\n{body}'

    #

    server.sendmail(
        f'{SENDER_EMAIL}',  # From
        f'{RECEIVER_EMAIL}',  # To
        message  # Message
    )

    print('> Email has been sent')

    server.quit()


def check_price():

    page = requests.get(URL, headers=HEADERS)  # Getting the page
    soup = BeautifulSoup(page.content, 'lxml')  # Create a Instance of bs4

    title = soup.find(id='title').get_text()
    raw_price = soup.find(id='priceblock_ourprice').get_text()
    price = float(raw_price[:-5])

    print(
        f'> Getting web page......\n\n'
        f'Product: {title.strip()}\n'
        f'Price: {price}'
    )

    # Here you can change when the program notify you

    if (price < float(WANTED_PRICE)):
        send_email(title.encode('utf-8').strip())

    else:
        print('Nothing interesting happend')

    print(f'\n> Waiting for next execution.....')
