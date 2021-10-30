from command_line_argument_parser import UserArgumentParser
from irc_connection import Client
from dotenv import load_dotenv
from parser import Parser
from customizer import Customizer
from colorama import Style
import os

load_dotenv()

class TwitchChat:
    ADDRESS = "irc.chat.twitch.tv"
    PORT = 6667
    OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")

    def __init__(self, nickname : str, channel : str):
        self.client = Client(TwitchChat.ADDRESS, TwitchChat.PORT)
        self.nickname = nickname
        self.channel = "#" + channel
        self.parser = Parser()
        self.customizer = Customizer()

    def join_channel(self, channel_name : str):
        self.client.join(channel_name)

    def send_credentials_to_server(self):
        self.client.send_oauth_token_to_server(TwitchChat.OAUTH_TOKEN)
        self.client.send_nick_to_server(self.nickname)

    def make_beautiful_printing(self, color : str, user : str, message : str):
        print(f"{color}[{user}]", end = " ")
        print(Style.RESET_ALL, end = " ")
        print(f"< {message}")

    def run(self):
        self.client.connect()
        self.send_credentials_to_server()
        self.join_channel(self.channel)

        while 1:
            unparsed_twitch_chat = self.client.get_data_from_irc_server_response().decode()

            if "PRIVMSG" in unparsed_twitch_chat:
                user_text_color = self.customizer.select_color_for_text()
                user, message = self.parser.parse_message(unparsed_twitch_chat)
                self.make_beautiful_printing(user_text_color, user, message)

            elif "PING" in unparsed_twitch_chat:
                self.client.send_pong_to_server()


def main():
    user_argument_parser = UserArgumentParser()
    args = user_argument_parser.parse_all_arguments()

    nickname = getattr(args, "nickname"))
    channel_name = getattr(args, "channel"))

    chat = TwitchChat(nickname, channel)
    chat.run()
main()
