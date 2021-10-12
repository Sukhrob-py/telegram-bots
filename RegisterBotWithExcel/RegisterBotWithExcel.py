# register 

import telebot
import telebot.types
import mysql.connector

from pymysql import * 
import xlwt 
import pandas.io.sql as sql


db=mysql.connector.connect(
    user="root",
    host="localhost",
    password="root",
    port="3307",
    database="registartsiya")


cursor=db.cursor()

# cursor.execute("create table register3 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), phone VARCHAR(255), user_id VARCHAR(255) )")



markup=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add("Tekshirish")

class User:
    def __init__(self,name):
        self.name=name
        self.surname=None
        self.phone=None
        self.user_id=None
        
bot=telebot.TeleBot("1757005090:AAGncM7NkcROa31qMORyqPrDMAPE4Od3ZRg")
# engMoview
chat_id='@engMoview'  
user_data={}
possible_statuses=['creator','administrator','member']
possible_statuses1=['left']

@bot.message_handler(commands=['start'])
def welcome(message):
    aa=f"SELECT id FROM register3 WHERE user_id={message.from_user.id}"
    cursor.execute(aa)
        # db.commit()
    result=cursor.fetchall()
    x=0
    for i in result:
        x+=1
        
    if x==7:
        msg=bot.send_message(message.from_user.id,"Assalom alekum\nRo'yxatdan o'tish uchun ismingizni kiriting")
        bot.register_next_step_handler(msg,surname)
       
                    
    else:
        aa=f"SELECT id FROM register3 WHERE user_id={message.from_user.id}"
        cursor.execute(aa)
        # db.commit()
        result=cursor.fetchall()
        print(result)
        result=str(result)
        markup4=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        markup4.add("Databaseni excel formatda ko'chirib olish")
        # user=user_data[message.from_user.id]
    
        chek_user=bot.get_chat_member(chat_id,message.from_user.id)
        if chek_user.status in ['creator','administrator','owner']:
            bot.send_message(message.from_user.id,f"Siz avval ro'yxatdan o'tgansiz\nSizning id :{(result[2])}",reply_markup=markup4)
        else:
            bot.send_message(message.from_user.id,f"Siz avval ro'yxatdan o'tgansiz\nSizning id :{(result[2])}")

def surname(message):
    user_data[message.from_user.id]=User(message.text)
    msg=bot.send_message(message.from_user.id,"Familiyangizni kiriting:")
    bot.register_next_step_handler(msg,phone)
    
def phone(message):
    user=user_data[message.from_user.id]
    user.surname=message.text        
    markup1=telebot.types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True,one_time_keyboard=True)
    button_phone=telebot.types.KeyboardButton(text="Nomer jo'natish",request_contact=True)
    markup1.add(button_phone)
    msg=bot.send_message(message.from_user.id,"nomeringizni yuboring:",reply_markup=markup1)
    
    
    
    
    bot.register_next_step_handler(msg,jointochannel)    

def jointochannel(message):
    
    try:
        user=user_data[message.from_user.id]
        user.phone=message.contact.phone_number
        
        
    except:
        user=user_data[message.from_user.id]
        user.phone=message.text
    markupinline=telebot.types.InlineKeyboardMarkup()

    item1 = telebot.types.InlineKeyboardButton("Kanalga a'zo bo'lish", url='https://t.me/engMoview')
 
    item2 = telebot.types.InlineKeyboardButton("azo boldm", callback_data='azo')

    markupinline.add(item1,item2)
    markup2=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    markup2.add("Azo boldim")
    msg=bot.send_message(message.from_user.id,"Botdan foydalanish uchun\nKanalga a'zo bo'ling",reply_markup=markupinline)
    # msg=bot.send_message(message.from_user.id,"A'zo bo'ling",reply_markup=markup2)

    
    bot.register_next_step_handler(msg,result)
    
