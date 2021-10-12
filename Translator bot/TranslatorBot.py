from translate import Translator
import telebot 

from PIL import Image 
import pytesseract

bot=telebot.TeleBot("1827592811:AAGEgPaNGKQKBIWutDokCPsAbN0WrA0FyWI")

@bot.message_handler(commands=['start'])
def srt(message):
    bot.send_message(message.chat.id,"Assalom alekum men translator botman\nO'zingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng")


@bot.message_handler(commands=['uz_eng'])
def uzeng(message):

        msg=bot.send_message(message.from_user.id,"Marhamat o'zbekcha tekstingizni kiriting:")
        bot.register_next_step_handler(msg,uz_eng)


def uz_eng(message):
    
    
    translator= Translator(from_lang='uz',to_lang="en")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    bot.send_message(message.from_user.id,'ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')
    # bot.register_next_step_handler(msg,uz_eng)
    
@bot.message_handler(commands=['eng_uz'])
def uzeng(message):
        msg=bot.send_message(message.from_user.id,"Send me your english text:")
        bot.register_next_step_handler(msg,eng_uz)


def eng_uz(message):
    
    
    translator= Translator(from_lang='en',to_lang="uz")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    # bot.register_next_step_handler(msg,eng_uz)
    bot.send_message(message.from_user.id,'Ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')
    

@bot.message_handler(commands=['uz_ru'])
def uzeng(message):
        msg=bot.send_message(message.from_user.id,"Tekstingizni yuboring:")
        bot.register_next_step_handler(msg,uz_ru)


def uz_ru(message):
    
    
    translator= Translator(from_lang='uz',to_lang="ru")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    # bot.register_next_step_handler(msg,eng_uz)
    bot.send_message(message.from_user.id,'Ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')

@bot.message_handler(commands=['ru_uz'])
def uzeng(message):
        msg=bot.send_message(message.from_user.id,"Отправьте свой текст:")
        bot.register_next_step_handler(msg,ru_uz)


def ru_uz(message):
    
    
    translator= Translator(from_lang='ru',to_lang="uz")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    # bot.register_next_step_handler(msg,eng_uz)
    bot.send_message(message.from_user.id,'Ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')



@bot.message_handler(commands=['eng_ru'])
def uzeng(message):
        msg=bot.send_message(message.from_user.id,"Send your text to me:")
        bot.register_next_step_handler(msg,eng_ru)


def eng_ru(message):
    
    
    translator= Translator(from_lang='en',to_lang="ru")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    # bot.register_next_step_handler(msg,eng_uz)
    bot.send_message(message.from_user.id,'Ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')



@bot.message_handler(commands=['ru_eng'])
def uzeng(message):
        msg=bot.send_message(message.from_user.id,"Отправьте свой текст:")
        bot.register_next_step_handler(msg,ru_eng)


def ru_eng(message):
    
    
    translator= Translator(from_lang='ru',to_lang="en")
    translation = translator.translate(message.text)
    msg=bot.send_message(message.from_user.id,translation )
    # bot.register_next_step_handler(msg,eng_uz)
    bot.send_message(message.from_user.id,'Ozingizga kerakli buruqni tanlang \n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng')







@bot.message_handler(content_types=['text'])
def oood(message):
    bot.reply_to(message,"Avval kerakli buruqni tanlang\n/uz_eng   /eng_uz\n/uz_ru   /ru_uz\n/eng_ru   /ru_eng")
import os
@bot.message_handler(content_types=['photo'])
def oood(message):
    
    # img = Image.open('silence_poem.jpg')
    print(message)
    # message.photo[-1
    fileID = message.photo[-1].file_id

    
    img=bot.get_file(fileID)
    print(img)
    download=bot.download_file(img.file_path)
    # 
    # print(img)
    src='photos/'+fileID+'.jpg'
    # os.open()
  
    rasm=open(img.file_path,'rb')
    result = pytesseract.image_to_string(img.file_path)
    
    
    
    
    
bot.polling(none_stop=(True))