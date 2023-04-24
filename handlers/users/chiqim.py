from aiogram import types

from keyboards.default.default_btn import menu_btn
from states.getKirim import GetChiqim
from keyboards.inline.chiqim_btn import chiqim_btn
from loader import dp, db
from aiogram.dispatcher import FSMContext
from data.data import data, data1
from datetime import datetime
import pytz
#########################################################################################################
@dp.message_handler(text="🔴 Chiqim")
@dp.message_handler(text="🔴 Expenses")
@dp.message_handler(text="🔴 Расходы")
async def chiqim(message: types.Message):
    lang = db.select_user(user_id=message.from_user.id)[2]
    index = data["lang"].index(lang)
    soha = data["sohaa"][index]
    await message.answer(soha, reply_markup=chiqim_btn(index))
    await GetChiqim.tur.set()
#########################################################################################################

@dp.callback_query_handler(lambda query: query.data in ("bank", "divident", "ortga"), state=GetChiqim.tur)
async def tur_kiritishsh(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = db.select_user(user_id=call.from_user.id)[2]
    index = data["lang"].index(lang)

    if call.data == "bank":
        tur = data["bankxizmati"][index]
    if call.data == "divident":
        tur = data["divedent"][index]

    menu = data["menu"][index]
    txt = data["kritayotgansummaa"][index]

    if call.data != "ortga":
        await state.update_data({"turi": tur})
        await call.message.answer(txt)
        await GetChiqim.nomi.set()
    else:
        await state.finish()
        await call.message.answer(menu, reply_markup=menu_btn(index))
# #########################################################################################################
@dp.message_handler(content_types=types.ContentType.TEXT, state=GetChiqim.nomi)
async def turii(message: types.Message, state: FSMContext):
    text = message.text
    lang = db.select_user(user_id=message.from_user.id)[-1]
    index = data["lang"].index(lang)
    summa = data['summanikirit'][index]

    await state.update_data({"nomi": text})
    await message.answer(summa)
    await GetChiqim.qiymat.set()
# #########################################################################################################

@dp.message_handler(content_types='text', state=GetChiqim.qiymat)
async def qiymatt(message: types.Message, state: FSMContext):

    txt = message.text
    lang = db.select_user(user_id=message.from_user.id)[-1]
    index = data["lang"].index(lang)
    tasdiq = data['malumottas'][index]
    yes = data["yes"][index]
    no = data["no"][index]
    re_enter = data["re_enter"][index]

    if txt.isdigit():
        btn_yes_no = types.InlineKeyboardMarkup(row_width=2)
        btn_yes_no.insert(types.InlineKeyboardButton(text=f"{yes}", callback_data="yes"))
        btn_yes_no.insert(types.InlineKeyboardButton(text=f"{no}", callback_data="no"))
        await state.update_data({"qiymati": txt})
        await message.answer(tasdiq, reply_markup=btn_yes_no)
        await GetChiqim.tasdiq.set()
    else:
        await message.answer(re_enter)
        await GetChiqim.qiymat.set()
# #########################################################################################################
@dp.callback_query_handler(lambda query: query.data in ["yes","no"], state=GetChiqim.tasdiq)
async def tasdiqq(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.answer(cache_time=60)

    lang = db.select_user(user_id=call.from_user.id)[2]
    index = data1["lang"].index(lang)
    success = data1['malmuv'][index]
    re_enter = data1["re_enter"][index]

    if call.data == "yes":
        # get data from state
        data = await state.get_data()
        type = data.get("turi")
        name = data.get("nomi")
        value = data.get("qiymati")
        user_id = call.from_user.id
        date = datetime.now(pytz.timezone("Asia/Tashkent")).strftime("%d.%m.%Y")
        # insert data to DB
        db.add_chiqim(
            type=type,
            name=name,
            value=value,
            date=date,
            user_id=user_id
        )
        await call.message.answer(success)
        await state.finish()
    else:
        await call.message.answer(re_enter)
        await GetChiqim.qiymat.set()
# #########################################################################################################

