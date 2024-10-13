from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .config import token_bot

bot = Bot(token_bot, parse_mode="HTML")
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot, storage=MemoryStorage())
