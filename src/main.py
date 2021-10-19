from irc_connection import Client
from dotenv import load_dotenv
from parser import Parser
from customizer import Customizer
from colorama import Style
import os

"""
TODO:
    [X] Print chat on terminal
    [X] Parse IRC message (separate all components, such as nickname, type, message).
    [X] Customize parsed IRC message (colors and more for the username and message).
    [] Add support to simple emojis (Unicode).
    [] Insert nickname and channel name with command-line arguments.
    [] Handle cases when nickame / channel name doesn't exist or just failed for some reason.
"""

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

    def run(self):
        self.client.connect()
        self.send_credentials_to_server()
        self.join_channel(self.channel)

        while 1:
            unparsed_twitch_chat = self.client.get_data_from_irc_server_response().decode()

            if "PRIVMSG" in unparsed_twitch_chat:
                user_text_color = self.customizer.select_color_for_text()

                user, message = self.parser.parse_message(unparsed_twitch_chat)

                if str(message).endswith("\r\n"):
                    message = str(message)[:-4]

                print(f"{user_text_color}[{user}]", end = " ")
                print(Style.RESET_ALL, end = " ")
                print(f"< {message} >")

            elif "PING" in unparsed_twitch_chat:
                self.client.send_pong_to_server()


def main():
    chat = TwitchChat("hicaro____", "gaules")
    chat.run()

main()
