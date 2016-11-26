import telebot
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
    if(not (message.chat.id in grupos)):
        grupos.append(message.chat.id)
        save()
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
    if(not (message.chat.id in grupos)):
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
@bot.message_handler(func=lambda m: True)
def echo_all(message):
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


def save(): 
    writer=open('grupos.txt','w')
    aux=json.dumps(grupos)
    writer.write(aux)
    writer.close()

bot.polling()
