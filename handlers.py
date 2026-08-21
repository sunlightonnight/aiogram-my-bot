from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Start")],
            [KeyboardButton(text="Help"), KeyboardButton(text="Settings")],
            [KeyboardButton(text="About")]
        ]
    )
    return keyboard

@router.message(Command("start"))
@router.message(F.text == "Start")
async def start_handler(message: Message):
    await message.answer("Hello! I'm your bot. How can I assist you today?", reply_markup=get_main_reply_keyboard())

@router.message(Command("help"))
@router.message(F.text == "Help")
async def help_handler(message: Message):
    await message.answer("Here are some commands you can use:\n/start - Start the bot\n/help - Show this help message\n/settings "
    "- Configure your settings\n/about - Learn more about this bot")