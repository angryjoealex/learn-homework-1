import logging
import settings
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

    
def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_planet_place(update, context): 
    try:
        planet = update.message.text.split(" ")
        if hasattr(ephem, planet[1]):
            planet_info = getattr(ephem, planet[1])()
            #print(planet_info)
            print(planet_info.name)
            planet_info.compute(datetime.date.today())
            planet_place = ephem.constellation(planet_info)
            # print (planet_place)
            # print(len(planet_place))
            # print(type(planet_place))
            update.message.reply_text(planet_place)
        else:
             update.message.reply_text("Введенная планета не найдена")            
    except IndexError:
         update.message.reply_text("Вы не ввели название планеты")
 

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_place))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()