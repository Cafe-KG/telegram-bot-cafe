from aiogram.dispatcher.filters.state import StatesGroup, State


class CafeSubscribe(StatesGroup):
    step1 = State()
    step2 = State()


price1 = 100
price2 = 500
