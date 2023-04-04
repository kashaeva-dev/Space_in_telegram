import telegram


def send_image(path, chat_id, token):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as image:
        bot.send_document(chat_id=chat_id, document=image, timeout=100)
