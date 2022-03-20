class Message(object):

    def __init__(self, parsing_message):
        self.event_id = parsing_message[0]
        self.event_message = parsing_message[1]

    def get_message_text(self):
        return ('ID: {}\n'.format(self.event_id) +
                'Message: {}\n'.format(self.event_message[0:3000]))

    def get_short_message_text(self):
        return ('Risk_type: {}\n'.format(self.event_risk) +
                'ID: {}\n'.format(self.event_id))

    def id_message(self):
        return self.event_id.strip()

    def for_save_to_db(self):
        return self.event_id, self.event_message
