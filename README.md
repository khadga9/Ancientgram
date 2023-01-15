# Ancientgram 1.0.0
# Telegram Bot Api Framework for Python
A simple way for creating bots in Telegram using Python. This Framework supports every method in the Bot Api.
# Install
```
pip3 install ancientgram
```
# Usage
## Creating the bot
```
from ancientgram import ancientgram

bot = ancientgram.Ancientgram("123456:your_token")
```
## Getting updates
```
def handle_update(update):
    print(update)
bot.loop(handle_update)
```
# Samples
## Echo Bot
```
from ancientgram import ancientgram

bot = ancientgram.Ancientgram("123456:your_token")

def handle_update(update):
    try:
        bot.sendMessage(chat_id=update['message']['from']['id'], text=update['message']['text'])
    except:
        pass
bot.loop(handle_update)
```
For samples see [samples](https://github.com/khadga9/Ancientgram/tree/main/samples)
