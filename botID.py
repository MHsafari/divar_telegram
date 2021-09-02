import telegram
import json

f = open("data.json")
data=json.load(f)


bot = telegram.Bot(token=data['my_token_sell'])
# print(bot.get_me())
updates = bot.get_updates()
print(updates[0]['channel_post']['sender_chat']['id'])


my_token = data["my_token_sell"]
chat_id = data["chat_id_sell"]

chat="Hello Test"
def send(msg, chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


send(chat, chat_id, my_token)
