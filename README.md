# Ancientgram 1.0.0
# Telegram Bot Api Framework for Python
This is a really simple Framework for creating bots
# Install
```
pip3 install ancientgram
```
# Usage
```
from ancientgram import ancientgram

bot = ancientgram.Ancientgram("5765870339:AAFCkjZbvpRGZQoNXSBo2wzE3oAque8XEaE")
bot.getMe()

def handle_update(update):
    print(update)
bot.loop(handle_update)
```
