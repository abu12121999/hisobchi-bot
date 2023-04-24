from aiogram import types
from data.data import data

def menu_btn(index):
    kirim = data["btn_kirim"][index]
    chiqim = data["btn_chiqim"][index]
    til = data["btn_til"][index]
    info = data["btn_info"][index]
    menu_btn = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(kirim),
             types.KeyboardButton(chiqim)],
            [types.KeyboardButton(til),
             types.KeyboardButton(info)],
        ],
        resize_keyboard=True)
    return menu_btn