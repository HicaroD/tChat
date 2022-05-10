from setuptools import setup

long_description = None
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="tChat",
    description="A Twitch chat UI for your terminal.",
    long_description=long_description,
    author="Hícaro",
    author_email="hdanrlley1@gmail.com",
    license="MIT License",
    url="http://pypi.python.org/pypi/tChat/",
    packages=["tChat"],
    entry_points = {
        "console_scripts": [
            "tChat = tChat.main:main",
        ]
    },
)

