import telebot

from bs4 import BeautifulSoup as BS

import requests

bot=telebot.TeleBot("1978322910:AAG4s-O03zDeD2GCWrIr_rTIyr2lDY0mN2Y")



HEADERS={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
        'accept':'*/*'
        
}


channels=['Sevimli TV','ZO`R TV','Milliy TV','Mening Yurtim','Kinoteatr Telekanali','Yoshlar Telekanali','Bolajon Telekanali']


markup_channels=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
markup_channels.add('Sevimli TV','ZO`R TV')
markup_channels.add('Mening Yurtim','Kinoteatr Telekanali')
# markup_channels.add('Yoshlar Telekanali','Bolajon Telekanali')
markup_channels.add('Milliy TV')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id,"Assalom alekum\nTele ko'rsatuvlar botiga xush kelibsiz\nQiziq bo'lgan kanalingizni tanlang",reply_markup=markup_channels)
    
    
@bot.message_handler(content_types=['text'])
def channels(message):
    if message.text=="Mening Yurtim":
        url='https://www.savol-javob.com/my-5-tv-dasturlari-mening-yurtim-programmasi-bugungi/'
                
        session=requests.Session()
        response=session.get(url,headers=HEADERS)
    
        soup=BS(response.content,'html.parser')
    
        items=soup.find_all('div',class_='sc-cJSrbW dRyaGb')
        a=0
        text=''
        for i in items:
            j=i.find_all('p')
            for l in j:
                a+=1
                text+=l.text
        
                if a==8:
                    break
            if a==8:
                break
        text=text.replace("PAYSHANBA", "\n\nPAYSHANBA\n\n")
        text=text.replace("DUSHANBA", "\n\nDUSHANBA\n\n")
        text=text.replace("SESHANBA", "\n\nSESHANBA\n\n")
        text=text.replace("CHORSHANBA", "\n\nCHORSHANBA\n\n")
        text=text.replace("JUMA", "\n\nJUMA\n\n")
        text=text.replace("YAKSHANBA", "\n\nYAKSHANBA\n\n")
        bot.send_message(message.from_user.id,text)
        
    
    elif message.text=="Sevimli TV":
        url='https://www.savol-javob.com/sevimli-tv-dasturlari-bugungi/'
                
        session=requests.Session()
        response=session.get(url,headers=HEADERS)
    
        soup=BS(response.content,'html.parser')
    
        items=soup.find_all('div',class_='sc-cJSrbW dRyaGb')
        a=0
        text=''
        for i in items:
            j=i.find_all('h6')
            print(len(j))
            for l in j:
                a+=1
                text+=l.text
        
                if a==12:
                    break
            if a==12:
                break
        text=text.replace("PAYSHANBA", "\n\nPAYSHANBA\n\n")
        text=text.replace("DUSHANBA", "\n\nDUSHANBA\n\n")
        text=text.replace("SESHANBA", "\n\nSESHANBA\n\n")
        text=text.replace("CHORSHANBA", "\n\nCHORSHANBA\n\n")
        text=text.replace("JUMA", "\n\nJUMA\n\n")
        text=text.replace("YAKSHANBA", "\n\nYAKSHANBA\n\n")
        bot.send_message(message.from_user.id,text)
        
    elif message.text=="Kinoteatr Telekanali":
        url='https://www.savol-javob.com/kinoteatr-telekanali-programmasi-bugungi/'
                
        session=requests.Session()
        response=session.get(url,headers=HEADERS)
    
        soup=BS(response.content,'html.parser')
    
        items=soup.find_all('div',class_='sc-cJSrbW dRyaGb')
        a=0
        text=''
        for i in items:
            j=i.find_all('p')
            print(len(j))
            for l in j:
                a+=1
                text+=l.text
        
                if a==12:
                    break
            if a==12:
                break
        text=text.replace("PAYSHANBA", "\n\nPAYSHANBA\n\n")
        text=text.replace("DUSHANBA", "\n\nDUSHANBA\n\n")
        text=text.replace("SESHANBA", "\n\nSESHANBA\n\n")
        text=text.replace("CHORSHANBA", "\n\nCHORSHANBA\n\n")
        text=text.replace("JUMA", "\n\nJUMA\n\n")
        text=text.replace("YAKSHANBA", "\n\nYAKSHANBA\n\n")
        bot.send_message(message.from_user.id,text)
        
    
    elif message.text=="Milliy TV":
        url='https://www.savol-javob.com/milliy-tv-dasturlari-bugungi/'
                
        session=requests.Session()
        response=session.get(url,headers=HEADERS)
    
        soup=BS(response.content,'html.parser')
    
        items=soup.find_all('div',class_='sc-cJSrbW jfrHCE')
        a=0
        text=''
        for i in items:
            j=i.find_all('h6')
            print(len(j))
            for l in j:
                a+=1
                text+=l.text
        
                if a==9:
                    break
            if a==9:
                break
        text=text.replace("PAYSHANBA", "\n\nPAYSHANBA\n\n")
        text=text.replace("DUSHANBA", "\n\nDUSHANBA\n\n")
        text=text.replace("SESHANBA", "\n\nSESHANBA\n\n")
        text=text.replace("CHORSHANBA", "\n\nCHORSHANBA\n\n")
        text=text.replace("JUMA", "\n\nJUMA\n\n")
        text=text.replace("YAKSHANBA", "\n\nYAKSHANBA\n\n")
        bot.send_message(message.from_user.id,text)
        
    elif message.text=="ZO`R TV":
        url='https://www.savol-javob.com/zor-tv-dasturlari-bugungi/'
                
        session=requests.Session()
        response=session.get(url,headers=HEADERS)
    
        soup=BS(response.content,'html.parser')
    
        items=soup.find_all('div',class_='sc-cJSrbW jfrHCE')
        a=0
        text=''
        for i in items:
            j=i.find_all('h6')
            print(len(j))
            for l in j:
                a+=1
                text+=l.text
        
                if a==10:
                    break
            if a==10:
                break
        text=text.replace("PAYSHANBA", "\n\nPAYSHANBA\n\n")
        text=text.replace("DUSHANBA", "\n\nDUSHANBA\n\n")
        text=text.replace("SESHANBA", "\n\nSESHANBA\n\n")
        text=text.replace("CHORSHANBA", "\n\nCHORSHANBA\n\n")
        text=text.replace("JUMA", "\n\nJUMA\n\n")
        text=text.replace("YAKSHANBA", "\n\nYAKSHANBA\n\n")
        bot.send_message(message.from_user.id,text)
    
bot.polling()
        
    
    
    
    