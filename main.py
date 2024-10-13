import asyncio
from aiogram.utils import executor
from Bot.dispatcher import dp
from utils.sheduled_functions import scheduled_get_parsers, scheduled_check_updates


async def on_startup(x):
    asyncio.create_task(scheduled_get_parsers())


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        scheduled_check_updates()
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except KeyboardInterrupt:
        pass
