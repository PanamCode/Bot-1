from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states import ApplicationForm
from bot.keyboards.menus import main_menu, cancel_keyboard
from bot.services.google_sheets import save_application
from bot.config import settings

router = Router()


@router.message(F.text == "📝 Оставить заявку")
async def start_form(message: Message, state: FSMContext):
    await state.set_state(ApplicationForm.name)
    await message.answer(
        "Как вас зовут?",
        reply_markup=cancel_keyboard(),
    )


@router.message(F.text == "❌ Отмена")
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Заявка отменена.",
        reply_markup=main_menu(),
    )


@router.message(ApplicationForm.name)
async def process_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("Имя слишком короткое. Попробуйте ещё раз:")
        return

    await state.update_data(name=name)
    await state.set_state(ApplicationForm.phone)
    await message.answer("Отлично! Теперь укажите номер телефона:")


@router.message(ApplicationForm.phone)
async def process_phone(message: Message, state: FSMContext):
    phone = message.text.strip()
    if not any(c.isdigit() for c in phone) or len(phone) < 7:
        await message.answer("Похоже, это не номер телефона. Введите ещё раз:")
        return

    await state.update_data(phone=phone)
    await state.set_state(ApplicationForm.comment)
    await message.answer(
        "И последний шаг — комментарий (или просто «-»):",
        reply_markup=cancel_keyboard(),
    )


@router.message(ApplicationForm.comment)
async def process_comment(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    comment = message.text.strip()

    name = data["name"]
    phone = data["phone"]

    try:
        save_application(
            name=name,
            phone=phone,
            comment=comment,
            user_id=message.from_user.id,
            username=message.from_user.username,
        )
    except Exception:
        await message.answer(
            "Произошла ошибка при сохранении. Попробуйте позже.",
            reply_markup=main_menu(),
        )
        await state.clear()
        return

    # Уведомление админу
    admin_text = (
        f"<b>Новая заявка!</b>\n\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Телефон:</b> {phone}\n"
        f"<b>Комментарий:</b> {comment}\n\n"
        f"<b>От:</b> {message.from_user.full_name}\n"
        f"<b>ID:</b> <code>{message.from_user.id}</code>\n"
        f"<b>Username:</b> @{message.from_user.username or '—'}"
    )

    try:
        await bot.send_message(settings.admin_id, admin_text, parse_mode="HTML")
    except Exception:
        pass

    await state.clear()
    await message.answer(
        "Спасибо! Ваша заявка успешно отправлена ✅\n"
        "Мы свяжемся с вами в ближайшее время.",
        reply_markup=main_menu(),
    )
