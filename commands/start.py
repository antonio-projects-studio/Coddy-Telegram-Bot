from aiogram.types import Message


async def start(message: Message):
    await message.answer("Я зашел")
