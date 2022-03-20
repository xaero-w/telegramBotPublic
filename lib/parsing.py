from re import findall


class Parsing(object):

    def __init__(self):
        self.REGEX_PARSING_ID = r'(^Id:\s)(.+?)(\t|\s)'
        self.REGEX_PARSING_MESSAGE = r'(Message:\s)(.[\s\S]*)(^Id:\s|$)'
        self.REGEX_CHECKING_START_NEW_LINE = r'(^Id:)'
        self.REGEX_CHECKING_MESSAGE_FOR_TAG = r'(Заявка на доступ)'
        self.REGEX_CHECKING_WORD_IN_A_MESSAGE = r'(?i)(swift)'

    def checking_start_new_line(self, read_line):
        if findall(self.REGEX_CHECKING_START_NEW_LINE, read_line):
            return True
        else:
            return False

    def read_message(self, read_line):
        event_id = findall(self.REGEX_PARSING_ID, read_line)
        parsing_id = event_id[0][1].strip()

        event_message = findall(self.REGEX_PARSING_MESSAGE, read_line)
        if (event_message != []) and (event_message[0][1].strip() != ''):
            parsing_message = event_message[0][1].replace('='*60, '='*28)
        else:
            parsing_message = 'N/A'

        parsing_text = [parsing_id, parsing_message.replace("'", "")]

        if parsing_text[1] == 'N/A':
            return []
        else:
            return parsing_text
