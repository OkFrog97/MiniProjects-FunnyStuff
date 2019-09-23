# Simple telegram bor, which repeat your message in telegramm
# Name: test_bot;
# Username: test23092019_bot

# add token
token = "942108158:AAEvqWvMWSmhBXks5s_n7La2npUnbZVr6ds"

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)