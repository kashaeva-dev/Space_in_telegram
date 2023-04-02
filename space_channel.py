import telegram


def send_message():
    bot = telegram.Bot(token='6262224084:AAHQsOlVRGLg_-deC3aTAMzlGUtZmPzkUXg')
    bot.send_message(text='Всем привет!', chat_id=-1001852069690)


if __name__ == "__main__":
    send_message()
