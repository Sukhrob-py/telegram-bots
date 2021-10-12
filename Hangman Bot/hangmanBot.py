import telebot,random,time
from telebot import types


bot=telebot.TeleBot("1901437887:AAH0DZXWHyWgLtSGZAsr8fx2NXVJGO2dNYU")
kiritilganlar=''
user_data={}
word=None
javob=''
words=['acer','iphone','shoxruh','compyuter']
class User:
    def __init__(self,user_id):
        self.user_id=user_id
        
imkoniyat=7   
@bot.message_handler(commands=['start'])
def welcome(msg):
    global word,imkoniyat,kiritilganlar
    kiritilganlar=''
    imkoniyat=7
    word=random.choice(words)
    len_=len(word)
    bot.send_message(msg.chat.id,f"Asssalom alekum\nHangman o'yiniga xush kelibsiz\n{len_} harfli so'z yashirilgan shuni topish uchun biron harf yuboring")
    

@bot.message_handler(content_types=['text'])
def hangman(msg):
    global javob,kiritilganlar,word,imkoniyat
    
    if len(msg.text)>1:
        bot.reply_to(msg,"Iltimos bitta harf kiriting")
        
    else:
        kiritilganlar+=msg.text.lower()
        if imkoniyat>0:
            wrong=0
            for char in word:
                if char in kiritilganlar:
                    javob+=char
                    
                else:
                    javob+='_'
                    wrong+=1
            bot.send_message(msg.chat.id,javob)
            if '_' in javob:
                bot.send_message(msg.chat.id,"Harf yuboring")
            javob=''
            if wrong==0:
                bot.send_message(msg.chat.id,"Siz yutdingiz\nYana o'ynamoqchi bo'lsabgiz /start commandasini yozing")
                
            
            if msg.text.lower() not in word:
                imkoniyat-=1
                bot.send_message(msg.chat.id,f"Sizda {imkoniyat} ta imkoniyat qoldi")
                
            if imkoniyat==0:
                bot.send_message(msg.chat.id,"Yutqazdingiz(\nYana o'ynashni xohlasangiz /start commandasini yozing")
                

                
bot.polling()
                
                
                    
                    
                    
                    