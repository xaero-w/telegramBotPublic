from time import sleep
from telegram import Bot
from config import TOKEN
from config import CHANNEL_ID_WORK_CHAT
from config import ERRORS_CHANNEL_ID
from lib.data_base import DataBase
from lib.message import Message
from lib.parsing import Parsing


bot = Bot(token=TOKEN)
parsing = Parsing()
db = DataBase()
buffer = ""

while True:
    file = open("data/logs_new_format.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    for line in lines:

        if parsing.checking_start_new_line(line):
            # Блок условий 1.
            # Если буффер(предыдущая строка) содержит метку начала лога и строка не является последней.
            if (parsing.checking_start_new_line(buffer)) and (line != lines[-1]):
                new_message = parsing.read_message(buffer)

                if new_message != []:
                    message = Message(new_message)

                    if db.check_before_recording(new_message) == 0:
                        db.save_to_db(new_message)

                        # print(message.get_message_text())
                        try:
                            bot.send_message(
                                chat_id=CHANNEL_ID_WORK_CHAT,
                                text=message.get_message_text()
                            )

                        except:
                            bot.send_message(
                                chat_id=ERRORS_CHANNEL_ID,
                                text="Блок условий 1\n!!!EXCEPT!!!\n{}".format(message.get_message_text())
                            )

                        sleep(3)

                buffer = ""

            # Блок условий 2.
            # Если буфер имеет метку начала лога и строка является последней в списке.
            # Парсим содержимое буфера.
            if (parsing.checking_start_new_line(buffer)) and (line == lines[-1]):
                new_message = parsing.read_message(buffer)

                if new_message != []:
                    message = Message(new_message)

                    if db.check_before_recording(new_message) == 0:
                        db.save_to_db(new_message)

                        # print(message.get_message_text())
                        try:
                            bot.send_message(
                                chat_id=CHANNEL_ID_WORK_CHAT,
                                text=message.get_message_text()
                            )
                        except:
                            bot.send_message(
                                chat_id=ERRORS_CHANNEL_ID,
                                text="Блок условий 2\n!!!EXCEPT!!!\n{}".format(message.get_message_text())
                            )

                        sleep(3)

                # Парсим содержимое строки.
                new_message = parsing.read_message(line)

                if new_message != []:
                    message = Message(new_message)

                    if db.check_before_recording(new_message) == 0:
                        db.save_to_db(new_message)

                        # print(message.get_message_text())
                        try:
                            bot.send_message(
                                chat_id=CHANNEL_ID_WORK_CHAT,
                                text=message.get_message_text()
                            )
                        except:
                            bot.send_message(
                                chat_id=ERRORS_CHANNEL_ID,
                                text="Блок условий 2.1\n!!!EXCEPT!!!{}".format(message.get_message_text())
                            )

                        sleep(3)

                    buffer = ""

            buffer += line
        else:
            # Блок условий 3.
            # Если строка является последней строкой.
            if line == lines[-1]:
                buffer += line
                new_message = parsing.read_message(buffer)

                if new_message != []:
                    message = Message(new_message)

                    if db.check_before_recording(new_message) == 0:
                        db.save_to_db(new_message)

                        # print(message.get_message_text())
                        try:
                            bot.send_message(
                                chat_id=CHANNEL_ID_WORK_CHAT,
                                text=message.get_message_text()
                            )
                        except:
                            bot.send_message(
                                chat_id=ERRORS_CHANNEL_ID,
                                text="Блок условий 3\n!!!EXCEPT!!!\n{}".format(message.get_message_text())
                            )

                        sleep(3)

                buffer = ""

            else:
                buffer += line
