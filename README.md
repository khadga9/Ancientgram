# Ancientgram 1.0.0
# Telegram Bot Api Framework for Python
A simple way for creating bots in Telegram using Python
# Install
```
pip3 install ancientgram
```
# Usage
```
from ancientgram import ancientgram

bot = ancientgram.Ancientgram("123456:your_token")
bot.getMe()

def handle_update(update):
    print(update)
bot.loop(handle_update)
```
