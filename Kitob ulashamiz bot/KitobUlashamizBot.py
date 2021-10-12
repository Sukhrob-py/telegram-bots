try:   
    import telebot
    from telebot import types
    
    
    import mysql.connector
    
    
    db=mysql.connector.connect(
        host='localhost',
        database='registartsiya',
        user='root',
        password='root',
        port="3307"
    )
    
    cur=db.cursor()
    # cur.execute("create table books (id INT AUTO_INCREMENT PRIMARY KEY, book_name VARCHAR(255), author VARCHAR(255), rent_time VARCHAR(255), rent_cost VARCHAR(255),about_book varchar(255),photo_id varchar(255),user_id varchar(255) )")
    
    class User:
        def __init__(self,photo_id):
            self.photo_id=photo_id
            
            
    user_data={}
    
    
    
    
    
    
    
    
    
    
    bot=telebot.TeleBot("1768565507:AAGEnvmeujwWhXBCcQ4IJU3-0MqvyAUAoDs")
    
    # markup request contact
    markup_contact=types.ReplyKeyboardMarkup(resize_keyboard=(True))
    button=types.KeyboardButton("📞 Nomer yuborish",request_contact=(True))
    markup_contact.add(button)
    
    # markup request contact rus
    markup_contact_rus=types.ReplyKeyboardMarkup(resize_keyboard=(True))
    button=types.KeyboardButton("📞 Отправить номер",request_contact=(True))
    markup_contact_rus.add(button)
    
    
    # uzb rus inline keyboard
    markup_uzb_ru=types.InlineKeyboardMarkup()
    button_uz=types.InlineKeyboardButton("Uzbek",callback_data="Uzbek")
    button_ru=types.InlineKeyboardButton("Rus",callback_data="Rus")
    markup_uzb_ru.add(button_uz,button_ru)
    
    # inline markup region
    regions=["Andijon viloyati","Jizzax viloyati","Navoiy viloyati","Samarqand viloyati",
             "Sirdaryo viloyati","Toshkent viloyati","Xorazm viloyati","Buxoro viloyati",
             "Qashqadaryo viloyati","Namangan viloyati","Surxondaryo viloyati","Toshkent shahar",
             "Farg'ona viloyati","Qoraqalpog'iston Resp."]
    markup_region=types.InlineKeyboardMarkup(row_width=2)
    lang=None
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
                
    
    
    
    
    twoline(regions,markup_region)
    
    # inline merkup district
    districts_Andijon=["Andijon shahar","Qorasuv shahar","Andijon tumani","Bo'z tumani","Jalolquduq tumani",
                       "Ulug'nor tumani","Asaka tumani","Shahrixon tumani","Xo'jaobod tumani","Xonobod shahar",
                       "Oltinko'l tumani","Baliqchi tumani","Buloqboshi tumani","Izboskan tumani","Qo'rg'ontepa tumani",
                       "Marhamat tumani","Paxtaobod tumani","Ortga"]
    districts_Jizzax=["Arnasoy tumani","G'allaorol tumani","Do'stlik tumani","Zomin tumani","Mirzacho'l tumani",
                       "Forish tumani","Yangiobod tumani","Baxmal tumani","Sharof Rashidov tumani","Zarbdor tumani",
                       "Zafarobod tumani","Paxtakor tumani","Jizzax shahar","Ortga"]
    districts_Navoiy=["Navoiy shahar","Uchquduq shahar","Qiziltepa tumani","Navbahor tumani","Nurota tumani",
                       "Zarafshon shahar","Konimex tumani","Tomdi tumani","Xatirchi tumani","Karmana shahar","Ortga"]
    districts_Samarqand=["Samarqand shahar","Kattaqo'rg'on shahar","Bulung'ur tumani","Ishtihon tumani","Qo'shrabod tumani",
                       "Qayariq tumani","Paxtachi tumani","Nurobod tumani","Toyloq tumani","Oqdaryo tumani",
                       "Jomboy tumani","Kattaqo'rg'on tumani","Narpay tumani","Pastdarg'om tumani","Samarqand tumani",
                       "Urgut tumani","Ortga"]
    districts_Sirdaryo=["Shirin shahar","Guliston shahar","Yangiyer shahar","Oqoltin tumani","Guliston tumani",
                       "Mirzaobod tumani","Sirdaryo tumani","Sardoba tumani","Boyovut tumani","Mehnatobod tumani",
                        "Sayxunobod tumani","Xovos tumani","Ortga"]
    districts_Toshkent_vil=["Nurafshon shahar","Chirchiq shahar","Olmaliq shahar","Angren shahar","Yangiyo'l shahar",
                       "Ohangaron shahar","Bekobod shahar","Bekobod tumani","Bo'stonliq tumani","Yuqori Chirchiq tumani",
                       "Oqqo'rg'on tumani","Parkent tumani","Toshkent tumani","Chinoz tumani","Yangiyo'l tumani",
                       "Bo'ka tumani","Zangiota tumani","Qibray tumani","Ohangaron tumani","Piskent tumani",
                       "O'rta Chirchiq tumani","Quyi Chirchiq tumani","Ortga"]
    districts_Xorazm=["Urganch shahar","Xiva shahar","Pitnak tumani","Xiva tumani","Gurlan tumani",
                      "Yangiariq tumani","Bog'ot tumani","Yangibozor tumani","Urganch tumani","Xozarasp tumani",
                      "Shovot tumani","Qo'shko'pir tumani","Xonqa tumani","Ortga"]
    districts_Buxoro=["Buxoro shahar","Kogon shahar","Olot tumani","Vobkent tumani","Jondor tumani",
                      "Qorako'l tumani","Romitan tumani","Qorovulbozor tumani","Buxoro tumani","G'ijduvon tumani",
                      "Kogon tumani","Peshku tumani","Shofirkon tumani","Ortga"]
    districts_Qashqadaryo=["Qarshi shahar","Shahrisabz shahar","G'uzor tumani","Qamashi tumani","Koson tumani",
                       "Muborak tumani","Kasbi tumani","Shahrisabz tumani","Mirishkor tumani","Dehqonobod tumani",
                       "Qarshi tumani","Kitob tumani","Nishon tumani","Yakkabog' tumani","Chiroqchi tumani","Ortga"]
    districts_Namangan=["Namangan shahar","Kosonsoy tumani","Norin tumani","To'raqo'rg'on tumani","Uchqo'rg'on tumani",
                      "Chust tumani","Mingbuloq tumani","Namangan tumani","Pop tumani","Uychi tumani",
                      "Chortoq tumani","Yangiqo'rg'on tumani","Ortga"]
    districts_Surxondaryo=["Termiz shahar","Oltinsoy tumani","Muzrabod tumani","Jarqo'rg'on tumani","Qiziriq tumani",
                       "Termiz tumani","Sho'rchi tumani","Bandixon tumani","Angor tumani","Boysun tumani",
                       "Denov tumani","Qumqo'rg'on tumani","Sariosiyo tumani","Sherabod tumani","Uzun tumani","Ortga"]
    districts_Toshkent_shah=["Mirobod tumani","Yunusobod tumani","Shayxontohur tumani","Sirg'ali tumani","Olmazor tumani",
                       "Bektemir tumani","Mirzo Ulug'bek tumani","Yakkasaroy tumani","Chilonzor tumani","Yashnobod tumani","Uchtepa tumani","Ortga"]
    districts_Fargona=["Quvasoy shahar","Marg'ilon shahar","Qo'qon shahar","Farg'ona shahar","Beshariq tumani",
                       "Buvayda tumani","Yozyovon tumani","Oltiariq tumani","Rishton tumani","Toshloq tumani",
                       "Uchko'prik tumani","Furqat tumani","Bog'dod tumani","Dangara tumani","Quva tumani",
                       "Qo'shtepa tumani","Sho'x tumani","O'zbekiston tumani","Farg'ona tumani","Ortga"]
    districts_Qoraqalpoq=["Nukus shahar","Beruniy tumani","Qo'ng'rot tumani","Muynoq tumani","Taxtako'prik tumani",
                      "Xo'jayli tumani","Shumanay tumani","Qorauzuk tumani","Amudaryo tumani","Kegeyli tumani",
                      "Qonliko'l tumani","Nukus tumani","To'rtko'l tumani","Chimboy tumani","Ellikq'ala tumani","Taxiatosh tumani","Ortga"]
    
    markup_orqa_rus=types.ReplyKeyboardMarkup(one_time_keyboard=(True),resize_keyboard=True)
    markup_orqa_rus.add("Изменить данные")
    markup_orqa_rus.add("Удалить книгу")
    markup_orqa_rus.add("Назад")
    
    markup_dist_Andijon=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Andijon,markup_dist_Andijon)
    markup_dist_Jizzax=types.InlineKeyboardMarkup(row_width=2)
    twoline(districts_Jizzax,markup_dist_Jizzax)
    
    markup_dist_Navoiy=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Navoiy,markup_dist_Navoiy)
    markup_dist_Samarqand=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Samarqand,markup_dist_Samarqand)
    markup_dist_Sir=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Sirdaryo,markup_dist_Sir)
    markup_dist_T_vil=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Toshkent_vil,markup_dist_T_vil)
    markup_dist_Xorazm=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Xorazm,markup_dist_Xorazm)
    markup_dist_Buxoro=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Buxoro,markup_dist_Buxoro)
    markup_dist_Qash=types.InlineKeyboardMarkup(row_width=2)
    twoline(districts_Qashqadaryo,markup_dist_Qash)
    markup_dist_Nam=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Namangan,markup_dist_Nam)
    markup_dist_Sur=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Surxondaryo,markup_dist_Sur)
    markup_dist_Tshah=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Toshkent_shah,markup_dist_Tshah)
    markup_dist_Far=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Fargona,markup_dist_Far)
    markup_dist_Qoraqalp=types.InlineKeyboardMarkup(row_width=2)
    
    twoline(districts_Qoraqalpoq,markup_dist_Qoraqalp)
    
    # markup about me rus
    markup_about_me_rus=types.ReplyKeyboardMarkup(resize_keyboard=(True))
    
    
    markup_about_me_rus.add("Имя","Фамилия")
    markup_about_me_rus.add("Телефонный номер")
    markup_about_me_rus.add("Изменить язык")
    markup_about_me_rus.add("Сохранить")
    
    # markup about me 
    markup_about_me=types.ReplyKeyboardMarkup(resize_keyboard=(True))
    
    
    markup_about_me.add("🖌 Ism","🖍 Familiya")
    markup_about_me.add("☎️ Telefon nomer")
    markup_about_me.add("🇸🇱 Tilni o'zgartirish 🇷🇺")
    markup_about_me.add("✔️ Saqlash")
    
    
    # markup language
    markup_new_lang=types.ReplyKeyboardMarkup(resize_keyboard=(True))
    markup_new_lang.add("Uzbek","Rus")
    
    # menu markup
    markup_menu=types.ReplyKeyboardMarkup(resize_keyboard=(True),one_time_keyboard=(True))
    markup_menu.add("🔎 Kitob qidirish","➕ Kitob qo'shish")
    markup_menu.add("📚 Mening kutubxonam","⚙️ Sozlamalar")
    markup_menu.add("📱 Biz bilan bog'lanish")
    
    
    # menu markup rus
    markup_menu_rus=types.ReplyKeyboardMarkup(resize_keyboard=(True),one_time_keyboard=(True))
    markup_menu_rus.add("Книжный поиск","Добавить книгу")
    
    markup_menu_rus.add("Моя библиотека","Настройки")
    markup_menu_rus.add("свяжитесь с нами")
    
    # markup tasdiqlash
    markup_tasdiq=types.ReplyKeyboardMarkup(resize_keyboard=(True),one_time_keyboard=(True))
    markup_tasdiq.add("Tasdiqlash")
    
    
    # markup tasdiqlash rus
    markup_tasdiq_rus=types.ReplyKeyboardMarkup(resize_keyboard=(True),one_time_keyboard=(True))
    markup_tasdiq_rus.add("Подтверждение")
    
    # kitob malumotlari ni ozgartirish markup
    markup_about_book=types.ReplyKeyboardMarkup()
    about_book_list=["Kitob nomi","Kitob muallifi","Ijara muddati","Ijara narxi","Kitob rasmi","Saqlash "]
    for i in about_book_list:
        markup_about_book.add(i)
    
    markup_about_book_rus=types.ReplyKeyboardMarkup()
    about_book_list_rus=["Название книги","Автор книги","Срок аренды","Стоимость аренды","книжная картина"," спасти"]
    for i in about_book_list_rus:
        markup_about_book_rus.add(i)
        
    # id_oz_och=None
    import time
    @bot.message_handler(commands=['start'])
    def starting(message):
        time.sleep(1)
        cur.execute(f"select id,language,district,n2 from users where user_id={message.from_user.id}")
        res=cur.fetchall()
        # print(res[3])
        # print(len(res))
        if len(res)==0:
    
            bot.send_message(message.from_user.id,"Assalom alekum\nTil tanlang",reply_markup=markup_uzb_ru)
            time.sleep(1)
        else:
            for r in res:
                if r[1]=="Uzbek":
                    bot.send_message(message.from_user.id,"Assalom alekum\nKerakli bo'limni tanlang",reply_markup=markup_menu)
                else:
                    bot.send_message(message.from_user.id,"Привет\nВыберите нужный раздел",reply_markup=markup_menu_rus)
            time.sleep(1)  
    @bot.callback_query_handler(func=lambda call:True)
    def uzbru(call):
    
        try:
            time.sleep(1)
            sql="select language from users where user_id=%s"
            val=(call.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            if lang=="Uzbek":
    
                if call.message.text=="Sizning kitoblaringiz":
                    print(call)
                    cur.execute(f"select book_name,rent_time,rent_cost,photo_id,id,author from books where user_id={call.from_user.id}")
                    res=cur.fetchall()
                    # time.sleep(1)
                    # global id_oz_och
                        
                    for j in res:
        
        
                        if call.data==str(j[0]):
                            markup_orqa=types.ReplyKeyboardMarkup(one_time_keyboard=(True),resize_keyboard=True)
                            markup_orqa.add("Malumotlarni o'zgartirish")
                            markup_orqa.add("Kitobni o'chirish")
                            markup_orqa.add("Orqaga","Bosh menu")
                            bot.send_photo(call.from_user.id,j[3],caption=f"📕 Kitob nomi: {j[0]}\n✍️ Kitob muallifi : {j[-1]}\n⏳ Ijara muddati : {j[1]}\n💵 Ijara narxi : {j[2]} ",reply_markup=markup_orqa)
                                    # id olish kk
                            # id_oz_och=j[4]
                            sql="update books set about_book=%s where book_name=%s"
                            val=(j[4],j[0])
                            cur.execute(sql,val)
                            db.commit()
                            # markup_orqa=types.ReplyKeyboardMarkup(one_time_keyboard=(True),resize_keyboard=True)
                            # markup_orqa.add("Malumotlarni o'zgartirish")
                            # markup_orqa.add("Kitobni o'chirish")
                            # markup_orqa.add("Orqaga","Bosh menu")
                            #             # but_orqa=types.InlineKeyboardButton("Orqaga",callback_data="Orqaga")
                            # bot.send_message(call.from_user.id,f"Kitob nomi: {j[0]}\nKitob muallifi : {j[-1]}\nIjara muddati : {j[1]}\nIjara narxi : {j[2]} ",reply_markup=markup_orqa)
                            time.sleep(1)
                            
        
                elif call.message.text=="Kitoblar":
                    time.sleep(1)
                    
                    cur.execute("select book_name,author,rent_time,rent_cost,user_id,photo_id,id from books")
                    result=cur.fetchall()
                    print("i")
                    for res in result:
                        if call.data==str(res[-1]):
                            print("m")
                            time.sleep(1)
                            userid=res[4]
                        
                            cur.execute(f"select name,phone,n5,region,district from users where user_id={userid}")
                            natija=cur.fetchall()
                            for i in natija:
                                text=f"🧑 Kitob egasi 🧔: {i[0]}\n☎️ Telefon nomeri : {i[1]}\n📍 Turar joyi: {i[-2]} {i[-1]}"
                                username=i[2]
                            bot.send_photo(call.from_user.id,res[-2],caption=text+f"\n📕 Kitob nomi : {res[0]}\n✍️ Muallif : {res[1]}\n⏳ Ijara vaqti :  {res[2]}\n💵 Ijara narxi : {res[3]}\nTelegram : @{username}")
                            # bot.send_message(call.from_user.id,text+f"\nKitob nomi : {res[0]}\nMuallif : {res[1]}\nIjara vaqti :  {res[2]}\nIjara narxi : {res[3]}")
                            time.sleep(1)
        
                elif call.data=="Andijon viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Andijon)
                    # like
        
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Jizzax viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Jizzax )
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Navoiy viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Navoiy )
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Samarqand viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Samarqand )
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Sirdaryo viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Sir)
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Toshkent viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_T_vil)
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Xorazm viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Xorazm)
                    cur.execute(sql,val)
                    db.commit()
                elif call.data=="Buxoro viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Buxoro)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Qashqadaryo viloyati":
                    print("qashqadaryo")
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Qash)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Namangan viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Nam)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Surxondaryo viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Sur)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Toshkent shahar":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Tshah)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Farg'ona viloyati":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Far)
                    cur.execute(sql,val)
                    db.commit()        
                elif call.data=="Qoraqalpog'iston Resp.":
                    sql="update users set region=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.send_message(call.from_user.id,"Tuman(shahar) tanlang",reply_markup=markup_dist_Qoraqalp)
                    cur.execute(sql,val)
                    db.commit()    
                elif (call.data in districts_Andijon or districts_Buxoro or districts_Navoiy or districts_Sirdaryo or districts_Xorazm or districts_Qashqadaryo or districts_Surxondaryo or districts_Fargona or districts_Jizzax or districts_Toshkent_shah or districts_Toshkent_vil or districts_Qoraqalpoq or districts_Namangan) and call.data!="Ortga" :
                    time.sleep(1)
                    sql="update users set district=%s where user_id=%s"
                    val=(call.data,call.from_user.id)
                    bot.delete_message(call.from_user.id,call.message.message_id-1)
                    # bot.delete_message(call.from_user.id,call.message.message_id-2)
    
                    cur.execute(sql,val)
                    db.commit()
                        
                        
                    bot.send_message(call.from_user.id,"Muvoffaqqiyatli ro'yxatdan o'tdingiz",reply_markup=markup_menu)
                    bot.delete_message(call.from_user.id,call.message.message_id)
                    bot.delete_message(call.from_user.id,call.message.message_id-1)
    
                
                elif call.data=="Ortga":
                    bot.send_message(call.from_user.id,"Viloyatingizni tanlang",reply_markup=markup_region)
                        
                    bot.delete_message(call.from_user.id,call.message.message_id-1)
            elif lang=="Rus":
                try:
                    text="Выберите район (город)"
                    if call.message.text=="Твои книги":
                        print(call)
                        cur.execute(f"select book_name,rent_time,rent_cost,photo_id,id,author from books where user_id={call.from_user.id}")
                        res=cur.fetchall()
                        # global id_oz_och
                            
                        for j in res:
            
            
                            if call.data==j[0]:
                                bot.send_photo(call.from_user.id,j[3],caption=f"Название книги: {j[0]}\nАвтор книги : {j[-1]}\nСтоимость аренды : {j[1]}\nСрок аренды : {j[2]} ",reply_markup=markup_orqa_rus)
                                        # id olish kk
                                sql="update books set about_book=%s where book_name=%s"
                                val=(j[4],j[0])
                                cur.execute(sql,val)
                                db.commit()
                                # bot.send_message(call.from_user.id,f"Название книги: {j[0]}\nАвтор книги : {j[-1]}\nСтоимость аренды : {j[1]}\nСрок аренды : {j[2]} ",reply_markup=markup_orqa_rus)
            
                    
                    elif call.data=="Andijon viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Andijon)
                        cur.execute(sql,val)
                        db.commit()              
                            
                    elif call.data=="Jizzax viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Jizzax )
                        cur.execute(sql,val)
                        db.commit()              
                    elif call.data=="Navoiy viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Navoiy )
                        cur.execute(sql,val)
                        db.commit()      
                    elif call.data=="Samarqand viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Samarqand )
                        cur.execute(sql,val)
                        db.commit()    
                    elif call.data=="Sirdaryo viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Sir)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Toshkent viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_T_vil)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Xorazm viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Xorazm)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Buxoro viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Buxoro)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Qashqadaryo viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Qash)
                        cur.execute(sql,val)
                        db.commit()    
                    elif call.data=="Namangan viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Nam)
                        cur.execute(sql,val)
                        db.commit()   
                    elif call.data=="Surxondaryo viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Sur)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Toshkent shahar":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Tshah)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Farg'ona viloyati":
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Far)
                        cur.execute(sql,val)
                        db.commit()  
                    elif call.data=="Qoraqalpog'iston Resp.":
                        
                        sql="update users set region=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dist_Qoraqalp)
                        cur.execute(sql,val)
                        db.commit()  
                        
                    elif (call.data in districts_Andijon or districts_Buxoro or districts_Navoiy or districts_Sirdaryo or districts_Xorazm or districts_Qashqadaryo or districts_Surxondaryo or districts_Fargona or districts_Jizzax or districts_Toshkent_shah or districts_Toshkent_vil or districts_Qoraqalpoq or districts_Namangan) and call.data!="Ortga" :
                        sql="update users set district=%s where user_id=%s"
                        val=(call.data,call.from_user.id)
                        cur.execute(sql,val)
                        db.commit()  
                        bot.send_message(call.from_user.id,"Вы успешно зарегистрировались",reply_markup=markup_menu_rus)
                    # bot.delete_message(call.from_user.id,call.message.message_id-1)
                    bot.delete_message(call.from_user.id,call.message.message_id)
                    time.sleep(1)
    
                    # bot.delete_message(call.from_user.id,call.message.message_id-1) 
                except Exception as a:
                    print(a)
    
    
        except :
                    if call.data=="Uzbek":
                        print("a")
            
                        sql="insert into users (language,user_id,n5) values (%s,%s,%s)"
                        val=("Uzbek",call.from_user.id,call.from_user.username)
                        cur.execute(sql,val)
                        db.commit()
                        time.sleep(1)
                        print("b")
                        bot.send_message(call.from_user.id,"Ism Familiyangizni kiriting\nMasalan : Ali Valiyev")
                        # bot.delete_message(call.from_user.id,call.message.message_id-1)
                        bot.delete_message(call.from_user.id,call.message.message_id)
    
                    elif call.data=="Rus":
                        sql="insert into users (language,user_id,n5) values (%s,%s,%s)"
                        val=("Rus",call.from_user.id,call.from_user.username)
                        cur.execute(sql,val)
                        db.commit()
                        time.sleep(1)
            
                        bot.send_message(call.from_user.id,"Введите ваше имя\nнапример Али Валиев")
                        bot.delete_message(call.from_user.id,call.message.message_id-1)
                        bot.delete_message(call.from_user.id,call.message.message_id)
    
                        # bot.delete_message(call.from_user.id,call.message.message_id-2)
    
    
    @bot.message_handler(content_types=['text'])
    def name_sur(message):
        try:
            time.sleep(1)
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            if lang=="Uzbek":
                if message.text=="🔎 Kitob qidirish":
                    msg=bot.send_message(message.from_user.id,"Kitob nomini kiriting:")
                    bot.register_next_step_handler(msg,search_book)
                
                elif message.text=="➕ Kitob qo'shish":
                    bot.send_message(message.from_user.id,"Kitob rasmini yuboring")  
                
                elif message.text=="Malumotlarni o'zgartirish":
                    # global id_oz_och
                    time.sleep(1)
                    cur.execute("select book_name,rent_time,rent_cost,photo_id,author from books where id=about_book")
                    # val=(id_oz_och,)
                    # cur.execute(sql,val)
                    result=cur.fetchall()
                    for j in result:                                    #📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}
                        bot.send_photo(message.from_user.id,j[3],caption=f"Qaysi malumotlarni o'zgartirmoqchisiz\n📕 Kitob nomi: {j[0]}\n✍️ Kitob muallifi : {j[-1]}\n⏳ Ijara muddati : {j[1]}\n💵 Ijara narxi : {j[2]}",reply_markup=markup_about_book)
                        # bot.send_message(message.from_user.id,f"Qaysi malumotlarni o'zgartirmoqchisiz\nKitob nomi: {j[0]}\nKitob muallifi : {j[-1]}\nIjara muddati : {j[1]}\nIjara narxi : {j[2]}",reply_markup=markup_about_book)
                    
                elif message.text=="Kitob nomi":
                    msg=bot.send_message(message.from_user.id,"Kitob nomini kiriting")
                    bot.register_next_step_handler(msg,new_book_name)
                elif message.text=="Kitob muallifi":
                    msg=bot.send_message(message.from_user.id,"Kitob muallifini kiriting")
                    bot.register_next_step_handler(msg,new_book_author)                    
        
                elif message.text=="Ijara muddati":
                    msg=bot.send_message(message.from_user.id,"Kitob ijara muddatini kiriting")
                    bot.register_next_step_handler(msg,new_book_time)
                elif message.text=="Ijara narxi":
                    msg=bot.send_message(message.from_user.id,"Kitob ijara narxini kiriting")
                    bot.register_next_step_handler(msg,new_book_cost)
                elif message.text=="Kitob rasmi":
                    msg=bot.send_message(message.from_user.id,"Kitob rasmini yuboring")
                    bot.register_next_step_handler(msg,new_book_photo)
                   
                elif message.text=="Saqlash ":
                    # cur.execute(f"update users set book_name={user.book_name},rent_cost={user.rent_cost},rent_time={user.rent_time},photo_id={user.photo_id} where id={user.n1}")
                        # db.commit()
                    sql="update books set about_book=%s where id=about_book and user_id=%s"
                    val=(None,message.from_user.id)
                    cur.execute(sql,val)
                    db.commit()
                        
                    bot.send_message(message.from_user.id,"Malumotlar saqlandi",reply_markup=markup_menu)
                    bot.delete_message(message.from_user.id,message.message_id-1)
                    bot.delete_message(message.from_user.id,message.message_id-2)
                               
                    
                elif message.text=="✔️ Saqlash":
                    bot.send_message(message.from_user.id,"Malumotlar saqlandi",reply_markup=markup_menu)
                    bot.delete_message(message.from_user.id,message.message_id-1)
                    bot.delete_message(message.from_user.id,message.message_id-2)
    
    
    
    
                elif message.text=="📚 Mening kutubxonam" or message.text=="Orqaga" :
                    time.sleep(1)
                    sql="update books set about_book=%s where id=about_book and user_id=%s"
                    val=(None,message.from_user.id)
                    cur.execute(sql,val)
                    db.commit()
                        
                    markup_my_books=types.InlineKeyboardMarkup()
                    cur.execute(f"select book_name from books where user_id={message.from_user.id}")
                        
                    books=cur.fetchall()
                    for i in books:
                        but_book=types.InlineKeyboardButton(str(i[0]),callback_data=str(i[0]))
                        markup_my_books.add(but_book)
                            
                    bot.send_message(message.from_user.id,"Sizning kitoblaringiz",reply_markup=markup_my_books)
                
                
                elif message.text=="⚙️ Sozlamalar":
                    time.sleep(1)
                    sql="select name , surname, phone,language from users where user_id=%s"
                    val=(message.from_user.id,)
                    cur.execute(sql,val)
                    result=cur.fetchall()
                    for res in result:
                        msg=bot.send_message(message.from_user.id,f"Qaysi malumotni o'zgartirmoqchisiz\nIsmingiz : {res[0]}\nFamiliyangiz : {res[1]}\nTelefon nomer : {res[2]}\nTil : {res[3]}",reply_markup=markup_about_me)
                        quit()                    
                elif message.text=="Kitobni o'chirish":
                    time.sleep(1)
                    # global id_oz_och
                    # print(id_oz_och)
                    cur.execute(f"delete from books where id=about_book")
                    db.commit()
                        
                    bot.send_message(message.from_user.id,"Kitob o'chirildi",reply_markup=markup_menu)
    
                    bot.delete_message(message.from_user.id,message.message_id-1)
                    bot.delete_message(message.from_user.id,message.message_id-2)
                
                elif message.text=="📱 Biz bilan bog'lanish":
            
                    bot.send_message(message.from_user.id,"Bu yerda malumotlar bo'ladi")   
                
                elif message.text=="🖌 Ism":
                    msg=bot.send_message(message.from_user.id,"Ismingizni kiriting")    
                    bot.register_next_step_handler(msg,new_name)
                    bot.delete_message(message.from_user.id, message.message_id-1)
                    
                elif message.text=="Bosh menu":
                    sql="update books set about_book=%s where id=about_book and user_id=%s"
                    val=(None,message.from_user.id)
                    cur.execute(sql,val)
                    db.commit()
                        
                    bot.send_message(message.from_user.id,"Bosh menu",reply_markup=markup_menu)
                        
                elif message.text=="🖍 Familiya":
                    msg=bot.send_message(message.from_user.id,"Familiyangizni kiriting")    
                    bot.register_next_step_handler(msg,new_surname)
                    bot.delete_message(message.from_user.id, message.message_id-1)
                elif message.text=="☎️ Telefon nomer":
                    msg=bot.send_message(message.from_user.id,"Telefon nomeringizni kiriting",reply_markup=markup_contact)    
                    bot.register_next_step_handler(msg,new_phone)
                    bot.delete_message(message.from_user.id, message.message_id-1)
                elif message.text=="🇸🇱 Tilni o'zgartirish 🇷🇺":
                    msg=bot.send_message(message.from_user.id,"Til tanlang",reply_markup=markup_new_lang)    
                    bot.register_next_step_handler(msg,new_lang)
                    bot.delete_message(message.from_user.id, message.message_id-1)
                elif message.text=="Saqlash" :
                    sql="update books set about_book=%s where id=about_book and user_id=%s"
                    val=(None,message.from_user.id)
                    cur.execute(sql,val)
                    db.commit()
                    bot.send_message(message.from_user.id,"Malumotlar saqlandi",reply_markup=markup_menu)
                    bot.delete_message(message.from_user.id, message.message_id-1)
                    bot.delete_message(message.from_user.id,message.message_id-3)
                    bot.delete_message(message.from_user.id,message.message_id-2)
                else:
                    bot.delete_message(message.from_user.id,message.message_id)
                    try:
                        time.sleep(1)
        
                        sql="update users set name=%s,surname=%s where user_id=%s"
                        name,surname=message.text.split()
                        print(name,surname)
                        val=(name,surname,message.from_user.id)
                        cur.execute(sql,val)
                        db.commit()
                    except:
                        time.sleep(1)
        
                        sql="update users set name=%s where user_id=%s"
                        val=(message.text,message.from_user.id)
                        cur.execute(sql,val)
                        db.commit()
                    msg=bot.send_message(message.from_user.id,"Raqamingizni yuboring\nPastdagi tugma orqali yoki +998 XX xxx xx xx",reply_markup=markup_contact)
                    bot.register_next_step_handler(msg,phone)
                    bot.delete_message(message.from_user.id,message.message_id-1)                
                
            else:
                try:
                    if message.text=="Добавить книгу":
                        bot.send_message(message.from_user.id,"Отправить фотографию книги")           
                        
                    elif message.text=="Книжный поиск":
                        pass
                    elif message.text=="Моя библиотека" or message.text=="Назад":
                        time.sleep(1)
                        markup_my_books=types.InlineKeyboardMarkup()
                        cur.execute(f"select book_name from books where user_id={message.from_user.id}")
                            
                        books=cur.fetchall()
                        for i in books:
                            but_book=types.InlineKeyboardButton(str(i[0]),callback_data=str(i[0]))
                            markup_my_books.add(but_book)
                                
                        bot.send_message(message.from_user.id,"Твои книги",reply_markup=markup_my_books)
                
                    elif message.text=="Изменить данные":
                        # global id_oz_och
                        cur.execute("select book_name,rent_time,rent_cost,photo_id,author from books where id=about_book")
                        # val=(id_oz_och,)
                        # cur.execute(sql,val)
                        result=cur.fetchall()
                        for j in result:
                            bot.send_photo(message.from_user.id,j[3],caption=f"Какие данные вы хотите изменить\nНазвание книги: {j[0]}\nАвтор книги : {j[-1]}\nСрок аренды : {j[1]}\nСтоимость аренды : {j[2]}",reply_markup=markup_about_book_rus)
                            # bot.send_message(message.from_user.id,f"Какие данные вы хотите изменить\nНазвание книги: {j[0]}\nАвтор книги : {j[-1]}\nСрок аренды : {j[1]}\nСтоимость аренды : {j[2]}",reply_markup=markup_about_book_rus)
                    elif message.text=="Название книги":
                        msg=bot.send_message(message.from_user.id,"Введите название книги")
                        bot.register_next_step_handler(msg,new_book_name)
                    elif message.text=="Автор книги":
                        msg=bot.send_message(message.from_user.id,"Введите автора книги")
                        bot.register_next_step_handler(msg,new_book_author)                    
            
                    elif message.text=="Удалить книгу":
                        # global id_oz_och
                        # print(id_oz_och)
                        cur.execute(f"delete from books where id=about_book")
                        db.commit()
                            
                        bot.send_message(message.from_user.id,"Книга удалена",reply_markup=markup_menu_rus)
        
                        bot.delete_message(message.from_user.id,message.message_id-1)
                        bot.delete_message(message.from_user.id,message.message_id-2)
            
                    elif message.text=="Срок аренды":
                        msg=bot.send_message(message.from_user.id,"Введите срок проката книги")
                        bot.register_next_step_handler(msg,new_book_time)
                    elif message.text=="Стоимость аренды":
                        msg=bot.send_message(message.from_user.id,"Введите стоимость аренды книги")
                        bot.register_next_step_handler(msg,new_book_cost)
                    elif message.text=="книжная картина":
                        msg=bot.send_message(message.from_user.id,"Oтправить фотографию книги")
                        bot.register_next_step_handler(msg,new_book_photo)
                        
                    elif message.text=="спасти":
                        # cur.execute(f"update users set book_name={user.book_name},rent_cost={user.rent_cost},rent_time={user.rent_time},photo_id={user.photo_id} where id={user.n1}")
                            # db.commit()
                            
                        bot.send_message(message.from_user.id,"Данные сохранены",reply_markup=markup_menu_rus)
                        bot.delete_message(message.from_user.id,message.message_id-1)
                        bot.delete_message(message.from_user.id,message.message_id-2)
                
                    elif message.text=="Настройки":
              
                        sql="select name , surname, phone,language from users where user_id=%s"
                        val=(message.from_user.id,)
                        cur.execute(sql,val)
                        result=cur.fetchall()
                        for res in result:
                            msg=bot.send_message(message.from_user.id,f"Какую карту вы хотите поменять\nимя : {res[0]}\nФамилия : {res[1]}\nТелефонный номер : {res[2]}\nязык : {res[3]}",reply_markup=markup_about_me_rus)
                            quit()                      
                    elif message.text=="свяжитесь с нами":
                
                        bot.send_message(message.from_user.id,"Bu yerda malumotlar bo'ladi")   
                    elif message.text=="Имя":
                        msg=bot.send_message(message.from_user.id,"Введите ваше имя")    
                        bot.register_next_step_handler(msg,new_name)
                        
                    elif message.text=="Фамилия":
                        msg=bot.send_message(message.from_user.id,"Введите вашу фамилию")    
                        bot.register_next_step_handler(msg,new_surname)
                        
                    elif message.text=="Телефонный номер":
                        msg=bot.send_message(message.from_user.id,"Введите свой номер телефона",reply_markup=markup_contact_rus)    
                        bot.register_next_step_handler(msg,new_phone)
                        
                    elif message.text=="Изменить язык":
                        msg=bot.send_message(message.from_user.id,"Выберите язык",reply_markup=markup_new_lang)    
                        bot.register_next_step_handler(msg,new_lang)
                        
                    elif message.text=="Сохранить" :
    
                      
                        # cur.execute(f"update users set name={user.name},surname={user.surname},phone={user.phone},language={user.language}")
                        # db.commit()
                        # cur.close()
                        # db.close()
                        bot.send_message(message.from_user.id,"Ссылка сохранена",reply_markup=markup_menu_rus)
                        bot.delete_message(message.from_user.id,message.message_id-1)
                        bot.delete_message(message.from_user.id,message.message_id-2)
    
                    else:
    
                        bot.delete_message(message.from_user.id,message.message_id)
                        try:
    
                            sql="update users set name=%s,surname=%s where user_id=%s"
                            name,surname=message.text.split()
                            val=(name,surname,message.from_user.id)
                            cur.execute(sql,val)
                            db.commit()
                        except:
    
                            sql="update users set name=%s where user_id=%s"
                            val=(message.text,message.from_user.id)
                            cur.execute(sql,val)
                            db.commit()
                        msg=bot.send_message(message.from_user.id,"Отправь свой номер\nС помощью кнопки ниже или +998 XX xxx xx xx",reply_markup=markup_contact_rus)
                        bot.register_next_step_handler(msg,phone)
                        bot.delete_message(message.from_user.id,message.message_id-1)
                except Exception as a:
                    print(a)
                
                
        except Exception as a:
            print(a)    
    
    def phone(message):
        try:
            time.sleep(1)
    
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            if lang=="Uzbek":
                try:
                    x=0
                    cur.execute("select phone from users")
                    result=cur.fetchall()
                    print("a")
                    for res in result:
                        try:
                            if res[0][::-1][:7]==message.contact.phone_number[::-1][:7]:
                                x+=1
                        except:
                            pass
                    print("b")
                    if x>0:
                        msg=bot.send_message(message.from_user.id,"Bu nomer avval ro'yxattan o'tgan\nBoshqa nomer yuboring")
                        bot.register_next_step_handler(msg,phone)
                    else:
                        sql="update users set phone=%s where user_id=%s"
                        val=(message.contact.phone_number,message.from_user.id)
                        cur.execute(sql,val)
                        db.commit()
                        
        
                        bot.send_message(message.from_user.id,"Viloyatingizni tanlang",reply_markup=markup_region)
                        time.sleep(1)
                    
                except:
                    x=0
                    cur.execute("select phone from users")
                    result=cur.fetchall()
                    print("c")
                    for res in result:
                        print(res[0])
                        try:
                            if res[0][::-1][:7]==message.text[::-1][:7]:
                                x+=1
                        except:
                            pass
                    print("d")
                    if x>0:
                        msg=bot.send_message(message.from_user.id,"Bu nomer avval ro'yxattan o'tgan\nBoshqa nomer yuboring")
                        bot.register_next_step_handler(msg,phone)
                    else:
                        sql="update users set phone=%s where user_id=%s"
                        val=(message.text,message.from_user.id)
                        cur.execute(sql,val)
                        db.commit()
                        time.sleep(1)
        
                        bot.send_message(message.from_user.id,"Viloyatingizni tanlang",reply_markup=markup_region)
            
                bot.delete_message(message.from_user.id,message.message_id-1)
                bot.delete_message(message.from_user.id,message.message_id)
            else:  
                try:
                    x=0
                    cur.execute("select phone from users")
                    result=cur.fetchall()
                    for res in result:
                        if res[0][::-1][:7]==message.contact.phone_number[::-1][:7]:
                            x+=1
                    if x>0:
                        msg=bot.send_message(message.from_user.id,"Bu nomer avval ro'yxattan o'tgan\nBoshqa nomer yuboring")
                        bot.register_next_step_handler(msg,phone)
                    else:
                        sql="update users set phone=%s where user_id=%s"
                        val=(message.contact.phone_number,message.from_user.id)                
                        cur.execute(sql,val)
                        db.commit()
                        time.sleep(1)
                        bot.send_message(message.from_user.id,"выберите свой регион",reply_markup=markup_region)
                    
                except:
                    x=0
                    cur.execute("select phone from users")
                    result=cur.fetchall()
                    for res in result:
                        if res[0][::-1][:7]==message.text[::-1][:7]:
                            x+=1
                    if x>0:
                        msg=bot.send_message(message.from_user.id,"Bu nomer avval ro'yxattan o'tgan\nBoshqa nomer yuboring")
                        bot.register_next_step_handler(msg,phone)
                    else:
                        sql="update users set phone=%s where user_id=%s"
                        val=(message.text,message.from_user.id)
                        cur.execute(sql,val)
                        db.commit()
                        time.sleep(1)
                        bot.send_message(message.from_user.id,"выберите свой регион",reply_markup=markup_region)
                
                bot.delete_message(message.from_user.id,message.message_id-1)
                bot.delete_message(message.from_user.id,message.message_id)
    
        except Exception as a:
            print(a)
    
    
    # photo_id=None
    
    import time
    @bot.message_handler(content_types=['photo'])
    def get_photo(message):
        try:
            print("aa")
            sql="insert into books (photo_id,user_id) values (%s,%s)"
            print("bb")
            val=(message.photo[-1].file_id,message.from_user.id)
            print("cc")
            cur.execute(sql,val)
            print("dd")
            db.commit()
            time.sleep(1)
            print("a")
            
            user_data[message.from_user.id]=User(message.photo[-1].file_id)
    
            sql="select language from users where user_id=%s"
            print("b")
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            print("c")
            if lang=="Uzbek":
                msg=bot.send_message(message.from_user.id,"Kitob nomini kiriting")
            else:
                msg=bot.send_message(message.from_user.id,"Введите название книги")
            bot.register_next_step_handler(msg,book_name)
            
        except Exception as a:
            print(a)
    
    def book_name(message):
        try:
            user=user_data[message.from_user.id]
            sql="update books set book_name=%s where photo_id=%s"
            print("d")
            val=(message.text,user.photo_id)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            print("e")
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            print("f")
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            print("g")
            if lang=="Uzbek":
    
                
                msg=bot.send_message(message.from_user.id,"Kitob muallifini kiriting")
                bot.register_next_step_handler(msg,author)        
                bot.delete_message(message.from_user.id,message.message_id-1)
                
            else:
    
    
                msg=bot.send_message(message.from_user.id,"Введите автора книги")
                bot.register_next_step_handler(msg,author)        
                bot.delete_message(message.from_user.id,message.message_id-1)
                
        except Exception as a:
            print(a)
    
    
    def author(message):
        try:
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            user=user_data[message.from_user.id]
            sql="update books set author=%s where photo_id=%s"
            val=(message.text,user.photo_id)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
    
            if lang=="Uzbek":
                
    
                msg=bot.send_message(message.from_user.id,"Kitob ijara muddatini kiriting")
                bot.register_next_step_handler(msg,rent_time)        
                bot.delete_message(message.from_user.id,message.message_id-1)
                
            else:
    
                msg=bot.send_message(message.from_user.id,"Введите срок проката книги")
                bot.register_next_step_handler(msg,rent_time)        
                bot.delete_message(message.from_user.id,message.message_id-1)
        except Exception as a:
            print(a)
    
    
    def rent_time(message):
        try:
            user=user_data[message.from_user.id]
            sql="update books set rent_time=%s where photo_id=%s"
            val=(message.text,user.photo_id)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
    
            if lang=="Uzbek":   
    
                msg=bot.send_message(message.from_user.id,"Kitob ijara narxini kiriting(Masalan : Bepul/10000)")
                bot.register_next_step_handler(msg,rent_cost)        
                bot.delete_message(message.from_user.id,message.message_id-1)
                
            else:
    
                msg=bot.send_message(message.from_user.id,"Введите стоимость аренды книги(Ьесплатно/10000)")
                bot.register_next_step_handler(msg,rent_cost)        
                bot.delete_message(message.from_user.id,message.message_id-1)            
        except Exception as a:
            print(a)
    
    def rent_cost(message):
        try:
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            user=user_data[message.from_user.id]
            sql="update books set rent_cost=%s where photo_id=%s"
            val=(message.text,user.photo_id)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            sql="select book_name,author,rent_time,rent_cost,photo_id from books where photo_id=%s"
            val=(user.photo_id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            # time.sleep(1)
            print("j")
            if lang=="Uzbek":
                print("k")
                for re in result:
                    print("l")
                    msg=bot.send_photo(message.from_user.id,re[-1],caption=f"Malumotlarni tasdiqlang\n📕 Kitob nomi : {re[0]}\n✍️ Kitob muallifi : {re[1]}\n💵 Ijara narxi : {re[3]}\n⏳ Ijara muddati : {re[2]}",reply_markup=markup_tasdiq)
                    print("m")
                    # msg=bot.send_message(message.from_user.id,f"Malumotlarni tasdiqlang\nKitob nomi : {re[0]}\nKitob muallifi : {re[1]}\nIjara narxi : {re[3]}\nIjara muddati : {re[2]}",reply_markup=markup_tasdiq)
                    bot.register_next_step_handler(msg,tasdiq)        
                    bot.delete_message(message.from_user.id,message.message_id-1)
                
            else:
                for re in result:
                    msg=bot.send_photo(message.from_user.id,re[-1],caption=f"Подтвердите детали\nНазвание книги : {re[0]}\nАвтор книги : {re[1]}\nСтоимость аренды : {re[3]}\nСрок аренды : {re[2]}",reply_markup=markup_tasdiq_rus)
                    # msg=bot.send_message(message.from_user.id,f"Подтвердите детали\nНазвание книги : {re[0]}\nАвтор книги : {re[1]}\nСтоимость аренды : {re[3]}\nСрок аренды : {re[2]}",reply_markup=markup_tasdiq_rus)
                bot.register_next_step_handler(msg,tasdiq)        
                bot.delete_message(message.from_user.id,message.message_id-1)
                            
        except Exception as a:
            print(a)
    
    
    def tasdiq(message):
        try:
            sql="select language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
    
            
            # cur.execute("insert into users (user_id,name,surname,language,region,phone,district,book_name,rent_time,rent_cost,photo_id,author) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user.user_id , user.name,user.surname,user.language,user.region,user.phone,user.district ,user.book_name,user.rent_time,user.rent_cost,user.photo_id,user.author))
            
            # db.commit()
            # cur.close()
            # db.close()
            if lang=="Uzbek":
            
                bot.send_message(message.from_user.id,"Kitob muvaffaqqiyatli qo'shildi",reply_markup=markup_menu)
            else:
                bot.send_message(message.from_user.id,"Книга успешно добавлена",reply_markup=markup_menu_rus)
                
            
        except Exception as a:
            print(a)
    
    
    
    def new_book_name(message):
        try:
            # global id_oz_och
            sql="update books set book_name=%s where id=about_book"
            val=(message.text,)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            sql="select language,id,book_name,author,rent_cost,rent_time,photo_id from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            cur.execute("select book_name,rent_time,rent_cost,photo_id,id,author from books where id=about_book")
            # val=(id_oz_och,)
            # cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            if lang=="Uzbek":
                for res in result:
                    text=f"Qaysi malumotni o'zgartirmoqchisiz\n📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book)
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book)
            else:
                for res in result:
                    text=f"Какие данные вы хотите изменить\nНазвание книги: {res[0]}\nАвтор книги : {res[-1]}\nСрок аренды : {res[1]}\nСтоимость аренды : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book_rus)
                
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book_rus)
        except Exception as a:
            print(a)
    
        
    
    def new_book_author(message):
        try:
            # global id_oz_och
            sql="update books set author=%s where id=about_book"
            val=(message.text,)
            cur.execute(sql,val)
            db.commit()
            sql="select language,id,book_name,author,rent_cost,rent_time,photo_id from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            cur.execute("select book_name,rent_time,rent_cost,photo_id,id,author from books where id=about_book")
            # val=(id_oz_och,)
            # cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            
            if lang=="Uzbek":
                for res in result:
                    text=f"Qaysi malumotni o'zgartirmoqchisiz\n📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book)
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book)
            else:
                for res in result:
                    text=f"Какие данные вы хотите изменить\nНазвание книги: {res[0]}\nАвтор книги : {res[-1]}\nСрок аренды : {res[1]}\nСтоимость аренды : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book_rus)
                
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book_rus)
        except Exception as a:
            print(a)
    
    
        
    
    def new_book_cost(message):
        try:
            # global id_oz_och
            sql="update books set rent_cost=%s where id=about_book"
            val=(message.text,)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            sql="select language,id,book_name,author,rent_cost,rent_time,photo_id from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            cur.execute("select book_name,rent_time,rent_cost,photo_id,id,author from books where id=about_book")
            # val=(id_oz_och,)
            # cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            if lang=="Uzbek":
                for res in result:
                    text=f"Qaysi malumotni o'zgartirmoqchisiz\n📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book)
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book)
            else:
                for res in result:
                    text=f"Какие данные вы хотите изменить\nНазвание книги: {res[0]}\nАвтор книги : {res[-1]}\nСрок аренды : {res[1]}\nСтоимость аренды : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book_rus)
                
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book_rus)
        except Exception as a:
            print(a)
    
    
    
        
    
    def new_book_time(message):
        try:
            sql="update books set rent_time=%s where id=about_book"
            val=(message.text,)
            cur.execute(sql,val)
            db.commit()
            time.sleep(1)
            sql="select language,id,book_name,author,rent_cost,rent_time,photo_id from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            for r in res:
                lang=r[0]
            cur.execute("select book_name,rent_time,rent_cost,photo_id,id,author from books where id=about_book")
            # val=(id_oz_och,)
            # cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            
            if lang=="Uzbek":
                for res in result:
                    text=f"Qaysi malumotni o'zgartirmoqchisiz\n📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book)
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book)
            else:
                for res in result:
                    text=f"Какие данные вы хотите изменить\nНазвание книги: {res[0]}\nАвтор книги : {res[-1]}\nСрок аренды : {res[1]}\nСтоимость аренды : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book_rus)   
        
        
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book_rus)
        except Exception as a:
            print(a)
    def new_book_photo (message):
        try:
    
            # global id_oz_och
            sql="update books set photo_id=%s where id=about_book"
            val=(message.photo[-1].file_id,)
            cur.execute(sql,val)
            db.commit()
            sql="select language,id,book_name,author,rent_cost,rent_time,photo_id from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            res=cur.fetchall()
            time.sleep(1)
            for r in res:
                lang=r[0]
            cur.execute("select book_name,rent_time,rent_cost,photo_id,id,author from books where id=about_book")
            # val=(id_oz_och,)
            # cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            
            if lang=="Uzbek":
                for res in result:
                    text=f"Qaysi malumotni o'zgartirmoqchisiz\n📕 Kitob nomi: {res[0]}\n✍️ Kitob muallifi : {res[-1]}\n⏳ Ijara muddati : {res[1]}\n💵 Ijara narxi : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book)
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book)
            else:
                for res in result:
                    text=f"Какие данные вы хотите изменить\n📕 Название книги: {res[0]}\n✍️ Автор книги : {res[-1]}\n⏳ Срок аренды : {res[1]}\n💵 Стоимость аренды : {res[2]}"

                    bot.send_photo(message.from_user.id,res[3],caption=text,reply_markup=markup_about_book_rus)
                
                    # bot.send_message(message.from_user.id,text,reply_markup=markup_about_book_rus)  ✍️ 📕 💵 ⏳
        except Exception as a:
            print(a)
    
    
    def new_name(message):
        try:
            sql="update users set name=%s where user_id=%s"
            val=(message.text,message.from_user.id)
            cur.execute(sql,val)
            db.commit()
            sql="select language,name,surname,phone,language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            global lang
    
            
            for res in result:
                if res[0]=="Uzbek":
                    bot.send_message(message.from_user.id,f"Yana qaysi malumotni o'zgartirmoqchiz\nIsmingiz : {res[1]}\nFamiliyangiz : {res[2]}\nNomeringiz : {res[3]}\nJoriy til : {res[4]}",reply_markup=markup_about_me)
                # bot.delete_message(message.from_user.id,message.message_id-1)
                
                else:
    
    
                    bot.send_message(message.from_user.id,f"Какие еще данные вы хотите изменить?\nИмя : {res[1]}\nФамилия : {res[2]}\nТелефонный номер : {res[3]}\nязык : {res[4]}",reply_markup=markup_about_me_rus)
            bot.delete_message(message.from_user.id,message.message_id-1)
        except Exception as a:
            print(a)
    
    
    def new_surname(message):
        try:
            sql="update users set surname=%s where user_id=%s"
            val=(message.text,message.from_user.id)
            cur.execute(sql,val)
            db.commit()
            sql="select language,name,surname,phone,language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            global lang
            time.sleep(1)
    
            
            for res in result:
                if res[0]=="Uzbek":
                    bot.send_message(message.from_user.id,f"Yana qaysi malumotni o'zgartirmoqchiz\nIsmingiz : {res[1]}\nFamiliyangiz : {res[2]}\nNomeringiz : {res[3]}\nJoriy til : {res[4]}",reply_markup=markup_about_me)
                # bot.delete_message(message.from_user.id,message.message_id-1)
                
                else:
                    bot.send_message(message.from_user.id,f"Какие еще данные вы хотите изменить?\nИмя : {res[1]}\nФамилия : {res[2]}\nТелефонный номер : {res[3]}\nязык : {res[4]}",reply_markup=markup_about_me_rus)
            bot.delete_message(message.from_user.id,message.message_id-1)
            time.sleep(1)
        except Exception as a:
            print(a)
    
    
    def new_phone(message):
        try:
            sql="update users set phone=%s where user_id=%s"
            val=(message.contact.phone_number,message.from_user.id)
            cur.execute(sql,val)
            db.commit()
            sql="select language,name,surname,phone,language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            global lang
    
            
            for res in result:
                if res[0]=="Uzbek":
                    bot.send_message(message.from_user.id,f"Yana qaysi malumotni o'zgartirmoqchiz\nIsmingiz : {res[1]}\nFamiliyangiz : {res[2]}\nNomeringiz : {res[3]}\nJoriy til : {res[4]}",reply_markup=markup_about_me)
                # bot.delete_message(message.from_user.id,message.message_id-1)
                
                else:
                    bot.send_message(message.from_user.id,f"Какие еще данные вы хотите изменить?\nИмя : {res[1]}\nФамилия : {res[2]}\nТелефонный номер : {res[3]}\nязык : {res[4]}",reply_markup=markup_about_me_rus)
            bot.delete_message(message.from_user.id,message.message_id-1)
        except:
            sql="update users set phone=%s where user_id=%s"
            val=(message.text,message.from_user.id)
            cur.execute(sql,val)
            db.commit()
            sql="select language,name,surname,phone,language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)

    
            
            for res in result:
                if res[0]=="Uzbek":
                    bot.send_message(message.from_user.id,f"Yana qaysi malumotni o'zgartirmoqchiz\nIsmingiz : {res[1]}\nFamiliyangiz : {res[2]}\nNomeringiz : {res[3]}\nJoriy til : {res[4]}",reply_markup=markup_about_me)
                
                else:
                    bot.send_message(message.from_user.id,f"Какие еще данные вы хотите изменить?\nИмя : {res[1]}\nФамилия : {res[2]}\nТелефонный номер : {res[3]}\nязык : {res[4]}",reply_markup=markup_about_me_rus)
            bot.delete_message(message.from_user.id,message.message_id-1)
    def new_lang(message):
        try:
            sql="update users set language=%s where user_id=%s"
            val=(message.text,message.from_user.id)
            cur.execute(sql,val)
            db.commit()
            sql="select language,name,surname,phone,language from users where user_id=%s"
            val=(message.from_user.id,)
            cur.execute(sql,val)
            result=cur.fetchall()
            time.sleep(1)
            global lang     
            for res in result:
                if res[0]=="Uzbek":
                    bot.send_message(message.from_user.id,f"Yana qaysi malumotni o'zgartirmoqchiz\nIsmingiz : {res[1]}\nFamiliyangiz : {res[2]}\nNomeringiz : {res[3]}\nJoriy til : {res[4]}",reply_markup=markup_about_me)
                # bot.delete_message(message.from_user.id,message.message_id-1)
                
                else:
                    bot.send_message(message.from_user.id,f"Какие еще данные вы хотите изменить?\nИмя : {res[1]}\nФамилия : {res[2]}\nТелефонный номер : {res[3]}\nязык : {res[4]}",reply_markup=markup_about_me_rus)
            bot.delete_message(message.from_user.id,message.message_id-1)
        except Exception as a:
            print(a)
    
    
    def search_book(message):
        try:
            book=message.text
            sql="select book_name,author,rent_time,rent_cost,id,photo_id from books where book_name like %s"
            val=('%'+book+'%',)
            cur.execute(sql,val)
            result=cur.fetchall()
            
            markup_books=types.InlineKeyboardMarkup()
            for res in result:
                bbutton=types.InlineKeyboardButton(res[0],callback_data=res[4])
                markup_books.add(bbutton)
                
            bot.send_message(message.from_user.id,"Kitoblar",reply_markup=markup_books)
            time.sleep(1)
            
            
        except Exception as a:
            print(a)
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    bot.polling(none_stop=(True))
    
except Exception as a:
    
    print(a)
