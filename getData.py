# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 23:25:56 2021

@author: Hossein
"""

from bs4 import BeautifulSoup
import requests
import os
import time
import telegram
import csv
import json
import jdatetime

f = open("data.json")
data = json.load(f)

os.system('cls')
my_token_car = data["my_token_car"]
chat_id_car = data["chat_id_car"]

my_token_mobile = data["my_token_mobile"]
chat_id_mobile = data["chat_id_mobile"]

my_token_rent = data["my_token_rent"]
chat_id_rent = data["chat_id_rent"]

my_token_sell = data["my_token_sell"]
chat_id_sell = data["chat_id_sell"]

date_f = str(jdatetime.date.today()).split('-')
date = f"{date_f[0]}/{date_f[1]}/{date_f[2]}"

print(date)


def send(msg, chat_id, token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


def get_sell_price(last_title):
    response = requests.get('https://divar.ir/s/tehran/buy-apartment')
    # print(response.status_code)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    price = soup.find_all('div', {"class": "kt-post-card__description"})
    title = soup.find_all('div', {"class": "kt-post-card__title"})
    place = soup.find_all('div', {"class": "kt-post-card__bottom"})
    recent = len(title)
    for i in range(len(title)):
        if title[i].text == last_title:
            recent = i

    title2 = []
    place2 = []
    price2 = []
    link_sell2 = []
    for j in range(0, recent):
        title2.append(title[j].text)
    for j in range(0, recent):
        price2.append(price[j].text)
    for j in range(0, recent):
        place2.append(place[j].text)

    for i in range(0, recent):
        href_tags = soup.find_all("a", href=True)
        link_sell2.append('https://divar.ir' + href_tags[386 + i]['href'])
    return (title2, price2, place2, link_sell2)


def get_rent_price(last_title):
    response = requests.get(
        'https://divar.ir/s/tehran/rent-apartment?credit=100000-')
    # print(response.status_code)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    price = soup.find_all('div', {"class": "kt-post-card__description"})
    title = soup.find_all('div', {"class": "kt-post-card__title"})
    place = soup.find_all('div', {"class": "kt-post-card__bottom"})
    recent = len(title)
    for i in range(len(title)):
        if title[i].text == last_title:
            recent = i

    title2 = []
    place2 = []
    price2 = []
    link_rent2 = []
    for j in range(0, recent):
        title2.append(title[j].text)
    for j in range(0, recent):
        price2.append(price[j].text)
    for j in range(0, recent):
        place2.append(place[j].text)

    for i in range(0, recent):
        href_tags = soup.find_all("a", href=True)
        link_rent2.append('https://divar.ir' + href_tags[385 + i]['href'])

    return (title2, price2, place2, link_rent2)


def get_car_price(last_title):
    response = requests.get('https://divar.ir/s/tehran/car?price=10000-')
    # print(response.status_code)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    price = soup.find_all('div', {"class": "kt-post-card__description"})
    title = soup.find_all('div', {"class": "kt-post-card__title"})
    place = soup.find_all('div', {"class": "kt-post-card__bottom"})
    recent = len(title)
    for i in range(len(title)):
        if title[i].text == last_title:
            recent = i

    title2 = []
    place2 = []
    price2 = []
    link_car2 = []
    for j in range(0, recent):
        title2.append(title[j].text)
    for j in range(0, recent):
        price2.append(price[j].text)
    for j in range(0, recent):
        place2.append(place[j].text)

    for i in range(0, recent):
        href_tags = soup.find_all("a", href=True)
        link_car2.append('https://divar.ir' + href_tags[113 + i]['href'])

    return (title2, price2, place2, link_car2)


def get_mobile_price(last_title):
    response = requests.get(
        'https://divar.ir/s/tehran/mobile-phones?price=100000-')
    # print(response.status_code)
    mobile_text = response.text
    soup = BeautifulSoup(mobile_text, 'html.parser')
    price = soup.find_all('div', {"class": "kt-post-card__description"})
    title = soup.find_all('div', {"class": "kt-post-card__title"})
    place = soup.find_all('div', {"class": "kt-post-card__bottom"})
    recent = len(title)
    for i in range(len(title)):
        if title[i].text == last_title:
            recent = i

    title2 = []
    place2 = []
    price2 = []
    link_mobile2 = []
    for j in range(0, recent):
        title2.append(title[j].text)
    for j in range(0, recent):
        price2.append(price[j].text)
    for j in range(0, recent):
        place2.append(place[j].text)

    for i in range(0, recent):
        href_tags = soup.find_all("a", href=True)
        link_mobile2.append('https://divar.ir' + href_tags[19 + i]['href'])

    return (title2, price2, place2, link_mobile2)


last_sell = ''
last_rent = ''
last_car = ''
last_mobile = ''

delay = 3
first_loop = 1
while True:
    try:
        date_f = str(jdatetime.date.today()).split('-')
        date = f"{date_f[0]}/{date_f[1]}/{date_f[2]}"

        # print(get_sell_price())
        recent_sell_adv = get_sell_price(last_sell)
        if len(recent_sell_adv[0]) > 0:

            send_num = len(recent_sell_adv[0])
            if first_loop == 1:
                send_num = 1
            for ii in range(send_num):

                i = len(recent_sell_adv[0]) - ii - 1
                print('sell****************')
                print(i)

                time.sleep(delay)

                chat = recent_sell_adv[0][i] + '\n' + recent_sell_adv[1][i] + '\n' + '\n' + '\n'+'آگهی از سایت دیوار' + \
                '\n'+recent_sell_adv[2][i]+'\n'+'\n'+date+'\n'+recent_sell_adv[3][i]
                print(chat)
                send(chat, chat_id_sell, my_token_sell)

                last_sell = recent_sell_adv[0][i]
        else:
            print('no new sell advertisement')

        # print(get_rent_price())

        recent_rent_adv = get_rent_price(last_rent)
        if len(recent_rent_adv[0]) > 0:
            send_num = len(recent_rent_adv[0])
            if first_loop == 1:
                send_num = 1
            for ii in range(send_num):

                i = len(recent_rent_adv[0]) - ii - 1
                print('rent***************')
                print(i)

                time.sleep(delay)

                chat = recent_rent_adv[0][i] + '\n' + recent_rent_adv[1][i] + '\n' + '\n' + '\n'+'آگهی از سایت دیوار' + \
                '\n'+'\n'+recent_rent_adv[2][i]+'\n'+date+'\n'+recent_rent_adv[3][i]
                print(chat)
                send(chat, chat_id_rent, my_token_rent)
                last_rent = recent_rent_adv[0][i]
        else:
            print('no new rent advertisement')

        # print(get_car_price())

        recent_car_adv = get_car_price(last_car)
        if len(recent_car_adv[0]) > 0:
            send_num = len(recent_car_adv[0])
            if first_loop == 1:
                send_num = 1
            for ii in range(send_num):

                i = len(recent_car_adv[0]) - ii - 1
                print('car***************')
                print(i)

                time.sleep(delay)

                chat = recent_car_adv[0][i] + '\n' + recent_car_adv[1][i] + '\n' + '\n' + '\n'+'آگهی از سایت دیوار' + \
                '\n'+'\n'+recent_car_adv[2][i]+'\n'+date+'\n'+recent_car_adv[3][i]
                print(chat)
                send(chat, chat_id_car, my_token_car)
                last_car = recent_car_adv[0][i]
        else:
            print('no new car advertisement')

        # print(get_mobile_price())

        recent_mobile_adv = get_mobile_price(last_mobile)
        if len(recent_mobile_adv[0]) > 0:
            send_num = len(recent_mobile_adv[0])
            if first_loop == 1:
                send_num = 1
            for ii in range(send_num):

                i = len(recent_mobile_adv[0]) - ii - 1
                print('mobile************')
                print(i)

                time.sleep(delay)

                chat= recent_mobile_adv[0][i] + '\n' + recent_mobile_adv[1][i] + '\n' + '\n' + \
                '\n'+'\n'+recent_mobile_adv[2][i]+'\n'+date+'آگهی از سایت دیوار'+'\n' + \
                date+'\n'+recent_mobile_adv[3][i]
                print(chat)
                send(chat, chat_id_mobile, my_token_mobile)
                last_mobile = recent_mobile_adv[0][i]
        else:
            print('no new mobile advertisement')

        first_loop = 0

        # time.sleep(5)

    except:
        print('Error')
