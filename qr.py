from io import BytesIO
import qrcode
from aiogram import Bot, Dispatcher, executor, types
import logging
import environs

from transliterate import to_latin, to_cyrillic
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

env = environs.Env()
env.read_env()
TOKEN = env.str("TOKEN")

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# logging.basicConfig(level=logging.INFO)


class Cyrillic2latin(StatesGroup):
    cyrillic2latin = State()


class Qr(StatesGroup):
    qr = State()


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', "Start the bot"),
            types.BotCommand('cyrillic2latin', "Transliterate text cyrillic <> latin"),
            types.BotCommand('qr', "Generate qr code from the text"),
        ]
    )


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reply = f"Hello {message.from_user.full_name}! Bot started! Choose options from menu"
    await message.answer(reply)


@dp.message_handler(commands=['cyrillic2latin'], state=None)
async def cyrillic2latin(message: types.Message):
    await message.answer(text="Insert text to transliterate from cyrillic <> latin")
    await Cyrillic2latin.cyrillic2latin.set()


@dp.message_handler(state=Cyrillic2latin.cyrillic2latin)
async def cyrillic2latin_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cyrillic2latin'] = message.text

        if data['cyrillic2latin'].isascii():
            reply = to_cyrillic(data['cyrillic2latin'])
        else:
            reply = to_latin(data['cyrillic2latin'])

        await message.answer(reply)
        await state.finish()


@dp.message_handler(commands=['qr'], state=None)
async def qr(message: types.Message):
    await message.answer(text="Insert url to generate qr code")
    await Qr.qr.set()


@dp.message_handler(state=Qr.qr)
async def qr_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['qr'] = message.text

        qr_img = qrcode.make(data['qr'])
        bio = BytesIO()
        qr_img.save(bio, 'JPEG')
        bio.seek(0)

        await message.answer_photo(bio, caption=f"qr code of {data['qr']}")
        await state.finish()


executor.start_polling(dp)
