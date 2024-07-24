from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# from bot.keyboards import get_start_keyboard
# from bot.texts import BotText

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    pass


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with "/help" command.
    """
    pass
