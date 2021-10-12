from gtts import gTTS

import telebot
import os
bot=telebot.TeleBot("1806412813:AAE8WJU8HM7WoAr42t0t-KG0G_JO7Gh-YVI")

msg_text={}

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id,"Hello my friend welcome to me\nSend me your text and I will do it voice")
@bot.message_handler(content_types=['text'])

def texts(message):
    msg_text['text']=message.text
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=(True))
    markup.add("Slow and english","Fast and english")
    markup.add("Slow and russian","Fast and russian")

    
    msg=bot.reply_to(message,"Choice once",reply_markup=markup)
    bot.register_next_step_handler(msg,choice)
    
    
def choice(message):

    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=(True))
    markup.add("Slow","Fast")
    text=msg_text['text']
    tts1=gTTS(text=text,lang='en',slow=True)
    tts2=gTTS(text=text,lang='en',slow=False)
    tts3=gTTS(text=text,lang='ru',slow=True)
    tts4=gTTS(text=text,lang='ru',slow=False)
    a=tts1.save("DeCoder1.mp3")
    print(a)
    tts2.save("DeCoder2.mp3")
    tts3.save("DeCoder3.mp3")
    tts4.save("DeCoder4.mp3")
    audio1=open("DeCoder1.mp3",'rb')
    audio2=open("DeCoder2.mp3",'rb')
    audio3=open("DeCoder3.mp3",'rb')
    audio4=open("DeCoder4.mp3",'rb')
    # bot.send_audio(message.from_user.id, audio)
    if message.text=="Slow and english":
        msg=bot.send_audio(message.from_user.id, audio1)
        bot.send_message(message.from_user.id,"Send new text")
        # os.remove("C:/Users/Acer/Downloads/Telegram Desktop/DeCoder1.mp3")
        # bot.register_next_step_handler(msg,choice)
    elif message.text=="Fast and english":
        msg=bot.send_audio(message.from_user.id, audio2)
        # bot.register_next_step_handler(msg,choice)
        # os.remove("C:/Users/Acer/Downloads/Telegram Desktop/DeCoder2.mp3")
        bot.send_message(message.from_user.id,"Send new text")
    elif message.text=="Slow and russian":
        msg=bot.send_audio(message.from_user.id, audio3)
        # bot.register_next_step_handler(msg,choice)
        bot.send_message(message.from_user.id,"Send new text")
        # os.remove("C:/Users/Acer/Downloads/Telegram Desktop/DeCoder3.mp3")
        
    elif message.text=="Fast and russian":
        msg=bot.send_audio(message.from_user.id, audio4)
        # bot.register_next_step_handler(msg,choice)
        bot.send_message(message.from_user.id,"Send new text")
        # os.remove("C:\\Users\Acer\Downloads\Telegram Desktop\DeCoder4.mp3")
    
        
bot.polling(timeout=30000)