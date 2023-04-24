from aiogram import types

from keyboards.default.default_btn import menu_btn
from keyboards.inline.chiqim_btn import ofis_btn, soliq_btn, other_btn, chiqim_btn
from states.getKirim import GetChiqim
from loader import dp, db
from aiogram.dispatcher import FSMContext
from data.data import data

#########################################################################################################
@dp.callback_query_handler(lambda query: query.data in ["ofis", "soliq","boshqa","ortga"], state=GetChiqim.tur)
async def tur_kiritish(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = db.select_user(user_id=call.from_user.id)[2]
    index = data["lang"].index(lang)
    txt = data["tanlang"][index]

    if call.data == "ofis":
        tur = data["ofisxarajatlari"][index]
        await state.update_data({"turi": tur})
        await call.message.answer(txt, reply_markup=ofis_btn(index))
        await GetChiqim.nomi.set()

    if call.data == "soliq":
        tur = data["soliq"][index]
        await state.update_data({"turi": tur})
        await call.message.answer(txt, reply_markup=soliq_btn(index))
        await GetChiqim.nomi.set()

    if call.data == "boshqa":
        tur = data["boshqaxarajatlar"][index]
        await state.update_data({"turi": tur})
        await call.message.answer(txt, reply_markup=other_btn(index))
        await GetChiqim.nomi.set()

    if call.data == "ortga":
        menu = data["menu"][index]
        await call.message.answer(menu, reply_markup=menu_btn(index))
        await state.finish()
#########################################################################################################

@dp.callback_query_handler(state=GetChiqim.nomi)
async def turii(call: types.CallbackQuery, state: FSMContext):
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
        await GetChiqim.qiymat.set()
    else:
        soha = data["sohaa"][index]
        await call.message.answer(soha, reply_markup=chiqim_btn(index))
        await GetChiqim.tur.set()
# #########################################################################################################
#
#
