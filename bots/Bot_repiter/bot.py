# Simple telegram bor, which repeat your message in telegram
# Name: test_bot;
# Username: test23092019_bot

# import other files and libs
import setting
import telebot

# add token
token = "942108158:AAEvqWvMWSmhBXks5s_n7La2npUnbZVr6ds"


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)
