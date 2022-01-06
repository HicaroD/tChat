class Parser:
    @staticmethod
    def has_new_line_at_the_end(twitch_chat_message: str) -> bool:
        return twitch_chat_message.endswith("\r\n")

    @staticmethod
    def delete_new_line_at_the_end(twitch_chat_message: str) -> str:
        return "".join(list(twitch_chat_message)[:-2:])

    @staticmethod
    def extract_data_from_irc_message(unparsed_irc_message : str):
        unparsed_nickname = unparsed_message = ""

        if unparsed_irc_message[0] == ":":
            unparsed_irc_message = unparsed_irc_message[1::]

            for character in unparsed_irc_message:
                if character == ":":
                    unparsed_nickname = unparsed_irc_message[:unparsed_irc_message.index(character):]
                    unparsed_message = unparsed_irc_message[unparsed_irc_message.index(character)::]
                    break

        return unparsed_nickname, unparsed_message

    @staticmethod
    def parse_user_message(unparsed_message: str):
        message = unparsed_message[1::]

        if Parser.has_new_line_at_the_end(message):
            message = Parser.delete_new_line_at_the_end(message)
            return message

        return message

    @staticmethod
    def parse_nickname(unparsed_nickname: str):
        return unparsed_nickname.split('!')[0]

    def get_parsed_twitch_chat_data(self, unparsed_irc_message):
        unparsed_nickname, unparsed_message = Parser.extract_data_from_irc_message(unparsed_irc_message)
        nickname = Parser.parse_nickname(unparsed_nickname)
        message = Parser.parse_user_message(unparsed_message)
        return nickname, message
