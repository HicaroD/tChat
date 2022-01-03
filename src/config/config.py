import os
import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()

    @staticmethod
    def config_file_exists(self) -> bool:
        return os.path.exists("./config.ini")

    @staticmethod
    def ask_for_nickname(self):
        return input("Insert your Twitch nickname: ")

    @staticmethod
    def ask_for_oauth_token(self):
        return input("Insert your Twitch OAuth Token:")

    @staticmethod
    def is_a_valid_oauth_token(self, token: str) -> bool:
        return token.startswith("oauth:")

    @staticmethod
    def is_valid_nickname(self, nickname: str):
        return not nickname.isspace() and nickname != ""

    def make_config_file(self):
        nickname = Configuration.ask_for_nickname()
        oauth_token = Configuration.ask_for_oauth_token()

        if Configuration.is_valid_nickname(
            nickname
        ) and Configuration.is_a_valid_oauth_token(oauth_token):
            self.config["IRC"] = {"nickname": nickname, "oauth_token": oauth_token}

            with open("config.ini", "w") as configuration_file:
                self.config.write(configuration_file)

        else:
            print("Please insert a valid nickname and an oauth token")
            exit()
