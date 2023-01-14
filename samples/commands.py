from ancientgram import ancientgram

bot = ancientgram.Ancientgram("123456:your_token")
bot.getMe()

def handle_update(update):
    message = update['message']['text']

    if message == "/start":
        bot.sendMessage(chat_id=update['message']['from']['id'], text="Hi, thanks for starting me!")
    if message == "/who":
        bot.sendMessage(chat_id=update['message']['from']['id'], text="Hi, I'm using Ancientgram!")
    if message == "/help":
        bot.sendMessage(chat_id=update['message']['from']['id'], text="Help message, my commands are /help and /who")
bot.loop(handle_update)
