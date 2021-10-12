from telebot import types
# #################main memnu
main_menu_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
main_menu_keyboard.add('🍔Fast Food🌮','🛒Savatcha')
main_menu_keyboard.add('⚙️Sozlamalar','ℹ️Biz haqimizda')
# ##################savatcha
savatcha_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
savatcha_keyboard.add('↗️Buyurtma berish','Davom etish')
savatcha_keyboard.add('🗑Savatni boshatish','🛒Savatcha')


# ###################settings
sozlamalar_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
sozlamalar_keyboard.add("Tilni o'zgartirish","Ismni o'zgartirish",'Saqlash')

# ##################contact
contact_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
contact_button=types.KeyboardButton('Contact ulashish',request_contact=(True))
contact_keyboard.add(contact_button)


####################til
language_markup=types.InlineKeyboardMarkup()
lang_button_uz=types.InlineKeyboardButton('🇺🇿Uzbek',callback_data='🇺🇿uzbek')
lang_button_ru=types.InlineKeyboardButton('🇷🇺Rus',callback_data='🇷🇺rus')
language_markup.add(lang_button_uz,lang_button_ru)

#######################rus usb markup
rus_usb_markup=types.ReplyKeyboardMarkup(resize_keyboard=(True))
rus_usb_markup.add('🇺🇿uzbek tili','🇷🇺rus tili')


#########################
products=['🫔Lavash','🌯Lavash cheese','🥞Burger','🍔Big Burger',
          '🌭HotDog','🥙Xotlet','🍜Shorva','🍕Pitsa','🍹Coca cola','🥤Pepsi','🧃Sharbat']


costs={'🫔Lavash':21000,'🌯Lavash cheese':23000,'🥞Burger':15000,'🍔Big Burger':18000,
       '🌭HotDog':12000,'🥙Xotlet':14000,'🍜Shorva':17000,'🍕Pitsa':47000,
       '🍹Coca cola':11000,'🥤Pepsi':11000,'🧃Sharbat':10000}
#!!!!!!!!!!!!!!!!###############
products_markup=types.InlineKeyboardMarkup()

def twoline(lists,markup):
    
            a,b=0,1
            while b<len(lists):
                but1=types.InlineKeyboardButton(lists[a],callback_data=lists[a])
                but2=types.InlineKeyboardButton(lists[b],callback_data=lists[b])
                markup.add(but1,but2)
                a+=2
                b+=2
            if a+1==len(lists):
                but=types.InlineKeyboardButton(lists[a],callback_data=lists[a])
                markup.add(but)
                
twoline(products, products_markup)


number_markup=types.InlineKeyboardMarkup(row_width=4)
b1=types.InlineKeyboardButton(1,callback_data=1)
b2=types.InlineKeyboardButton(2,callback_data=2)
b3=types.InlineKeyboardButton(3,callback_data=3)
b4=types.InlineKeyboardButton(4,callback_data=4)
b5=types.InlineKeyboardButton(5,callback_data=5)
b6=types.InlineKeyboardButton(6,callback_data=6)
b7=types.InlineKeyboardButton(7,callback_data=7)
b8=types.InlineKeyboardButton(8,callback_data=8)
b9=types.InlineKeyboardButton(9,callback_data=9)
b10=types.InlineKeyboardButton('Ortga',callback_data='Ortga')
number_markup.add(b1,b2,b3,b4)
number_markup.add(b5,b6,b7,b8)
number_markup.add(b9,b10)



















