from aiogram.filters.callback_data import CallbackData


class MyCallbackClass(CallbackData, prefix="some_prefix"):
    pass
