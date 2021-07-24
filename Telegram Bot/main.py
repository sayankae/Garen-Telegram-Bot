import telegram_key as keys
from telegram.ext import *
from datetime import datetime
import Functions as translate
import requests
import re

print("Bot Started.....")
def sample_responses(input_text):
    if input_text in ("hello","hi","namaste"):
        return "Hello, I am Garen, How are you doing?"

    elif input_text in ("help","functions","help!"):
        return "I can send cute dog pics! and tell current time"
    
    elif input_text in ("time","what is the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    else:
        return "Sorry i dont get it!"

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def start_command(update, context):
    print("Type Something")
    update.message.reply_text("Type something")

def help_command(update, context):
    print("Bruh")
    update.message.reply_text("Bruh")

def woof(update, context):
    print("woof")
    url = get_image_url()
    update.message.reply_photo(url)

def handle_message(update, context):
    #print("Handling")
    text = str(update.message.text).lower()
    print(text)
    if "translate" in text:
        text = text[9::]
        response = translate.translating(text)
        update.message.reply_text(response)
    else:
        response = sample_responses(text)
        update.message.reply_text(response)

def error(update, context):
    print(f"Update{update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("woof",woof))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()