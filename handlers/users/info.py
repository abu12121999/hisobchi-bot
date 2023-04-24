
from aiogram import types

from data.data import data
from keyboards.inline.info import info_btn, time_btn
from loader import db, dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from states.info import infoState
from utils.db_api.excel import get_table_total, get_table_month


@dp.message_handler(Text(equals="👤 Ma'lumotlarim"))
@dp.message_handler(Text(equals="👤 Моя информация"))
@dp.message_handler(Text(equals="👤 My Info"))
async def info(message: types.Message, state: FSMContext):
    lang = db.select_user(user_id=message.from_user.id)[2]
    index = data["lang"].index(lang)
    tanla = data["tanlang"][index]
    await message.answer(tanla, reply_markup=info_btn(index))
    await infoState.type.set()

@dp.callback_query_handler(lambda query: query.data in ['kirim_t','chiqim_t',"ikkala","ortga"], state=infoState.type)
async def time_choose(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = db.select_user(user_id=call.from_user.id)[2]
    index = data["lang"].index(lang)
    tanla = data["vaqt_tanlash"][index]

    if call.data == "kirim_t":
        await state.update_data({"type": "kirim"})
        await infoState.time.set()
        await call.message.answer(tanla, reply_markup=time_btn(index))
    if call.data == "chiqim_t":
        await state.update_data({"type": "chiqim"})
        await infoState.time.set()
        await call.message.answer(tanla, reply_markup=time_btn(index))
    if call.data == "ikkala":
        await state.update_data({"type": "ikkala"})
        await infoState.time.set()
        await call.message.answer(tanla, reply_markup=time_btn(index))
    if call.data == "ortga":
        await call.message.answer(data["tanlang"][index], reply_markup=info_btn(index))
        await infoState.type.set()

@dp.callback_query_handler(lambda query: query.data in ["time_30","time_oy","total", "ortga"], state=infoState.time)
async def file_send(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)
    user_id = call.from_user.id
    lang = db.select_user(user_id=user_id)[2]
    index = data["lang"].index(lang)
    tanla = data["tanlang"][index]
    data_type = await state.get_data()
    type = data_type.get("type")

    if call.data == "time_30":


        await state.finish()

    if call.data == "time_oy":
        if type == "kirim":
            document = get_table_month(type="kirim", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=document)
            await state.finish()
        if type == "chiqim":
            document = get_table_month(type="chiqim", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=document)
            await state.finish()
        if type == "ikkala":
            kirim, chiqim = get_table_month(type="ikkala", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=kirim)
            await call.bot.send_document(chat_id=user_id, document=chiqim)
            await state.finish()

    if call.data == "total":
        if type == "kirim":
            document = get_table_total(type="kirim", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=document)
            await state.finish()
        if type == "chiqim":
            document = get_table_total(type="chiqim", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=document)
            await state.finish()
        if type == "ikkala":
            kirim, chiqim = get_table_total(type="ikkala", user_id=user_id)
            await call.bot.send_document(chat_id=user_id, document=kirim)
            await call.bot.send_document(chat_id=user_id, document=chiqim)
            await state.finish()


    if call.data == "ortga":
        await call.message.answer(tanla, reply_markup=info_btn(index))
        await infoState.type.set()


