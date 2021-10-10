class Parser:
    def parse_message(self, message : str):
        splited_message = message.split(":")
        user = splited_message[1].split("!")[0]
        message = splited_message[2]
        return user, message
