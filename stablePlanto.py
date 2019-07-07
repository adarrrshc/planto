# -*- coding: utf-8 -*-
import requests
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from lxml import html

import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

points=0

bot_token='648255198:AAG2MuauxswxYdibqHSQ_4OMAiLt4SQd5ig'

updater=Updater(token='648255198:AAG2MuauxswxYdibqHSQ_4OMAiLt4SQd5ig')
dispatcher = updater.dispatcher
jq = updater.job_queue

admin_id=128895599
users=[]
user_data=[]

jq = updater.job_queue

plant_name=""


links={
    "Tomato":"https://www.amazon.in/Tomato-Seeds-by-Kraft/dp/B00KOKXQWU",
    "Beans":"https://www.amazon.in/Seedscare-India-Beans-Super-Packets/dp/B01GJVF80K/ref=sr_1_1?keywords=beans&qid=1562423725&s=garden&sr=1-1",
    "Cherry":"https://www.amazon.in/National-Gardens-Sweet-Cherry-Fruit/dp/B01GD9556K/ref=sr_1_5?keywords=cherry&qid=1562426994&s=garden&sr=1-5"
}

tips={
    "Tomato":"Optimize Tomato Farming::https://youtu.be/6DSqcqKu6wI",
    "Beans":"Boost Beans Farming::https://youtu.be/F4d5qbyyPFU",
    "Cherry":"Improve Cherry Production::https://www.youtube.com/watch?v=gjGlux2byAY"
}


def init_bknd():
    global users
    global user_data
    for t in users:
        user_data.append([int(t),0,0,""])




def start(bot, update):
    global user_data
    flag=0
    for ud in user_data:
        if(int(ud[0])==update.message.chat_id):
            flag=1
            break

    if(flag==0):
        user_data.append([update.message.chat_id,0,0,""])
                           #chatid,points,level 
    try:
        #animation="https://compote.slate.com/images/697b023b-64a5-49a0-8059-27b963453fb1.gif"
        #bot.send_animation(update.message.chat_id, animation)
        print("inside start\n")
        
        bot.send_message(chat_id=update.message.chat_id,parse_mode="HTML", text="Welcome To Planto "+update.message.chat.first_name+"🌱")
        
        bot.send_message(chat_id=update.message.chat_id, text="Choose Your Option!", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/Plants"],["/Profile"],["/Challenges"],
                                                                                                            
                
                                                                                                            ]))
    except Exception as e:
        print(e)    


def back(bot,update):

    bot.send_message(chat_id=update.message.chat_id, text="Choose Your Option✨", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/Plants"],["/Profile"],["/Challenges"],
                                                                                                            
                
                                                                                                            ]))





    


def timeframe_chooser(bot,update):
    
    bot.send_message(chat_id=update.message.chat_id, text="Choose timeframe", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/daily"],
                                                                                                                              ["/weekly"],
                                                                                                                              ["/monthly"]],one_time_keyboard= False))





def choose_selection_bknd(bot,update):
    global points
    global user_data
        
    global sunsign
    global user_data
    t=""
    flag=0
    print(update.message.text)
    inpt=update.message.text
    #bot.send_message(chat_id=update.message.chat_id,text="Choose Plant!",parse_mode='Markdown')
    if(inpt=="/Plants"):
        print("Plants")
        bot.send_message(chat_id=update.message.chat_id, text="Choose Plant🌱", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/Tomato"],["/Beans"],["/Cherry"],
                                                                                                            
                
                                                                                                            ]))
    else:
        for ud in user_data:
            if(update.message.chat_id==int(ud[0])):
                flag=1
                points=ud[1]
                level=points//10
        if(flag==0):
            user_data.append([update.message.chat_id,0,0,""])
            points=0
            level=0
        #print(points)
        #print(user_data)
        #print("flag"+str(flag))
        
        out=update.message.chat.first_name+"\n\n"+"Points:"+str(points)+"\nLevel:"+str(level)+"\n\n/Share to Level Up!!"
        bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=True,text=out,parse_mode='Markdown')
        
        



def share(bot,update):
    
    global user_data
    print("share")
    whatsapp_share_text="[Share to Whatsapp]"+"(https://api.whatsapp.com/send?text="+"Hey i just Planted My Very first Tree!!!\n\nt.me/plantatreebot)"
        
    twitter_share_text="[Share to Twitter](https://twitter.com/intent/tweet?text=Hey+i+just+Planted+My+Very+first+Tree!!!&url=t.me/plantatreebot&hashtags=plantatreebot#plantatree)"
    out=whatsapp_share_text+"\n"+twitter_share_text
    print(out)
    for ud in user_data:
        if(update.message.chat_id==int(ud[0])):
            ud[1]=ud[1]+1
    bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=True,text=out,parse_mode='Markdown')

def plants_selection_bknd(bot,update):
    global plant_name
    print(update.message.text)
    plant_name=update.message.text
    
    bot.send_message(chat_id=update.message.chat_id, text="Choose Your Need✨", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/Buy"],["/Tips"],["/Back"]
                                                                                                            
                
                                                                                                            ]))



