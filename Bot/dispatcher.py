from aiogram import types
from aiogram.dispatcher import filters
from aiogram.utils.exceptions import BadRequest
from .bot import dp
from .message import *
from .keyboard import pagination_cb, parsers, get_pagination_keyboard
from utils.ftp_tasks import get_json, check_updates
from DataBase.models import User


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    User.get_or_create(tg_id=message.from_user.id)
    await bot.send_message(message.from_user.id, "Результаты",
                           reply_markup=get_pagination_keyboard(1, (len(parsers) - 1) // 4 + 1))


@dp.message_handler(commands=['check'])
async def send_check_updates(message: types.Message):
    await check_updates()


@dp.callback_query_handler(pagination_cb.filter())
async def handle_pagination_callback(call: types.CallbackQuery, callback_data: dict):
    current_page = int(callback_data['page'])
    total_pages = (len(parsers) - 1) // 4 + 1

    try:
        await call.message.edit_reply_markup(
            reply_markup=get_pagination_keyboard(current_page, total_pages)
        )
    except BadRequest:
        await bot.send_message(call.from_user.id, "Результаты",
                               reply_markup=get_pagination_keyboard(current_page, total_pages))
    await call.answer()


@dp.callback_query_handler(filters.Text(startswith="parser_"))
async def send_parser_info(call: types.CallbackQuery):
    try:
        file_name = get_json(call.data)
        await bot.send_message(call.from_user.id, f"https://parser-poiskzip.ru/{file_name}")
    except IndexError:
        await bot.send_message(call.from_user.id, f"Файла {call.data[7:]}.json не существует")
    await call.answer()
