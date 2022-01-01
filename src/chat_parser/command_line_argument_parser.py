import argparse

GITHUB_REPOSITORY_LINK = "https://github.com/HicaroD/tChat"


class UserArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Twitch Chat that runs on terminal",
            epilog=f"In case of you don't know how to setup: {GITHUB_REPOSITORY_LINK}",
        )

    def add_argument_for_channel_name(self):
        self.parser.add_argument(
            "-ch",
            "--channel",
            type=str,
            help="Name of the channel that you want to join",
            required=True,
        )

    def parse_all_arguments(self):
        self.add_argument_for_channel_name()
        return self.parser.parse_args()
