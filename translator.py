import logging
from aiogram import Bot, Dispatcher, executor, types
from defs import getDefs
from googletrans import Translator
import wikipedia
translator=Translator()

key='9c6f63862b5f860e0e454fdf4dd4e566'
id='49dd63a7'
language='en-gb'
api='5319758957:AAE3I-VUqcyM87g_hO-Al1yhsUa-Lv5pjrY'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=api)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi\nI'm translatorbot")

@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)

    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        dest='uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id=message.text
        else:
            word_id= translator.translate(message.text, dest='en').text
        lookup=getDefs(word_id)
        if lookup:
            await message.reply(f"word: {word_id} \Definitions:{lookup['diff']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("bunday soz yoq")

wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
