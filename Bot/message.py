from .bot import bot
from DataBase.models import User


async def send_notification(parser_name: str):
    for u in User.select():
        await bot.send_message(u.tg_id, f"{parser_name} не обновил товары")
