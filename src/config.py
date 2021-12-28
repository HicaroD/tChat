import os
import getpass


class InvalidOAuthToken(Exception):
    """Raised when the oauth token from the user input or .cfg is not valid."""

    def __init__(
        self,
        message="Invalid OAuth token. The token should looks like this: 'oauth:0smq58szgnf58ti7h12382askda31o'",
    ):
        self.message = message
        super().__init__(self.message)


class Configuration:
    def config_file_exists(self) -> bool:
        return os.path.exists(".cfg")

    def is_a_valid_oauth_token(self, token: str) -> bool:
        return token.startswith("oauth:")

    def make_config_file(self):
        try:
            with open(".cfg", "x") as file:
                token = self.ask_for_oauth_token()

                if not self.is_a_valid_oauth_token(token):
                    raise InvalidOAuthToken()

                else:
                    file.write(token.rstrip())

        except InvalidOAuthToken:
            print(
                "You can directly insert your oauth token in the .cfg stored in src/, with no extra spaces in the file"
            )

    def ask_for_oauth_token(self):
        return getpass.getpass("Insert your Twitch OAuth Token: ")
