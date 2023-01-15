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
For samples see [samples](https://github.com/khadga9/Ancientgram/tree/main/samples)
