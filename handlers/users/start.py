from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_btn import menu_btn
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from loader import dp, db
from data.data import data

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    user_id = int(message.from_user.id)
    all_user_id =[user[0] for user in db.select_all_users()]

    if user_id not in all_user_id:
        txt = "🇺🇿 Iltimos tilni tanlang!\n"
        txt += "🇺🇸 Please select a language!\n"
        txt += "🇷🇺 Пожалуйста, выберите язык!"
        # Inline Keyboard create
        btn_lang = InlineKeyboardMarkup(row_width=3)
        btn_lang.insert(InlineKeyboardButton(text="🇺🇿 Uz", callback_data="uz"))
        btn_lang.insert(InlineKeyboardButton(text="🇺🇸 Eng", callback_data="eng"))
        btn_lang.insert(InlineKeyboardButton(text="🇷🇺 Ru", callback_data="ru"))
        await message.answer(txt, reply_markup=btn_lang)
    else:
        lang = db.select_user(user_id=user_id)[2]
        index = data["lang"].index(lang)
        menu = data["menu"][index]
        await message.answer(menu, reply_markup=menu_btn(index))


@dp.callback_query_handler(lambda c: c.data in ["uz","eng","ru"])
async def process_callback_language(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = call.data
    index = data["lang"].index(lang)
    user_id = int(call.from_user.id)
    all_user_id = [user[0] for user in db.select_all_users()]

    if user_id not in all_user_id:
        # insert data to DB
        db.add_user(
                user_id=user_id,
                full_name=str(call.from_user.full_name),
                language=lang
            )
        til_tanlandi = data["til_tanlandi"][index]
        menu = data["menu"][index]

        await call.message.answer(til_tanlandi)
        await call.message.answer(menu, reply_markup=menu_btn(index))
    else:
        user_lang = db.select_all_users()[2]
        index = data["lang"].index(user_lang)
        allaqachon_til = data["allaqachon_til"][index]

        await call.message.answer(allaqachon_til)


