import json
import random
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink


def get_brand_data(brand):

    with open(f"data/{brand}.json", encoding="utf-8") as file:
        brand_data = json.load(file)
    return brand_data


def get_model_data(dict:dict):

    model = dict["model"]
    model_url = dict["model_url"]
    model_jpg_url = dict["model_jpg_url"]
    model_price = dict["model_price"]
    model_article = dict["model_article"]
    model_sizes = ' / '.join(dict["model_sizes"])
    if model_sizes == []:
        model_sizes = 'Нет размеров'
    model_data = f"<b>{hlink(model, model_jpg_url)}</b>\n\n" \
           f"<b>Артикул</b>:         {model_article}\n" \
           f"<b>Размеры</b>:        {model_sizes}\n" \
           f"<b>Цена</b>:                 {model_price}\n\n" \
           f"<b>{hlink('Купить', model_url)}</b>"
    return model_data


def price_search(data, search_price):

    searched_list = []
    for dict in data:
        price = int(dict['model_price'][:-2].replace(" ", ""))
        if price < search_price:
            searched_list.append(dict)
    return searched_list


def detect_price_for_search(message_price):

    price = ''
    for i in message_price:
        if i.isdigit():
            price += i
    if price != '':
        price_int = int(price)
        price_str = str(price)[:-3] + ' ' + str(price)[-3:] + ' ₽'
        price_list = [price_int, price_str]
        return price_list
    else:
        return False


def get_random_index(list):

    index = random.randint(0, len(list) - 1)
    return index