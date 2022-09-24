from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from app.handlers import markups
from app.handlers.data_search import *


class OrderBrand(StatesGroup):

    waiting_for_brand_name = State()
    waiting_for_price_search = State()


async def asics_start(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer("Бренд Asics выбран!", reply_markup=markups.AsicsMenu)
    await state.update_data(brand=message.text)


async def nike_start(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer("Бренд Nike выбран!", reply_markup=markups.NikeMenu)
    await state.update_data(brand=message.text)


async def puma_start(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer("Бренд Puma выбран!", reply_markup=markups.PumaMenu)
    await state.update_data(brand=message.text)


async def get_all(message: types.Message, state: FSMContext):

    await state.reset_state(with_data=False)
    user_data = await state.get_data()
    brand = user_data['brand']
    data = get_brand_data(brand)
    for model_data in data:
        model_info = get_model_data(model_data)
        dict = f"<b>{brand}</b>\n\n" + model_info
        await message.answer(dict)


async def search_models_by_price(message: types.Message, state: FSMContext):

    await message.answer("Введите цену")
    await state.set_state(OrderBrand.waiting_for_price_search.state)


async def get_models_by_price(message: types.Message, state: FSMContext):

    price_list = detect_price_for_search(message.text)
    price = price_list[0]
    user_data = await state.get_data()
    brand = user_data['brand']
    data = get_brand_data(brand)
    result = price_search(data, price)
    if result == []:
        await message.answer(f'Не найдено моделей, , цена которых ниже {price_list[1]}')
    else:
        for model_data in result:
            model_info = get_model_data(model_data)
            dict = f"<b>{brand}</b>\n\n" + model_info
            await message.answer(dict)
        await message.answer(f"Найдено {len(result)} моделей бренда {brand}, цена которых ниже {price_list[1]}")
    await state.reset_state(with_data=False)


def register_handlers_brands(dp: Dispatcher):

    dp.register_message_handler(asics_start, Text(equals='Asics', ignore_case=True), state="*")
    dp.register_message_handler(nike_start, Text(equals='Nike', ignore_case=True), state="*")
    dp.register_message_handler(puma_start, Text(equals='Puma', ignore_case=True), state="*")

    dp.register_message_handler(get_all, Text(equals="Все кроссовки Asics", ignore_case=True), state="*")
    dp.register_message_handler(get_all, Text(equals="Все кроссовки Nike", ignore_case=True), state="*")
    dp.register_message_handler(get_all, Text(equals="Все кроссовки Puma", ignore_case=True), state="*")

    dp.register_message_handler(search_models_by_price, Text(equals='Поиск по бренду Asics', ignore_case=True), state="*")
    dp.register_message_handler(search_models_by_price, Text(equals='Поиск по бренду Nike', ignore_case=True), state="*")
    dp.register_message_handler(search_models_by_price, Text(equals='Поиск по бренду Puma', ignore_case=True), state="*")

    dp.register_message_handler(get_models_by_price, state=OrderBrand.waiting_for_price_search)
