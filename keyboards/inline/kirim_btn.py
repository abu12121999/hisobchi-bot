from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data import data

def kirim_btn(index):

    oyboshi = data["oyboshiga"]
    boshqa_kirim = data["boshqakirim"]
    turar_joy = data["turarjoy"]
    ortga = data["ortga"]

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=oyboshi[index], callback_data="oyboshi")],
            [InlineKeyboardButton(text=boshqa_kirim[index], callback_data="boshqa_kirim"),
             InlineKeyboardButton(text=turar_joy[index], callback_data="turar_joy")],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],
        ],
    )
    return btn

def boshqa_btn(index):
    ortga = data["ortga"]
    jihoz = data['jihozlash']
    elektr = data["elektr"]
    pere = data['perebroska']
    obmen = data['obmen']
    rielt = data['rielterskiy']

    btn =  InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{jihoz[index]}", callback_data=f"{jihoz[index]}"),
                InlineKeyboardButton(text=f"{elektr[index]}", callback_data=f"{elektr[index]}"),
            ],
            [
                InlineKeyboardButton(text=f"{pere[index]}", callback_data=f"{pere[index]}"),
                InlineKeyboardButton(text=f"{obmen[index]}", callback_data=f"{obmen[index]}"),
            ],
            [InlineKeyboardButton(text=f"{rielt[index]}", callback_data=f"{rielt[index]}")],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],
        ]
    )
    return btn
def turar_joy_btn(index):
    ortga = data["ortga"]
    realizatsiya = data['realizatsiya']
    exteryer = data["exteryer"]
    uchastka = data['uchastka']
    noturarjoy = data['noturarjoy']
    aholiyashashjoyi = data['aholiyashashjoyi']
    fasad = data['Fasad']
    qurilish = data['qurilish']
    interyer = data['interyer']

    btn =  InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{exteryer[index]}", callback_data=f"{exteryer[index]}"),
                InlineKeyboardButton(text=f"{interyer[index]}", callback_data=f"{interyer[index]}"),
            ],
            [
                InlineKeyboardButton(text=f"{noturarjoy[index]}", callback_data=f"{noturarjoy[index]}"),
                InlineKeyboardButton(text=f"{aholiyashashjoyi[index]}", callback_data=f"{aholiyashashjoyi[index]}"),
            ],
            [
                InlineKeyboardButton(text=f"{uchastka[index]}", callback_data=f"{uchastka[index]}"),
                InlineKeyboardButton(text=f"{fasad[index]}", callback_data=f"{fasad[index]}"),
            ],
            [
                InlineKeyboardButton(text=f"{qurilish[index]}", callback_data=f"{qurilish[index]}"),
                InlineKeyboardButton(text=f"{realizatsiya[index]}", callback_data=f"{realizatsiya[index]}"),
            ],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],

        ]
    )
    return btn




