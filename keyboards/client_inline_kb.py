#from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from aiogram.dispatcher.filters import Text

urlkb = InlineKeyboardMarkup(row_width=1)

url_button = InlineKeyboardButton(text="3 курс", url="https://www.dropbox.com/s/ujptql6fghhr9pv/%D0%9D%D0%B0%D0%B2%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%20%D0%B4%D0%B8%D1%81%D1%86%D0%B8%D0%BF%D0%BB%D1%96%D0%BD%D0%B0%20_%D0%94%D0%86%D0%9C_3%20%D0%BA%D1%83%D1%80%D1%81_%20%D0%A1%D0%B8%D0%BB%D0%B0%D0%B1%D1%83%D1%81.doc?dl=0")
url_button2 = InlineKeyboardButton(text="4 курс", url="https://www.dropbox.com/s/kt6r4y3wi3p8xuj/%D0%9A%D1%83%D1%80%D1%81-%D0%B7%D0%B0-%D0%B2%D0%B8%D0%B1%D0%BE%D1%80%D0%BE%D0%BC-%20%D0%94%D0%86%D0%9C_%D0%95%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B4%D1%96%D0%BB%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BB%D0%B8%D1%81%D1%82%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F.doc?dl=0")

urlkb.add(url_button, url_button2)

proginkb = InlineKeyboardMarkup(row_width=1)

kb_url1 = InlineKeyboardButton(text='3 курс', url='https://www.dropbox.com/s/vph510m6v0oa957/upstream-upper-intermediate-b2-sb_red2.pdf?dl=0')
kb_url2 = InlineKeyboardButton(text='4 курс', url='https://www.dropbox.com/s/deakpmkxf70ywn9/tasks_part%201.pdf?dl=0')

proginkb.add(kb_url1, kb_url2)


selfkb = InlineKeyboardMarkup(row_width=1)

surl = InlineKeyboardButton(text='3 курс', url='https://learnenglish.britishcouncil.org/grammar/b1-b2-grammar')
surl1 = InlineKeyboardButton(text='4 курс', url='https://learnenglish.britishcouncil.org/grammar/b1-b2-grammar')

selfkb.add(surl, surl1)
