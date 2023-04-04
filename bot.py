import telegram


def send_message(text, chat_id, token):
    bot = telegram.Bot(token)
    bot.send_message(text=text, chat_id=chat_id)


def send_image(path, chat_id, token):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as image:
        bot.send_document(chat_id=chat_id, document=image, timeout=100)
