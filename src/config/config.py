import os
import configparser


class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def config_file_exists(self) -> bool:
        return os.path.exists("./config.ini")

    def ask_for_nickname(self):
        return input("Insert your Twitch nickname: ")

    def ask_for_oauth_token(self):
        return input("Insert your Twitch OAuth Token:")

    def is_a_valid_oauth_token(self, token: str) -> bool:
        return token.startswith("oauth:")

    def is_valid_nickname(self, nickname: str):
        return not nickname.isspace() and nickname != ""

    def make_config_file(self):
        nickname = self.ask_for_nickname()
        oauth_token = self.ask_for_oauth_token()

        if self.is_valid_nickname(nickname) and self.is_a_valid_oauth_token(
            oauth_token
        ):
            self.config["IRC"] = {"nickname": nickname, "oauth_token": oauth_token}

            with open("config.ini", "w") as configuration_file:
                self.config.write(configuration_file)

        else:
            print("Please insert a valid nickname and an oauth token")
            exit()
