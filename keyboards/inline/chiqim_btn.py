from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data import data


def chiqim_btn(index):

    ofisxarajat = data["ofisxarajatlari"]
    bankxizmat = data["bankxizmati"]
    soliq = data["soliq"]
    divedent = data["divedent"]
    other = data["boshqaxarajatlar"]
    ortga = data["ortga"]

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=bankxizmat[index], callback_data="bank"),
             InlineKeyboardButton(text=divedent[index], callback_data="divident"),],
            [InlineKeyboardButton(text=ofisxarajat[index], callback_data="ofis"),
             InlineKeyboardButton(text=soliq[index], callback_data="soliq")],
            [InlineKeyboardButton(text=other[index], callback_data='boshqa')],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],
        ],
    )
    return btn

def ofis_btn(index):
    ortga = data["ortga"]
    reklama = data['reklama']
    telefonwifi = data["telefonwifi"]
    teambuilding = data['teambuilding']
    xizmatlaruchun = data['xizmatlaruchun']
    xostovar = data['xostovar']
    dokumentish = data['dokumentish']
    yoqilgi = data["yoqilgi"]
    smm = data['smm']
    ehson = data['ehson']
    litsenziya = data['litsenziya']
    konsalting = data['konsalting']
    kuchmasmulk = data['kuchmasmulk']
    talim = data['talim']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{reklama[index]}", callback_data=f"{reklama[index]}"),
                InlineKeyboardButton(text=f"{telefonwifi[index]}", callback_data=f"{telefonwifi[index]}"),
                InlineKeyboardButton(text=f"{teambuilding[index]}", callback_data=f"{teambuilding[index]}")

            ],
            [
                InlineKeyboardButton(text=f"{xizmatlaruchun[index]}", callback_data=f"{xizmatlaruchun[index]}"),
                InlineKeyboardButton(text=f"{xostovar[index]}", callback_data=f"{xostovar[index]}"),
                InlineKeyboardButton(text=f"{dokumentish[index]}", callback_data=f"{dokumentish[index]}")
            ],
            [
                InlineKeyboardButton(text=f"{yoqilgi[index]}", callback_data=f"{yoqilgi[index]}"),
                InlineKeyboardButton(text=f"{smm[index]}", callback_data=f"{smm[index]}"),
                InlineKeyboardButton(text=f"{ehson[index]}", callback_data=f"{ehson[index]}")
            ],
            [
                InlineKeyboardButton(text=f"{litsenziya[index]}", callback_data=f"{litsenziya[index]}"),
                InlineKeyboardButton(text=f"{konsalting[index]}", callback_data=f"{konsalting[index]}"),
                InlineKeyboardButton(text=f"{kuchmasmulk[index]}", callback_data=f"{kuchmasmulk[index]}")
            ],
            [
                InlineKeyboardButton(text=f"{talim[index]}", callback_data=f"{talim[index]}")
            ],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],
        ]

    )
    return btn


def other_btn(index):
    ortga = data["ortga"]
    qurxaraj = data['qurxaraj']
    qarz = data["qarz"]
    arenda = data['arenda']
    kommunal = data['kommunal']
    bonus = data['bonus']
    inventlar = data['inventlar']
    transfer = data['transfer']
    maosh = data['maosh']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{qurxaraj[index]}", callback_data=f"{qurxaraj[index]}"),
                InlineKeyboardButton(text=f"{qarz[index]}", callback_data=f"{qarz[index]}"),
                InlineKeyboardButton(text=f"{arenda[index]}", callback_data=f"{arenda[index]}")

            ],
            [
                InlineKeyboardButton(text=f"{kommunal[index]}", callback_data=f"{kommunal[index]}"),
                InlineKeyboardButton(text=f"{bonus[index]}", callback_data=f"{bonus[index]}"),
                InlineKeyboardButton(text=f"{inventlar[index]}", callback_data=f"{inventlar[index]}")
            ],
            [
                InlineKeyboardButton(text=f"{transfer[index]}", callback_data=f"{transfer[index]}"),
                InlineKeyboardButton(text=f"{maosh[index]}", callback_data=f"{maosh[index]}"),
            ],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],

        ]

    )
    return btn

#
# def divedent_btn(index):
#
#     divfarrux = data['divfarrux']
#     divbegzod = data["divbegzod"]
#     divabdulloh = data['divabdulloh']
#     divbosh = data['divbosh']
#
#     btn = InlineKeyboardMarkup(
#         inline_keyboard=
#         [
#             [
#                 InlineKeyboardButton(text=f"{divfarrux[index]}", callback_data=f"{divfarrux[index]}"),
#                 InlineKeyboardButton(text=f"{divbegzod[index]}", callback_data=f"{divbegzod[index]}")
#             ],
#             [
#                 InlineKeyboardButton(text=f"{divabdulloh[index]}", callback_data=f"{divabdulloh[index]}"),
#                 InlineKeyboardButton(text=f"{divbosh[index]}", callback_data=f"{divbosh[index]}")
#             ]
#         ]
#     )
#     return btn


def soliq_btn(index):
    ortga = data["ortga"]
    daromadsoligi = data['daromadsoligi']
    soliqreja = data['soliqreja']

    btn = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text=f"{daromadsoligi[index]}", callback_data=f"{daromadsoligi[index]}"),
                InlineKeyboardButton(text=f"{soliqreja[index]}", callback_data=f"{soliqreja[index]}")
            ],
            [InlineKeyboardButton(text=ortga[index], callback_data="ortga")],
        ]
    )
    return btn




