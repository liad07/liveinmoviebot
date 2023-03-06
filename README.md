# live in movie bot

This is a Telegram bot built with Python to perform various actions. The bot is designed to help users find movies to watch and receive messages from the admin.

## Prerequisites
Python 3.6+

python-telegram-bot 13.7 library
## Setup

Clone the repository and navigate to the project directory:

```bash

git clone https://github.com/liad07/liveinmoviebot.git
cd liveinmoviebot

```
Install the python-telegram-bot library:

```bash
pip install python-telegram-bot==13.7
```

Obtain a Telegram bot API key from the BotFather on Telegram.

Replace TOKEN variable with your API key in the telegram_bot.py file:

``` python
TOKEN = "<your API key>"
```

Replace CHANNEL_ID variable with the ID of the channel you want to search in the telegram_bot.py file:

``` python

CHANNEL_ID = "<channel ID>"
```


Run the bot by executing the following command:

```bash
python telegram_bot.py
```
## Usage

Once the bot is running, you can use the following commands:

/start: Start the bot and display available actions.

/find <name of movie>: Find a movie by name and receive a URL/file to watch it.

/send <message>: Send a message to all users (admin only).

/set: Set options for adding a new movie.

The bot will save the user IDs of anyone who sends a message to it in a file called user_ids.txt. This can be used to send messages to all users.

## Contributions

Contributions to this project are welcome. Please feel free to submit a pull request or open an issue if you have any questions or suggestions.
