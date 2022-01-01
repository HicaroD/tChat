import sys, os
import unittest

sys.path.insert(0, os.path.abspath("../src/"))

from chat_parser.twitch_message_parser import Parser


class TestTwitchChatParserMethods(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parser_for_nickname(self):
        nickname, _ = self.parser.parse_message(
            ":hicaro____!hicaro____@hicaro____.tmi.twitch.tv PRIVMSG #hicaro____ :testing"
        )
        self.assertEqual(nickname, "hicaro____")

    def test_parser_for_user_message(self):
        _, message = self.parser.parse_message(
            ":hicaro____!hicaro____@hicaro____.tmi.twitch.tv PRIVMSG #hicaro____ :testing"
        )
        self.assertEqual(message, "testing")


if __name__ == "__main__":
    unittest.main()
