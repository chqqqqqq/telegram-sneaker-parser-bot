import json

import requests
from bs4 import BeautifulSoup



brand_list = ['Asics', 'Puma', 'Nike']

headers = {
    'Accept': 'image/avif,image/webp,*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }


for brand in brand_list:
    #brands_dict = {}
    models_dicts_list = []
    print(f"***Просматриваем бренд {brand}!")
    url = f'https://brandshop.ru/muzhskoe/obuv/krossovki/?mfp=manufacturers%5B{brand}%5D'
    req = requests.get(url=url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    all_products_hrefs = soup.find_all(class_="product-card__link")
    href_list = []

    for product_href in all_products_hrefs:
        href = "https://brandshop.ru" + product_href.get("href")
        href_list.append(href)
    print(f'Найдено {len(href_list)} моделей бренда {brand}!')

    for line in href_list:
        model_dict = {}
        req = requests.get(line)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        all_information = soup.find(class_='product-page')
        #brand = all_information.find(class_="product-page__header-wrapper").find("a").text
        model = all_information.find(class_="product-page__header-wrapper").find("span").text.strip()
        model_url = line
        model_jpg_url = all_information.find(class_='product-page__img _ibg').find('img').get("src")[:-9] + "1104x1104.jpg"
        model_price = all_information.find(class_='product-order__price-wrapper').text.strip()
        model_article = all_information.find(class_='product-data__name font_m').text
        model_sizes = all_information.find_all(class_="product-plate__item font font_sm")
        model_sizes_list = []
        for model_size in model_sizes:
            model_sizes_list.append(model_size.text.replace("В наличии: Онлайн, Офлайн", '').replace('\n', '').strip())
        model_dict = {
            'model': model,
            'model_url': model_url,
            'model_jpg_url': model_jpg_url,
            'model_price': model_price,
            'model_article': model_article,
            'model_sizes': model_sizes_list
        }
        models_dicts_list.append(model_dict)
        print(f'---Модель {model} бренда {brand} добавлена в БД!')
    #brands_dict[brand] = models_dicts_list
    with open(f"data/{brand}.json", "a", encoding="utf-8") as file:
        json.dump(models_dicts_list, file, indent=4, ensure_ascii=False)
    print(f'***Бренд {brand} просмотрен! Переходим к следующему....')



