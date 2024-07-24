# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from bot.filters import ...


def get_some_keyboard():
    builder = InlineKeyboardBuilder()
    # some logic
    # builder.adjust()
    return builder.as_markup()
