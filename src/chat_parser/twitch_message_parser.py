class Parser:
    @staticmethod
    def has_new_line_at_the_end(twich_chat_message: str) -> bool:
        return twich_chat_message.endswith("\r\n")

    @staticmethod
    def delete_new_line_at_the_end(twitch_chat_message: str) -> str:
        return "".join(list(twitch_chat_message)[:-2:])

    @staticmethod
    def parse_message(message: str):
        splited_message = message.split(":")
        user = splited_message[1].split("!")[0]
        message = "".join(splited_message[2::])

        if Parser.has_new_line_at_the_end(message):
            message = Parser.delete_new_line_at_the_end(message)
            return user, message

        return user, message
