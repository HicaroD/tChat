from irc_connection import Client
from dotenv import load_dotenv
import os

"""
TODO:
    [] Connect to IRC server
    [] Print chat on terminal
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
            print(unparsed_twitch_chat)

            if "PING" in unparsed_twitch_chat:
                self.client.send_pong_to_server()


def main():
    chat = TwitchChat("hicaro____", "gaules")
    chat.run()

main()
