import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.db import fruits
from keyboards.inline.callback_datas import buy_callback, choose_callback, like_callback, dislike_callback
from keyboards.inline.choice_buttons import pear_keyboard, apples_keyboard, choose_item
from loader import dp


# по команде item отображаем фото магазина и меню с выбором товара. Меню генерируется исходя из того, какие товары
# находятся в базе данных (просто массив в db.py)
@dp.message_handler(Command("item"))
async def show_items(message: Message):
    await message.answer_photo(photo="https://i.pinimg.com/originals/88/96/32/88963271b64bb94ce4c404471434cc07.jpg",
                               caption="FRUITS SHOP",
                               reply_markup=choose_item)


# Поскольку не назначен аргумент для нашего фильтра, в хэндлер будут попадать все, что назначается
# для этого коллбэка
@dp.callback_query_handler(choose_callback.filter())
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    choose_action = InlineKeyboardMarkup(row_width=2)
    id = callback_data.get('id')
    fruit = fruits[int(id)]
    # создаем кнопки для меню
    buy_item = InlineKeyboardButton(text="Buy", callback_data=buy_callback.new(id=id))
    choose_action.insert(buy_item)
    like_item = InlineKeyboardButton(text="👍", callback_data=like_callback.new(id=id))
    choose_action.insert(like_item)
    dislike_item = InlineKeyboardButton(text="👎", callback_data=dislike_callback.new(id=id))
    choose_action.insert(dislike_item)
    # для того, чтобы поделиться используем switch_inline_query
    share = InlineKeyboardButton(text="Share it", switch_inline_query=f"Buy {fruit.name} in our shop!")
    choose_action.insert(share)

    await call.message.answer_photo(photo=fruit.photo,
                                    caption=f"This is  {fruit.name}. Buy and eat it", reply_markup=choose_action)


@dp.callback_query_handler(buy_callback.filter())
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    id = callback_data.get('id')
    fruit = fruits[int(id)]
    await call.message.answer_photo(photo=fruit.photo,
                                    caption=f"You bought the fruit with id {fruit.id}", reply_markup=None)


@dp.callback_query_handler(like_callback.filter())
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    id = callback_data.get('id')
    fruit = fruits[int(id)]
    # меняем рейтинг с помощью метода like обьекта Fruit()
    fruit.like()
    await call.message.answer_photo(photo=fruit.photo,
                                    caption=f"You liked  fruit with id {fruit.id}. Now its rating is {fruit.rating}",
                                    reply_markup=None)


@dp.callback_query_handler(dislike_callback.filter())
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    id = callback_data.get('id')
    fruit = fruits[int(id)]
    # меняем рейтинг с помощью метода dislike обьекта Fruit()
    fruit.dislike()
    await call.message.answer_photo(photo=fruit.photo,
                                    caption=f"You liked  fruit with id {fruit.id}. Now its rating is {fruit.rating}",
                                    reply_markup=None)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили эту покупку!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)