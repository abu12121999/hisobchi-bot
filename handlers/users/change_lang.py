from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from data.data import data
from keyboards.default.default_btn import menu_btn
from loader import db, dp


@dp.message_handler(text="✍️ Tilni o'zgartirish")
@dp.message_handler(text="✍️ Change Language")
@dp.message_handler(text="✍️ Изменить язык")

async def til_uzgartirish(message: types.Message):
    lang = db.select_user(user_id=message.from_user.id)[2]

    txt = "🇺🇿 Iltimos tilni tanlang!\n"
    txt += "🇺🇸 Please select a language!\n"
    txt += "🇷🇺 Пожалуйста, выберите язык!"
    # Inline Keyboard create
    btn_lang = InlineKeyboardMarkup(row_width=3)
    btn_lang.insert(InlineKeyboardButton(text="🇺🇿 Uz", callback_data="edit_uz"))
    btn_lang.insert(InlineKeyboardButton(text="🇺🇸 Eng", callback_data="edit_eng"))
    btn_lang.insert(InlineKeyboardButton(text="🇷🇺 Ru", callback_data="edit_ru"))
    await message.answer(txt, reply_markup=btn_lang)

@dp.callback_query_handler(lambda c: c.data in ["edit_uz","edit_eng","edit_ru"])
async def process_callback_language(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = call.data.split('_')[-1]
    user_id = int(call.from_user.id)
    index = data["lang"].index(lang)
    menu = data["menu"][index]

    try:
        db.update_user_language(user_id=user_id,language=lang)
        await call.message.answer(menu, reply_markup=menu_btn(index))
    except:
        pass



