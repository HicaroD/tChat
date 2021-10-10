import socket


class Client:
    BUFFER_SIZE = 2040

    def __init__(self, address : str, port : int):
        self.address = address
        self.port = port
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.irc.connect((self.address, self.port))

    def send_command_to_server(self, command : str, message : str):
        self.irc.send(f"{command} {message}\r\n".encode())

    def send_oauth_token_to_server(self, oauth_token : str):
        self.send_command_to_server("PASS", oauth_token)

    def send_nick_to_server(self, nickname : str):
        self.send_command_to_server("NICK", nickname)

    def join(self, channel_name : str):
        self.send_command_to_server("JOIN", channel_name)

    def get_data_from_irc_server_response(self):
        return self.irc.recv(Client.BUFFER_SIZE)

    def send_pong_to_server(self):
        self.send_command_to_server("PONG", ":tmi.twitch.tv")
