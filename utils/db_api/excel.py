from datetime import datetime, timedelta
import io
import pandas as pd
import pytz
from loader import db
from aiogram import types

def get_table_total(type, user_id):
    # init variable
    type=type
    user_id=user_id
    today = datetime.now(pytz.timezone("Asia/Tashkent"))
    now = today.strftime("%d.%m.%Y")
    if type == "kirim":
        data = db.get_kirim(user_id=user_id)
        excel_file = io.BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer._save()
        excel_file.seek(0)
        document=types.InputFile(excel_file, filename=f"Kirim total {now}.xlsx")
        return document

    if type == "chiqim":
        data = db.get_chiqim(user_id=user_id)
        excel_file = io.BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer._save()
        excel_file.seek(0)
        document = types.InputFile(excel_file, filename=f"Chiqim total {now}.xlsx")
        return document

    if type == "ikkala":
        kirim = get_table_total(type="kirim", user_id=user_id)
        chiqim = get_table_total(type="chiqim", user_id=user_id)
        return (kirim, chiqim)
#########################################################################################
def get_table_month(type, user_id):
    # init variable
    type=type
    user_id=user_id
    today = datetime.now(pytz.timezone("Asia/Tashkent"))
    date = today - timedelta(days=today.day-1)
    now = today.strftime("%d.%m.%Y")
    if type == "kirim":
        data = db.get_kirim_month(date=date, user_id=user_id)
        excel_file = io.BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer._save()
        excel_file.seek(0)
        document=types.InputFile(excel_file, filename=f"Kirim month {now}.xlsx")
        return document

    if type == "chiqim":
        data = db.get_kirim_month(date=date, user_id=user_id)
        excel_file = io.BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer._save()
        excel_file.seek(0)
        document = types.InputFile(excel_file, filename=f"Chiqim month {now}.xlsx")
        return document

    if type == "ikkala":
        kirim = get_table_total(type="kirim", user_id=user_id)
        chiqim = get_table_total(type="chiqim", user_id=user_id)
        return (kirim, chiqim)


# today = datetime.now(pytz.timezone("Asia/Tashkent"))
#     date = today - timedelta(days=30) # 24.03.2023
#     # formatting date
#     date = date.strftime("%d.%m.%Y")
#     today = today.strftime("%d.%m.%Y")