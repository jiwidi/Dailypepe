import telebot
import time
import random
import os
import glob
import datetime
import threading
import json
from time import gmtime, strftime
from telebot import types
global cinturon

grupos=[]
fileG=open('grupos.txt').read()
grupos=json.loads(fileG)
token=open('token.txt').read()
pepe=token
bot=telebot.TeleBot(pepe)
@bot.message_handler(commands=['help'])
def send_Pepe(message):
    bot.send_message(message.chat.id,'Here is a list of commands: \n /getpepe NUM : get\'s you the pepe NUM \n /randompepe get a random pepe ');
@bot.message_handler(commands=['getpepe'])
def send_Pepe(message):
    try:
        if(not (message.chat.id in grupos) and (not message.chat.type=='private')and (not message.chat.type=='channel')):
            grupos.append(message.chat.id)
            save()
    except:
        bot.send_message(message.chat.id,'opps');
    try:
        number=message.text[8:]
        aux=int(float(number))
        if(aux>=0 and aux<=1252):
            number=number.strip();
            filename = glob.glob(number+'*.*')
            extension= os.path.splitext(filename[0])[1]
            file= open(filename[0],'rb')
    
            if(extension==".gif"):
                bot.send_document(message.chat.id,file)
            else:
                file= open(filename[0],'rb')
                bot.send_photo(message.chat.id, file);
            file.close()
            if(aux==0):
	        save()
        else:
            bot.send_message(message.chat.id,'wrong number');
    except:
        bot.send_message(message.chat.id,'opps');
@bot.message_handler(commands=['randompepe'])
def send_Rpepe(message):
    try:
        if(not (message.chat.id in grupos) and (not message.chat.type=='private')and (not message.chat.type=='channel')):
            grupos.append(message.chat.id)
            save()
        id=random.randint(0,1252)
        #dir='/home/jiwidi/GITHUB/telebots/pepes'
        id=str(id)
        filename = glob.glob(id+'*.*')
        file= open(filename[0],'rb')
        extension= os.path.splitext(filename[0])[1]
        if(extension==".gif"):
            bot.send_document(message.chat.id,file)
        else:
            bot.send_photo(message.chat.id, file);
            bot.send_message(message.chat.id, 'pepe number: '+str(id));
        file.close();
    except:
        bot.send_message(message.chat.id,'opps');
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.from_user.id == 80169346:
        ko=random.randint(0,10)
        if(ko==5):
	    bot.reply_to(message,'jajaja mis dieses <3 kek such funny very awuita de koko')
    try:
        rand=random.randint(0,150)
        if(rand==88 and (not('pepe' in message.text)) ):
            for u in range(len(grupos)):
                #if(grupos[u]==message.chat.id):
                id=random.randint(0,1252)
                #dir='/home/jiwidi/GITHUB/telebots/pepes'
                id=str(id)
                filename = glob.glob(id+'*.*')
                file= open(filename[0],'rb')
                extension= os.path.splitext(filename[0])[1]
                if(extension==".gif"):
                    bot.send_document(grupos[u],file)
                    bot.send_message(grupos[u], 'a random pepe appears: '+str(id));
                else:
                    bot.send_photo(grupos[u], file);
                    bot.send_message(grupos[u], 'a random pepe appears: '+str(id));
    except:
        bot.send_message(message.chat.id,'opps');

def save(): 
    writer=open('grupos.txt','w')
    aux=json.dumps(grupos)
    writer.write(aux)
    writer.close()
def randomPepeToAllGroups():
    try:
        for k in range(len(grupos)):
            randomPepeTo(grupos[k])
    except:
        hola='hola'
def randomPepeTo(targetId):
    try:
        id=random.randint(0,1252)
        id=str(id)
        filename = glob.glob(id+'*.*')
        file= open(filename[0],'rb')
        extension= os.path.splitext(filename[0])[1]
        if(extension==".gif"):
            bot.send_document(targetId,file)
            bot.send_message(targetId, 'a random pepe appears: '+str(id));
        else:
            bot.send_photo(targetId, file);
            bot.send_message(targetId, 'a random pepe appears: '+str(id));
    except:
         hola='hola'
bot.polling()
