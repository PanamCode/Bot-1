from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards.menus import main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>! 👋\n\n"
        "Я бот для сбора заявок.\n"
        "Нажми кнопку ниже, чтобы оставить заявку.",
        reply_markup=main_menu(),
        parse_mode="HTML",
    )


@router.message(F.text == "ℹ️ О проекте")
async def about(message: Message):
    await message.answer(
        "Это демонстрационный бот для портфолио.\n\n"
        "• Приветствие и меню\n"
        "• Пошаговая форма заявки\n"
        "• Сохранение в Google Таблицу\n"
        "• Уведомление администратору\n\n"
        "Стек: <b>aiogram 3 + gspread + Bothost</b>",
        reply_markup=main_menu(),
        parse_mode="HTML",
    )
