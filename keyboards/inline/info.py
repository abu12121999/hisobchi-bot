from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.data import data

def info_btn(index):

    ortga = data['ortga'][index]
    kirim = data["kirim_table"][index]
    chiqim = data["chiqim_table"][index]
    ikkala = data["ikkala_table"][index]

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=kirim, callback_data="kirim_t"),
                InlineKeyboardButton(text=chiqim, callback_data="chiqim_t"),
            ],
            [
                InlineKeyboardButton(text=ikkala, callback_data="ikkala")
            ],
            [
                InlineKeyboardButton(text=ortga, callback_data="ortga")
            ]
        ],
    )
    return btn

def time_btn(index):
    ortga = data['ortga'][index]
    oylik = data["oylik"][index]
    uttiz = data["o'ttiz"][index]
    total = data["total"][index]

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=uttiz, callback_data="time_30"),
                InlineKeyboardButton(text=oylik, callback_data="time_oy")
            ],
            [
                InlineKeyboardButton(text=total, callback_data="total")
            ],
            [InlineKeyboardButton(text=ortga, callback_data="ortga")],
        ],
    )
    return btn