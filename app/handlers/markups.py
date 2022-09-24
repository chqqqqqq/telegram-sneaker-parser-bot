from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton("Главное меню")


# --- Main Menu ---

btnBrands = KeyboardButton('Бренды')
btnSearch = KeyboardButton('Поиск  модели кроссовок')
btnInformation = KeyboardButton('Информация')
btnRandom_all = KeyboardButton('Рандомные кроссовки')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBrands,btnSearch, btnInformation, btnRandom_all)


# --- Brands Menu ---

btnNike = KeyboardButton("Nike")
btnPuma = KeyboardButton("Puma")
btnAsics = KeyboardButton("Asics")
BrandsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAsics, btnNike, btnPuma, btnMain)


# --- Nike Menu ---

btnShow_all_nike = KeyboardButton("Все кроссовки Nike")
btnSearch_nike = KeyboardButton('Поиск по бренду Nike')
NikeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShow_all_nike, btnSearch_nike,  btnMain)


# --- Puma Menu ---

btnShow_all_puma = KeyboardButton("Все кроссовки Puma")
btnSearch_nike = KeyboardButton('Поиск по бренду Puma')
PumaMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShow_all_puma, btnSearch_nike, btnMain)


# --- Asics Menu ---

btnShow_all_asics = KeyboardButton("Все кроссовки Asics")
btnSearch_asics = KeyboardButton('Поиск по бренду Asics')
AsicsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShow_all_asics, btnSearch_asics, btnMain)