def buy_tips_bknd(bot,update):
    global plant_name
    global links
    global tips
    inpt=update.message.text
    print(plant_name.replace("/",""))
    if(inpt=="/Buy"):
        out=plant_name.replace("/","")+"\n\n"+"[Click To Buy "+plant_name.replace("/","")+"]("+links[plant_name.replace("/","")]+")"+"\n\nSet Your /Location"
        bot.send_message(chat_id=update.message.chat_id,parse_mode="Markdown" ,disable_web_page_preview=True,text=out)
    else:
        headline=tips[plant_name.replace("/","")].split("::")[0]
        link=tips[plant_name.replace("/","")].split("::")[1]
        out="Resources\n\n1."+"["+headline+"]"+"("+link+")"
        bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=True,parse_mode="Markdown" ,text=out)



def challenges_bknd(bot,update):
    out="1. *Progress Challenges*\n Keep your plant's growth accounted and gain points!.\nPress /Progress and upload photo.  \n\n2. *5 Plants in 1 Month.* \n Challenge yourself to nurture 5 plants a Month.\n Press /5pim and upload photo."
    bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False,parse_mode="Markdown" ,text=out)

prpgressor5pim="Progress"

def challenges_bknd_bknd(bot,update):
    global user_data
    global prpgressor5pim
    print(update.message.photo)
    


    flag=0
    for ud in user_data:
        if(int(ud[0])==update.message.chat_id):
            flag=1
            break

    if(flag==0):
        user_data.append([update.message.chat_id,0,0,""])



    
    #print(update.message.photo)
    file = bot.getFile(update.message.photo[-1].file_id)
    print(file.file_path)
    requests.get(file.file_path)
    f = open('image.jpg','wb+')
    f.write(requests.get(file.file_path).content)
    f.close()

    if(prpgressor5pim=="Progress"):
        print("progress")
        res=1
        if(res==1):
            print("tree")
            for ud in user_data:
                if(update.message.chat_id==int(ud[0])):
                    ud[1]=ud[1]+10
            print("point incremented by 10")
            print(user_data)   
            bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False,text="Thats a Healthy looking bud😊")
            

        else:
            print("no tree")
            bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False,text="Foolin us")

    else:
        print("5pim")
        for ud in user_data:
                if(update.message.chat_id==int(ud[0])):
                    ud[1]=ud[1]+5
        print("point incremented by 5")
        print(user_data)   
        bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False,text="Keep it Coming!😊")

    


def progress_5pim_bknd(bot,update):
    global prpgressor5pim
    inpt=update.message.text.replace("/","")
    prpgressor5pim=inpt
    bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False ,text="Upload Photo Now😊")
    

def locationsetter(bot,update):

    bot.send_message(chat_id=update.message.chat_id, text="Choose Your Location✨", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/Fortkochi"],["/Perumbavoor"],["/Kakkanad"],["/Back"]]))
                                                                                                            
                                                                                                       
    

def locationsetter_bknd(bot,update):
    global user_data
    inpt=update.message.text.replace("/","")
    if(inpt=="Fortkochi"):
        print("fk")
        loc="Fortkochi"
    elif(inpt=="Perumbavoor"):
        print("pvr")
        loc="Perumbavoor"
    elif(inpt=="Kakkanad"):
        loc="Kakkanad"
        print("Kkd")
    flag=0
    for ud in user_data:
        if(int(ud[0])==update.message.chat_id):
            ud[3]=loc

    print(user_data)
    out="Location Set 🌱"
    bot.send_message(chat_id=update.message.chat_id,disable_web_page_preview=False,text=out)  
    



#handlers
start_handler = CommandHandler('start', start)



#dispatchers
dispatcher.add_handler(start_handler)

dispatcher.add_handler(CommandHandler(["Plants",
                                       "Profile", 
                                       ], 
                                        choose_selection_bknd))
dispatcher.add_handler(CommandHandler(["Buy",
                                       "Tips", 
                                       ], 
                                        buy_tips_bknd))

dispatcher.add_handler(CommandHandler(["Progress",
                                       "5pim", 
                                       ], 
                                        progress_5pim_bknd))

dispatcher.add_handler(CommandHandler(["Tomato",
                                       "Beans",
                                       "Cherry", 
                                       
                                       ], 
                                        plants_selection_bknd))
                                        
dispatcher.add_handler(CommandHandler("Back",back))
dispatcher.add_handler(CommandHandler("Share",share))
dispatcher.add_handler(CommandHandler("Location",locationsetter))
dispatcher.add_handler(CommandHandler(["Fortkochi",
                                       "Perumbavoor",
                                       "Kakkanad", 
                                       
                                       ],locationsetter_bknd))





dispatcher.add_handler(CommandHandler("Challenges",challenges_bknd))



dispatcher.add_handler(MessageHandler(Filters.photo & (~ Filters.forwarded), challenges_bknd_bknd))

updater.start_polling()

if __name__ == "__main__":
    init_bknd()