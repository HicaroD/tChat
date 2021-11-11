import os
import getpass

class Configuration:
    def config_file_exists(self) -> bool:
        return os.path.exists(".cfg")

    def make_config_file(self):
        with open(".cfg", "x") as f:
            password = self.ask_for_oauth_token()
            f.write(password.rstrip())

    def ask_for_oauth_token(self):
        return getpass.getpass("Insert your Twitch OAuth Token: ")
