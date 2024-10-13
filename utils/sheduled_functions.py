from Bot.keyboard import parsers
import asyncio
from .ftp_tasks import get_parsers, check_updates
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


async def scheduled_get_parsers() -> None:
    while True:
        parsers[:] = get_parsers()
        await asyncio.sleep(24 * 60 * 60)


def scheduled_check_updates() -> None:
    scheduler = AsyncIOScheduler()

    moscow_tz = pytz.timezone('Europe/Moscow')
    trigger = CronTrigger(hour=12, minute=0, timezone=moscow_tz)

    scheduler.add_job(check_updates, trigger)

    scheduler.start()
