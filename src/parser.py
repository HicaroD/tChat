class Parser:
    def parse_message(self, message : str):
        splited_message = message.split(":")
        user = splited_message[1].split("!")[0]
        message = splited_message[2]

        if message.endswith("\r\n"):
            message = "".join(list(message)[:-2:])
            return user, message

        return user, message
