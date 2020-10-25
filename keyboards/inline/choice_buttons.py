from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.db import fruits
from keyboards.inline.callback_datas import buy_callback, choose_callback

# Вариант 1, как в прошлом уроке
# choice = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear")),
#         InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple")
#     ],
#     [
#         InlineKeyboardButton(text="Отмена", callback_data="next")
#     ]
# ])


# Вариант 2 - с помощью row_width и insert.

choose_item = InlineKeyboardMarkup(row_width=2)

for fruit in fruits:
    buy = InlineKeyboardButton(text=f"Buy {fruit.name}",
                               callback_data=choose_callback.new(id=fruit.id))
    choose_item.insert(buy)

cancel_button = InlineKeyboardButton(text="Hate fruits", callback_data="cancel")
choose_item.insert(cancel_button)

# choose_action = InlineKeyboardMarkup(row_width=2)
#
# buy = InlineKeyboardButton(text="Buy")
# choose_action.insert(buy)
#
# like_banana = InlineKeyboardButton(text=" Like it 👍", callback_data="buy:apple:5")
# choose_action.insert(like_banana)
#
# dislike_banana = InlineKeyboardButton(text="Hate  it 👎", callback_data="cancel")
# choose_action.insert(dislike_banana)
#
# share_with_friends = InlineKeyboardButton(text="Share with friend", callback_data="buy:apple:5")
# choose_action.insert(share_with_friends)
#
# back_to_menu = InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu")
# choose_action.insert(back_to_menu)
#
# А теперь клавиатуры со ссылками на товары
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url="https://rozetka.com.ua/champion_a00225/p27223057")
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url="https://freshmart.com.ua/product/yabloko-gala-116.html")
    ]
])
