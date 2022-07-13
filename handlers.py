from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from keyboards import (
    restoran_key, bar_key, keyboard1,
    cb, cafe_key, fast_food_key
)
from main import bot, dp
from config import chat_id
from cafe import CafeSubscribe, price1, price2


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Здравствуйте, это Cafe.kg! \n'
                                                 '/cafe-Тип общественного питания \n'
                                                 '/buy-Покупка подписки на сайте')


@dp.message_handler(Command('cafe'))
async def show(message: Message):
    await message.answer(text='Выберите тип общественного питания: ', reply_markup=keyboard1)


@dp.callback_query_handler(text_contains='restoran')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Ресторан', reply_markup=restoran_key)


@dp.callback_query_handler(cb.filter(name='bar'))
async def mac(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Бар', reply_markup=bar_key)


@dp.callback_query_handler(text_contains='cafe')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Кафе', reply_markup=cafe_key)


@dp.callback_query_handler(text_contains='fast-food')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Фаст-Фуд', reply_markup=fast_food_key)


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(Command('buy'), state=None)
async def shop(message: Message):
    await message.answer('Какую подписку вы хотите купить: \n'
                         '1 - подписка \n'
                         '2 - подписка \n')

    await CafeSubscribe.step1.set()


@dp.message_handler(state=CafeSubscribe.step1)
async def shop(message: Message, state: FSMContext):
    item = message.text
    await state.update_data(
        {
            'item': item
        }
    )

    await message.answer('Сколько вас интересует?')
    await CafeSubscribe.next()


@dp.message_handler(state=CafeSubscribe.step2)
async def count(message: Message, state: FSMContext):
    data = await state.get_data()
    item = data.get('item')
    if item == '1':
        p = price1
    else:
        p = price2

    count = int(message.text)

    await message.answer(f'Супер! С вас: {p*count}')

    await state.finish()
