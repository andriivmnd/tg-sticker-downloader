
# Telegram Sticker Downloader

This script allows you to download stickers from Telegram by sending them to a bot, which then converts them into regular files for printing. The bot helps automate the process of creating stickers from Telegram stickers by preparing them for printing on paper.

## About the Project

This Telegram bot was originally created as a solution for my friends who opened an anime store and needed to create a large number of stickers from Telegram stickers. The manual process of sending stickers, downloading them, and then editing for printing was time-consuming. To simplify this, I wrote a small script that automates these tasks. Now, you just need to send the stickers you want to print to the bot, and it will automatically prepare them for printing.

## Installation

To get started with the bot, follow these steps:

1. Download this repository to your device.
2. Create a `config.py` file in the root directory:

```python
# config.py
TOKEN = ""  # Your Telegram bot token
```

3. Make sure you have Python installed. If not, download and install it from the official [Python website](https://www.python.org/).

## Running the Bot

To start the bot, follow these steps:

1. Run `start.bat` to create a virtual environment and start the bot:
   - This script will automatically install all necessary dependencies and activate the bot.
2. Open Telegram and start a chat with your bot.

## Usage

1. Send the stickers you want to download and print to the bot in a chat.
2. After sending the stickers, send the `/img` command to the bot.
3. Check the `done` directory in the root of the project. All your stickers will be there, ready for printing.

## Notes

- **Bot Token**: You can obtain a token for your bot by creating one through [BotFather](https://t.me/botfather) on Telegram.
- **`done` Folder**: This folder is automatically created after running the `/img` command and contains all processed images.
- **Future Commands**: More functionality for working with images is planned for future updates.

## Conclusion

This bot was developed to simplify and automate the process of creating stickers from Telegram stickers. I hope it proves useful for your business or personal use. If you have any suggestions for improvement or questions, feel free to contact me.
