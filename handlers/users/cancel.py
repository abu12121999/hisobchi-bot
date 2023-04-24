from aiogram import types
from aiogram.dispatcher import FSMContext
from data.data import data
from keyboards.default.default_btn import menu_btn
from loader import db, dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await message.delete()
    user_id = int(message.from_user.id)
    lang = db.select_user(user_id=user_id)[2]
    index = data["lang"].index(lang)
    menu = data["menu"][index]
    await state.finish()
    await message.answer(menu, reply_markup=menu_btn(index))

