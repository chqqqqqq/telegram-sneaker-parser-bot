from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from app.handlers import markups
from app.handlers.data_search import *


available_brand_names = ['asics', 'nike', 'puma']


async def cmd_start(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer(
        "Привет! Этот бот занимается поиском кроссовок!",
        reply_markup=markups.mainMenu
        )


async def cmd_mainmenu(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer(
        "Главное меню",
        reply_markup=markups.mainMenu
        )


async def cmd_brands(message: types.Message, state: FSMContext):

    await message.answer("Выберите бренд!", reply_markup=markups.BrandsMenu)


async def cmd_global_search(message: types.Message, state: FSMContext):

    await message.answer("Поиск по названию!")


async def cmd_info(message: types.Message, state: FSMContext):

    await message.answer("Информация")


async def cmd_random(message: types.Message, state: FSMContext):

        brand = available_brand_names[get_random_index(available_brand_names)]
        data = get_brand_data(brand)
        model_data = data[get_random_index(data)]
        model_info = get_model_data(model_data)
        dict = f"<b>{brand.capitalize()}</b>\n\n" + model_info

        await message.answer(dict)


def register_handlers_common(dp: Dispatcher):

    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_mainmenu, Text(equals="Главное меню", ignore_case=True), state="*")
    dp.register_message_handler(cmd_brands, Text(equals='Бренды', ignore_case=True), state="*")
    dp.register_message_handler(cmd_global_search, Text(equals='Поиск  модели кроссовок', ignore_case=True), state="*")
    dp.register_message_handler(cmd_info, Text(equals='Информация', ignore_case=True), state="*")
    dp.register_message_handler(cmd_random, Text(equals='Рандомные кроссовки', ignore_case=True), state="*")
