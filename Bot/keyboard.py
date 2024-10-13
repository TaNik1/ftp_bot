from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

pagination_cb = CallbackData('paginator', 'page')
parsers = []


def get_pagination_keyboard(current_page: int, total_pages: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)

    for name in parsers[(current_page - 1) * 4:(current_page - 1) * 4 + 4]:
        keyboard.add(InlineKeyboardButton(name, callback_data=name))

    if current_page > 1:
        keyboard.add(InlineKeyboardButton(
            "⬅️ Назад",
            callback_data=pagination_cb.new(page=current_page - 1)
        ))
        keyboard.insert(InlineKeyboardButton(
            f"{current_page}/{total_pages}",
            callback_data="current_page"
        ))

    else:
        keyboard.add(InlineKeyboardButton(
            f"{current_page}/{total_pages}",
            callback_data="current_page"
        ))

    if current_page < total_pages:
        keyboard.insert(InlineKeyboardButton(
            "Вперед ➡️",
            callback_data=pagination_cb.new(page=current_page + 1)
        ))

    return keyboard
