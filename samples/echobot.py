from ancientgram import ancientgram

bot = ancientgram.Ancientgram("123456:your_token")

def handle_update(update):
    print(update)
    bot.sendMessage(chat_id=update['message']['from']['id'], text=update['message']['text'])
bot.loop(handle_update)
