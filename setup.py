from setuptools import setup

long_description = None
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="tChat",
    description="A Twitch chat UI for your terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="Hícaro",
    author_email="hdanrlley1@gmail.com",
    license="MIT License",
    url="https://github.com/HicaroD/tChat",
    packages=["tChat"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        "console_scripts": [
            "tChat = tChat.main:_main",
        ]
    },
    python_requires=">=3.6",
)

