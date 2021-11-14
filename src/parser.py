class Parser:
    def has_new_line_at_the_end(self, twich_chat_message : str) -> bool:
        return twich_chat_message.endswith("\r\n")

    def delete_new_line_at_the_end(self, twitch_chat_message : str) -> str:
        return "".join(list(twitch_chat_message)[:-2:])

    def parse_message(self, message : str):
        splited_message = message.split(":")
        user = splited_message[1].split("!")[0]
        message = "".join(splited_message[2::])

        if self.has_new_line_at_the_end(message):
            message = self.delete_new_line_at_the_end(message)
            return user, message

        return user, message
