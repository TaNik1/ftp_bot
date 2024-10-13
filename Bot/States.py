from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateUser(StatesGroup):
    waiting_id = State()
