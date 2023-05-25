from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton

b1 = KeyboardButton('🔍 Искать')

b2 = KeyboardButton("❌стоп")

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1)

stop_menu = ReplyKeyboardMarkup(resize_keyboard=True)
stop_menu.add(b2)