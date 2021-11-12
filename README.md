# tChat
**WARNING: This project is a work in progress!**

<div align="center">
 <img src="./img/new_version.png">
 A terminal Twitch Chat written in Python
</div>

## Installation

1. Clone the repository
```bash
git clone https://github.com/HicaroD/tChat.git
```

2. Install all packages needed to run everything properly

You can use either pip3 or pip (it depends on the PIP version that you have installed in your machine)
```bash
cd tChat/ && pip3 install -r requirements.txt
```

## Usage
You can run the program by typing
```bash
python3 main.py -n <your nickname> -ch <channel name you want to join>
```
You can use -n for your Twitch username and -ch for the channel name you want to join! Remember to do that without "<>"

**IMPORTANT**: If it's the first you are using the program, you will need to insert a OAuth token to join the chat. Use this website to get your oauth token: [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/)

## License
[MIT](./LICENSE)
