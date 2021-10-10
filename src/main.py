from irc_connection import Client
from dotenv import load_dotenv
from parser import Parser
import os

"""
TODO:
    [X] Connect to IRC server
    [X] Print chat on terminal
    [] Parse IRC message (separate all components, such as nickname, type, message)
    [] Customize parsed IRC message (colors and more)
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
                user, message = self.parser.parse_message(unparsed_twitch_chat)
                print(user, message)

            elif "PING" in unparsed_twitch_chat:
                print("PINGING SERVER")
                self.client.send_pong_to_server()


def main():
    chat = TwitchChat("hicaro____", "gaules")
    chat.run()

main()
