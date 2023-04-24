from aiogram import types

from keyboards.default.default_btn import menu_btn
from states.getKirim import GetKirim
from loader import dp, db
from aiogram.dispatcher import FSMContext
from data.data import data

from keyboards.inline.kirim_btn import boshqa_btn, turar_joy_btn, kirim_btn

#########################################################################################################
@dp.callback_query_handler(lambda query: query.data in ["boshqa_kirim", "turar_joy","ortga"], state=GetKirim.tur)
async def tur_kiritish(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = db.select_user(user_id=call.from_user.id)[2]
    index = data["lang"].index(lang)
    txt = data["tanlang"][index]

    if call.data == "boshqa_kirim":
        tur = data["boshqakirim"][index]
        await state.update_data({"turi": tur})
        await call.message.answer(txt, reply_markup=boshqa_btn(index))
        await GetKirim.nomi.set()

    if call.data == "turar_joy":
        tur = data["turarjoy"][index]
        await state.update_data({"turi": tur})
        await call.message.answer(txt, reply_markup=turar_joy_btn(index))
        await GetKirim.nomi.set()

    if call.data == "ortga":
        menu = data["menu"][index]
        await call.message.answer(menu, reply_markup=menu_btn(index))
        await state.finish()
#########################################################################################################

@dp.callback_query_handler(state=GetKirim.nomi)
async def turi(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)
    text = call.data
    lang = db.select_user(user_id=call.from_user.id)[-1]
    index = data["lang"].index(lang)
    summa = data['summanikirit'][index]
    if text != "ortga":
        await state.update_data({"nomi": text})
        await call.message.answer(summa)
        await GetKirim.qiymat.set()
    else:
        soha = data["soha"][index]
        await call.message.answer(soha, reply_markup=kirim_btn(index))
        await GetKirim.tur.set()
#########################################################################################################


