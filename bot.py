# aiogram import
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

import html
from env import BOT_TOKEN
from utils import texts
import asyncio


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    inline_web_app_button = InlineKeyboardButton(
        text="📱 Yangi sim karta buyurtma qilish",
        web_app=WebAppInfo(url="https://4bb9-188-113-231-217.ngrok-free.app")
    )
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[[inline_web_app_button]])

    first_name = message.from_user.first_name
    await message.answer(texts.START.format(html.escape(first_name)), reply_markup=inline_markup, parse_mode="Markdown")
    
    
async def main():
    dp.include_router(router) 
    await dp.start_polling(bot)  

asyncio.run(main())
