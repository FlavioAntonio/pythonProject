import telebot
import os
import platform

# cria uma instancia do bot
bot = telebot.TeleBot('6349438511:AAFIaITWjswPa259XF5m8yTsVPkPhxzAmJ8')


# Defina um manipulador de mensagens

# @bot.message_handler(content_types=['text'])
# def receber_texto(message):
# Armazene o texto da mensagem na variável
# texto = message.text

# Faça algo com o texto
# if texto == 'Ola':
#     bot.send_message(message.chat.id, "bom dia")
# else:
#     bot.send_message(message.chat.id, "Boa noite")

# bot.send_message(message.chat.id,'Meu primeiro Bot utilizando o python')
# print(texto)

def execute_bate(filename):
    os.system(filename)
    #bot.send_message(message.chat.id, 'Escript executado')

@bot.message_handler(content_types=['text'])
def ativar_windows(message):
    executar = message.text
    if executar == "1":
        execute_bate(r"C:\Users\AN20165014\Documents\script\windows.bat")
    else:
        bot.send_message(message.chat.id,"Valor invalido")





# Inicie o bot
bot.polling()
