import os
import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def config_file_exists(self) -> bool:
        return os.path.exists("./config.ini")

    def is_a_valid_oauth_token(self, token: str) -> bool:
        return token.startswith("oauth:")

    def ask_for_nickname(self):
        return input("Insert your Twitch nickname: ")

    def ask_for_oauth_token(self):
        return input("Insert your Twitch OAuth Token:")

    def make_config_file(self):
        self.config["IRC"] = {
            "nickname": self.ask_for_nickname(),
            "oauth_token": self.ask_for_oauth_token(),
        }

        with open("config.ini", "w") as configuration_file:
            self.config.write(configuration_file)

    def get_nickname(self):
        self.config.read("config.ini")
        return self.config["IRC"]["nickname"]

    def get_oauth_token(self):
        self.config.read("config.ini")
        return self.config["IRC"]["oauth_token"]
