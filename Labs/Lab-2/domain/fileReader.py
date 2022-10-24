from utils import tokens


class FileReader:
    def __init__(self, filename):
        self.__filename = filename
        self.__tokens = []

    def open_file(self):
        return open(self.__filename, "r")

    def parse_file(self):
        file_stream = self.open_file()
        crt_token = ""

        for character in file_stream:
            if character not in tokens.separators:
                crt_token += character
            else:
                self.__tokens.append(crt_token)
                crt_token = ""

    def get_tokens(self):
        return self.__tokens