@bot.callback_query_handler(func=lambda call:True)
def call(call):
    
        user=user_data[call.from_user.id]
    
        chek_user=bot.get_chat_member(chat_id,call.from_user.id)  
        print(chek_user)
        user.user_id=call.from_user.id

        if chek_user.status in possible_statuses :
        # con=connect(user="root",password="root",port=3307,host="localhost",database="registartsiya")
   
        # ids=sql.read_sql(f'select id from register2 where user_id={user.user_id} ',con)
        
        # print(ids)
        
            aa=f"SELECT id FROM register3 WHERE user_id={call.from_user.id}"
            cursor.execute(aa)
        # db.commit()
            result=cursor.fetchall()
        # x=0
        # for i in result:
        #     x+=1
            
        # print(x)
        # count=cursor.rowcount
            print(f"sizni soningiz:{result}")
        
        
        
            markup4=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
            markup4.add("Databaseni excel formatda ko'chirib olish")
            if chek_user.status in ['creator','administrator','owner']:
                mysql="insert into register3 (name,surname,phone,user_id) values (%s,%s,%s,%s)"
                val=(user.name,user.surname,user.phone,user.user_id)
                cursor.execute(mysql,val)
                db.commit()
                aa=f"SELECT id FROM register3 WHERE user_id={call.from_user.id}"
                cursor.execute(aa)
        # db.commit()
                result=cursor.fetchall()
                result=str(result)
                msg=bot.send_message(call.from_user.id,f"Muvaffaqqiyatli ro'yxatdan o'tdingiz\nSizning id ingiz :{result[2]} ",reply_markup=markup4)

            # bot.register_next_step_handler(msg,excel)
            else:
            
                mysql="insert into register3 (name,surname,phone,user_id) values (%s,%s,%s,%s)"
                val=(user.name,user.surname,user.phone,user.user_id)
                cursor.execute(mysql,val)
                db.commit()
                aa=f"SELECT id FROM register3 WHERE user_id={call.from_user.id}"
                cursor.execute(aa)
        # db.commit()
                result=cursor.fetchall()
                result=str(result)
                bot.send_message(call.from_user.id,f"Muvaffaqqiyatli ro'yxatdan o'tdingiz\nSizning id ingiz :{result[2]} ")
        else:
            msg=bot.send_message(call.from_user.id,"Siz guruhda mavjud emassiz\nAvval guruhga azo bo'ling",reply_markup=markup)
            bot.register_next_step_handler(msg,check)
    
    
def check(message):
    user=user_data[message.from_user.id]
    if message.text=="Tekshirish":
        chek_user=bot.get_chat_member(chat_id,message.from_user.id)    
    
        if chek_user.status in possible_statuses :
            aa=f"SELECT id FROM register3 WHERE user_id={message.from_user.id}"
            cursor.execute(aa)
        # db.commit()
            result=cursor.fetchall()
            mysql="insert into register2 (name,surname,phone,user_id) values (%s,%s,%s,%s)"
            val=(user.name,user.surname,user.phone,user.user_id)
            cursor.execute(mysql,val)
            db.commit()
            markup4=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
            markup4.add("Databaseni excel formatda ko'chirib olish")
            # bot.send_message(message.from_user.id,"Malumotlar bazasini ko'chirib olishingiz mumkin",reply_markup=markup4)
            if chek_user.status in ['administrator','creator','owner']:
                aa=f"SELECT id FROM register3 WHERE user_id={message.from_user.id}"
                cursor.execute(aa)
        # db.commit()
                result=cursor.fetchall()
                result=str(result)
                msg=bot.send_message(message.from_user.id,f"Muvaffaqqiyatli ro'yxatdan o'tdingiz\nSizning id ingiz {result[2]} ",reply_markup=markup4)
                # bot.register_next_step_handler(msg,excel)
                
            else:
                bot.send_message(message.from_user.id,f"Muvaffaqqiyatli ro'yxatdan o'tdingiz\nSizning id ingiz{result[2]} ")

        else:
            bot.send_message(message.from_user.id,"Hali azo bo'lmadingiz")


@bot.message_handler(content_types=['text'])
def excel(message):
    if message.text=="Databaseni excel formatda ko'chirib olish":
        con=connect(user="root",password="root",port=3307,host="localhost",database="registartsiya")
# read the data
        df=sql.read_sql('select * from register3',con)
# print the data
        print(df)
# export the data into the excel sheet
        excel=df.to_excel('registartsiya.xls')
        doc=open('registartsiya.xls','rb')
    # print(excel)
        bot.send_document(message.from_user.id,doc )
        
bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()










bot.polling(none_stop=True)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
