from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters.builtin import Regexp
from dataclasses import dataclass


@dataclass
class BetData:
    amount: int
    num_range: list


class MyError(Exception):
    message: str

    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(*args)


def check_range_number(n: int) -> bool:
    if n < 0 or n > 12:
        raise MyError("Число дожно быть от 0 до 12")
    else:
        return True


def parse_bet_message(text: str) -> BetData:

    info_raw = text.split(" ")[:2]
    a_raw = info_raw[0]
    amount = int(a_raw)
    if amount < 1:
        raise MyError("Минимальная ставка - 1")

    # 1 | 1-2
    # [1000, 10 12]
    # 1000 ewrdf
    range_raw = info_raw[1].split("-")
    if len(range_raw) == 1:  # ситуация `100 1`
        from_ = int(range_raw[0])
        check_range_number(from_)
        return BetData(amount=amount, num_range=[from_])
    elif len(range_raw) == 2:  # ситуация `100 1-` ["1", ""]
        from_ = int(range_raw[0])
        to_ = int(range_raw[1])
        return BetData(amount=amount, num_range=[from_, to_])
    else:
        raise MyError("Что-то пошло не так")


@dp.message_handler(Regexp(r"^\d+\s(\d+)-(\d+)|^\d+\s(\d+)"))
async def roulette(m: types.Message):
    try:
        bet_data = parse_bet_message(m.text.lower().replace('\\', ""))
        amount = bet_data.amount
        num_range = bet_data.num_range
    except MyError as my_error_instance:
        await m.reply(my_error_instance.message)
        return
    if len(num_range) == 1:
        await m.answer(f"Вы поставили {amount} на {num_range[0]}")
    elif len(num_range) == 2:
        await m.answer(f"Вы поставили {amount} на {num_range[0]}-{num_range[1]}")


