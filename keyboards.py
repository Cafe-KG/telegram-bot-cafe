from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_MACBOOK, URL_IPHONE13


cb = CallbackData('buy', 'id', 'name')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Restoran', callback_data='buy:0:restoran'),
            InlineKeyboardButton(text='Bar', callback_data='buy:1:bar'),
            InlineKeyboardButton(text='Cafe', callback_data='buy:2:cafe'),
            InlineKeyboardButton(text='Fast-food', callback_data='buy:3:fast-food')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

restoran_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Navat', url=URL_IPHONE13),
            InlineKeyboardButton('Navigator', url=URL_IPHONE13)
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

bar_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Riders', url=URL_MACBOOK),
            InlineKeyboardButton('Oblako 53', url=URL_MACBOOK)
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

cafe_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Faiza', url=URL_MACBOOK),
            InlineKeyboardButton('Mustafa', url=URL_MACBOOK)
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

fast_food_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('KFC', url=URL_IPHONE13),
            InlineKeyboardButton('BFC', url=URL_IPHONE13)
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)
