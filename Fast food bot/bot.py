import telebot
from telebot import types
import mysql.connector

# from .db import *
from keyboards import (language_markup,contact_keyboard,main_menu_keyboard,
                    rus_usb_markup,products,costs,products_markup,number_markup,
                    savatcha_keyboard)
# a=main_menu_keyboard_func()


db=mysql.connector.connect(
    host='localhost',
    database='fast_food',
    user='root',
    password='root',
    port='3307'
)

cur=db.cursor()


class User:
    def __init__(self,user_id):
        self.user_id=user_id
        self.food=None
        self.number=None


user_data={}


# cur.execute('create table fast_food ( id INT AUTO_INCREMENT PRIMARY KEY, food_name VARCHAR(255), food_cost  INTEGER,food_photo VARCHAR(255), a varchar(255),b varchar(255),c varchar(255)  )')
# cur.execute('create table fast_food_users (id INT AUTO_INCREMENT PRIMARY KEY , name varchar(255), location varchar(255), a varchar(255),b varchar(255),c varchar(255)) ')



bot=telebot.TeleBot("2079783335:AAFymDFdnn1bEhNhmqD5XemZSUBTA1S-J-E")

@bot.message_handler(commands=['start'])
def welcome(message):
    sql='select * from fast_food_users where b=%s'
    val=(message.from_user.id,)
    cur.execute(sql,val)
    result=cur.fetchall()
    if len(result)==0:
        bot.send_message(message.from_user.id,"Assalom alekum\nTilni tanlang",reply_markup=language_markup)
    else:
        bot.send_message(message.from_user.id,"Assalom alekum",reply_markup=main_menu_keyboard)
        

@bot.callback_query_handler(func = lambda call: call.data in ['🇺🇿uzbek','🇷🇺rus'])
def lang(call):
    bot.delete_message(call.from_user.id,call.message.id)

    lang=call.data
 
    sql="insert into fast_food_users (a,b) values (%s,%s)"
 
    val=(lang,call.from_user.id)
 
    cur.execute(sql,val)

    db.commit()
    
    msg=bot.send_message(call.from_user.id,"Ismingizni kiriting\nMasalan : Mamarayim")
    bot.register_next_step_handler(msg,name)

@bot.callback_query_handler(func = lambda call: call.data in products)
def lang(call):
    bot.send_message(call.from_user.id,f"{call.data} narxi {costs[call.data]}\nSonini tanlang",reply_markup=number_markup)
    user=User(call.from_user.id)
    user.food=call.data
    user_data[call.from_user.id]=user
    bot.delete_message(call.from_user.id,call.message.id)
@bot.callback_query_handler(func = lambda call: call.data=='Ortga')
def number(call):
    bot.send_message(call.from_user.id,"Kerakli mahsulot tanlang",reply_markup=products_markup)
    
@bot.callback_query_handler(func = lambda call: int(call.data) in [1,2,3,4,5,6,7,8,9])
def number(call):
    bot.delete_message(call.from_user.id,call.message.id)
    user=user_data[call.from_user.id]
    user.number=call.data
    
    sql='insert into fast_food (food_name,food_cost,a) values (%s,%s,%s)'
    val=(user.food,user.number,call.from_user.id)
    cur.execute(sql,val)
    db.commit()

    bot.send_message(call.from_user.id,"Mahsulot savatchaga qo'shildi\nDavom eting\nBuyurtma berish uchun savatchaga o'ting",reply_markup=products_markup)
    user.food=None
    user.number=None
    user.user_id=None
    

@bot.message_handler(content_types=['contact'])
def finish(message):
    number=message.contact.phone_number
    sql='update fast_food_users set location=%s where b=%s'
    val=(number,message.from_user.id)
    cur.execute(sql,val)
    db.commit()   
    bot.send_message(message.from_user.id,"Muaffaqqiyatli ro'yxatdan o'tdingiz",reply_markup=main_menu_keyboard)


@bot.message_handler(func = lambda message:message.text=='ℹ️Biz haqimizda')
def aboutus(message):
    bot.send_message(message.from_user.id,"@Coder2002 "+'    +998916341985')

@bot.message_handler(func = lambda message:message.text=='⚙️Sozlamalar')
def settings(message):
    bot.send_message(message.from_user.id,"Sozlamalar",reply_markup=rus_usb_markup)
    
@bot.message_handler(func = lambda message:message.text=='🍔Fast Food🌮')
def foods(message):
    bot.send_message(message.from_user.id,"Tanlang",reply_markup=products_markup)

    
@bot.message_handler(func = lambda message:message.text=='🛒Savatcha')
def savat(message):
    bot.delete_message(message.from_user.id,message.message_id)
    cost=0
    text=''
    sql='select food_name,food_cost from fast_food where a=%s'
    val=(message.from_user.id,)
    cur.execute(sql,val)
    result=cur.fetchall()
    for res in result:
        text+=f"{res[1]} ta {res[0]}\n"
        cost+=costs[res[0]]*int(res[1])
        
    if cost>0:
        bot.send_message(message.from_user.id,text+f'Jami : {cost}',reply_markup=savatcha_keyboard)
    else:
        bot.send_message(message.from_user.id,"Savatcha bo'sh",reply_markup=main_menu_keyboard)
    
@bot.message_handler(func = lambda message:message.text in ['↗️Buyurtma berish','Davom etish','🗑Savatni boshatish'])
def svt(message):
    bot.delete_message(message.from_user.id,message.message_id)
    if message.text=='↗️Buyurtma berish':
        sql='delete from fast_food where a=%s'
        val=(message.from_user.id,)
        cur.execute(sql,val)
        db.commit()
        bot.send_message(message.from_user.id,"Buyurtma qabul qilindi",reply_markup=main_menu_keyboard)
        
    elif message.text=='Davom etish':
        bot.send_message(message.from_user.id,"Davom etishingiz mumkin",reply_markup=products_markup)
        
    elif message.text=='🗑Savatni boshatish':
        sql='delete from fast_food where a=%s'
        val=(message.from_user.id,)
        cur.execute(sql,val)
        db.commit()
        bot.send_message(message.from_user.id,"Savatcha bo'shatildi",reply_markup=main_menu_keyboard)
    
@bot.message_handler(func = lambda message:message.text in ['🇺🇿uzbek tili','🇷🇺rus tili'])
def aboutus(message):
    sql='update fast_food_users set a=%s where b=%s'
    if message.text=='🇺🇿uzbek tili':
        val=('🇺🇿uzbek',message.from_user.id)
    else:
        val=('🇷🇺rus',message.from_user.id)
    cur.execute(sql,val)
    db.commit()
    bot.send_message(message.from_user.id,"malumot o'zgartirildi",reply_markup=main_menu_keyboard)
    bot.delete_message(message.from_user.id,message.message_id)
def name(message):
    bot.delete_message(message.from_user.id,message.message_id)
    sql='update fast_food_users set name=%s where b=%s'
    val=(message.text,message.from_user.id)
    cur.execute(sql,val)
    db.commit()
    
    bot.send_message(message.from_user.id,"Telefon nomeringizni yuboring",reply_markup=contact_keyboard)
    
   

    
bot.polling(none_stop=True)
    

