import sqlite3
from config import TOKEN
from telegram import Bot
from config import ERRORS_CHANNEL_ID

class DataBase(object):

    def __init__(self):
        self.con = sqlite3.connect('logs_anotherConcept.db')
        self.cur = self.con.cursor()

    def disconnect(self):
        return self.con.close()

    def check_before_recording(self, message):
        exist_id = self.cur.execute(
            "SELECT event_id FROM rvision_logs  WHERE event_id = '{}';".format(message[0])).fetchall()
        return len(exist_id)

    def save_to_db(self, message):

        try:
            self.cur.execute(
                "INSERT INTO rvision_logs VALUES ('{}', '{}');".format(message[0], message[1])
            )
            self.con.commit()

        except sqlite3.Error as er:
            bot = Bot(token=TOKEN)

            bot.send_message(
                chat_id=ERRORS_CHANNEL_ID,
                text="Ошибка записи в БД!!!\nINSERT INTO rvision_logs VALUES ('{}', '{}');".format(message[0], message[1])
            )
