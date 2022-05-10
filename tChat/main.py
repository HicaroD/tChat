from tChat.command_line_argument_parser import UserArgumentParser
from tChat.irc_connection import Client
from tChat.twitch_message_parser import Parser
from tChat.customizer import Customizer
from tChat.config import Configuration, config_file_exists
from configparser import ConfigParser
import asyncio


def receive_command_line_arguments():
    user_argument_parser = UserArgumentParser()
    return user_argument_parser.parse_all_arguments()


def get_channel_name_from_command_line():
    args = receive_command_line_arguments()
    channel_name = getattr(args, "channel")
    return channel_name


class BotConfiguration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")

    # Configuration keys: "oauth_token" and "nickname"
    def __getitem__(self, configuration_key):
        return self.config["IRC"][configuration_key]


class TwitchChat:
    ADDRESS = "irc.chat.twitch.tv"
    PORT = 6667

    def __init__(self, bot_configuration: BotConfiguration, channel: str):
        self.client = Client(TwitchChat.ADDRESS, TwitchChat.PORT)
        self.bot_configuration = bot_configuration
        self.channel = "#" + channel
        self.parser = Parser()
        self.customizer = Customizer()
        self.users = {}

    async def join_channel(self):
        await self.client.join(self.channel)

    async def send_credentials_to_server(self):
        oauth_token = self.bot_configuration["oauth_token"]
        bot_name = self.bot_configuration["nickname"]

        await self.client.send_oauth_token_to_server(oauth_token)
        await self.client.send_nick_to_server(bot_name)

    def make_beautiful_printing(self, color: str, nickname: str, message: str):
        print(f"{color}[{nickname}]{self.customizer.RESET_ANSI_CODE}", end=" ")
        print(f"{message}")

    def is_user_message(self, message):
        return "PRIVMSG" in message

    def is_connection_message(self, message):
        return "You are in a maze of twisty passages, all alike." in str(message)

    def is_ping_message_from_server(self, message):
        return "PING" in message

    def get_user_color(self, nickname):
        if nickname in self.users.keys():
            return self.users[nickname]
        else:
            random_color = self.customizer.select_color_for_text()
            self.users[nickname] = random_color
            return random_color

    async def run(self):
        try:
            await self.client.connect()
            await self.send_credentials_to_server()
            await self.join_channel()

            while 1:
                unparsed_twitch_chat_message = (
                    await self.client.get_data_from_irc_server_response()
                )

                decoded_twitch_chat_messages = (
                    unparsed_twitch_chat_message.decode().split("\n")[0]
                )

                nickname, message = self.parser.get_parsed_twitch_chat_data(
                    decoded_twitch_chat_messages
                )

                user_text_color = self.get_user_color(nickname)

                if self.is_user_message(decoded_twitch_chat_messages):
                    self.make_beautiful_printing(user_text_color, nickname, message)

                elif self.is_connection_message(unparsed_twitch_chat_message):
                    self.make_beautiful_printing(
                        user_text_color,
                        "You",
                        f"are connected to {self.channel[1::]}'s chat",
                    )

                elif self.is_ping_message_from_server(decoded_twitch_chat_messages):
                    await self.client.send_pong_to_server()

        except KeyboardInterrupt:
            self.make_beautiful_printing(user_text_color, "You", "are disconnected")


async def main():
    configuration = Configuration()

    if not config_file_exists():
        configuration.make_config_file()

    bot_configuration = BotConfiguration()
    channel_name = get_channel_name_from_command_line()

    chat = TwitchChat(bot_configuration, channel_name)
    await chat.run()

def _main():
    asyncio.run(main())

if __name__ == "__main__":
    _main()
