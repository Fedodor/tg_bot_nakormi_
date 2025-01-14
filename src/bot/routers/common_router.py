from aiogram import Router
from aiogram.types import Message

from bot.texts import BotText

router = Router()


@router.message()
async def unidentified_message_handler(message: Message) -> None:
    """
    This handler receives any unspecified messages
    """
    await message.answer(text=BotText.TEXT_NAME)
