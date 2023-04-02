import telegram
from environment import get_bot_token, get_chat_id


def send_message(text, chat_id, token):
    bot = telegram.Bot(token)
    bot.send_message(text=text, chat_id=chat_id)


def send_image(path, chat_id, token):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=open(path, 'rb'))


def main():
    path = 'images/nasa_epic_3.png'
    bot_token = get_bot_token()
    chat_id = get_chat_id()
    if bot_token and chat_id:
        send_image(path, chat_id, bot_token)


if __name__ == "__main__":
    main()