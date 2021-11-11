from command_line_argument_parser import UserArgumentParser
from irc_connection import Client
from dotenv import load_dotenv
from parser import Parser
from customizer import Customizer
from config import Configuration
import os

load_dotenv()

def receive_command_line_arguments():
    user_argument_parser = UserArgumentParser()
    return user_argument_parser.parse_all_arguments()

def parse_args():
    args = receive_command_line_arguments()
    nickname = getattr(args, "nickname")
    channel_name = getattr(args, "channel")
    oauth_token = open(".cfg", "r").read()
    return nickname, channel_name, oauth_token

class TwitchChat:
    ADDRESS = "irc.chat.twitch.tv"
    PORT = 6667

    def __init__(self, nickname : str, channel : str, oauth_token : str):
        self.client = Client(TwitchChat.ADDRESS, TwitchChat.PORT)
        self.nickname = nickname
        self.channel = "#" + channel
        self.parser = Parser()
        self.customizer = Customizer()
        self.OAUTH_TOKEN = oauth_token

    def join_channel(self, channel_name : str):
        self.client.join(channel_name)

    def send_credentials_to_server(self):
        self.client.send_oauth_token_to_server(self.OAUTH_TOKEN)
        self.client.send_nick_to_server(self.nickname)

    def make_beautiful_printing(self, color : str, user : str, message : str):
        print(f"{color}[{user}]{self.customizer.RESET_ANSI_CODE}", end = " ")
        print(f"|| {message}")

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
    configuration = Configuration()

    if not configuration.config_file_exists():
        configuration.make_config_file()

    nickname, channel_name, oauth_token = parse_args()

    chat = TwitchChat(nickname, channel_name, oauth_token)
    chat.run()
main()
