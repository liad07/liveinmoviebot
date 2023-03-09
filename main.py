from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import telegram

# בס"ד
# Replace with your API key
TOKEN = ""
bot = telegram.Bot(token=TOKEN)
# Replace with the ID of the channel you want to search in
CHANNEL_ID = "-1001500640863"
name = ""
chat = bot.get_chat('@liveinmoviebot')

# get the chat history
# messages = chat.get_history()

# extract the text content of each message
# text_messages = [message.text for message in messages if message.text is not None]

# print the text messages
# print(text_messages)#print(chat.id)
#
print("bot started")


def start(update, context):
    """Start command handler"""
    user_id = update.effective_user.id
    ret = " ברוכים הבאים לבוט של חיים בסרט\n" "הבוט מכיל מספר פעולות \n" "/find <name of movie> : give url/file to see the movie\n" "/send <messege> : send messege to all users (only admin)\n"
    # Load the list of saved user IDs from the text file
    with open('user_ids.txt', 'r') as f:
        user_ids = f.read().splitlines()

    # Check if the user ID is in the list of saved user IDs
    if str(user_id) not in user_ids:
        # Add the user ID to the list of saved user IDs
        ret = " ברוכים הבאים לבוט של חיים בסרט\n"
        "הבוט מכיל מספר פעולות \n"
        "/find <name of movie> : give url/file to see the movie\n"
        "/send <messege> : send messege to all users (only admin)\n"
        "join our channel: https://t.me/Live_in_movie\n"
        with open('user_ids.txt', 'a') as f:
            f.write(str(user_id) + '\n')
    update.message.reply_text(ret)


def find_group_id(update, context):
    group_id = update.message.chat_id
    update.message.reply_text(f"The ID of this group is {group_id}.")

    # todo:find file or text or link forwad the found text to the user


def isurl():
    with open('tempfile.txt', 'r') as f:
        x = f.read()
    with open('list.txt', 'a') as w:
        w.write("#" + x.split("\n")[0] + "\n" + x.split("\n")[1] + "\ntype:url" + "#" + "\n")


def isvideo():
    with open('tempfile.txt', 'r') as f:
        x = f.read()
    with open('list.txt', 'a') as w:
        w.write("#" + x.split("\n")[0] + "\n" + x.split("\n")[1] + "\ntype:video" + "#" + "\n")


def isfile():
    with open('tempfile.txt', 'r') as f:
        x = f.read()
    with open('list.txt', 'a') as w:
        w.write("#" + x.split("\n")[0] + "\n" + x.split("\n")[1] + "\ntype:file" + "#" + "\n")


def button_click(update, context):
    query = update.callback_query
    option = query.data
    query.answer()

    # Handle the selected option
    if option == 'm1':
        # Handle url option
        isurl()
        query.edit_message_text(text="select type url")
    elif option == 'm2':
        # Handle file option
        isfile()
        query.edit_message_text(text='You selected file')
    elif option == 'm3':
        # Handle video option
        isvideo()
        query.edit_message_text(text='You selected video')


def set(update, context):
    user = update.message.from_user
    # adminuser = "Live_in_the_movie"
    adminuser = "Live_in_the_movie"
    # Check if the user has a username
    if user.username is not None:
        # Check if the user's username matches the desired username
        if user.username == adminuser:
            message = update.message.text.replace("/set ", "")
            message.split("\n")

            menu_main = [[InlineKeyboardButton('url', callback_data='m1')],
                         [InlineKeyboardButton('file', callback_data='m2')],
                         [InlineKeyboardButton('video', callback_data='m3')]]
            reply_markup = InlineKeyboardMarkup(menu_main)
            update.message.reply_text('Choose the option:', reply_markup=reply_markup)
            name = message.split("\n")[1]
            try:
                url = message.split("\n")[2]
                result = context.bot.send_message(chat_id=CHANNEL_ID, text="check")
                message_id = result.message_id
                link = f'https://t.me/liveinmoviebot/{message_id - 3}'
            except:
                result = context.bot.send_message(chat_id=CHANNEL_ID, text="check")
                message_id = result.message_id
                link = f'https://t.me/liveinmoviebot/{message_id - 3}'
                url = link
            with open('tempfile.txt', 'w') as f:
                f.write(name + "\n" + url)
        else:
            update.message.reply_text(f"only admin can use this function")



# find on text file
# set on text file
def find(update, context):
    findtext = update.message.text.replace("/find ", "")
    isfound=False
    with open('list.txt', 'r', encoding='iso-8859-8') as f:
        text = f.read()


# split the text into a list of entries
    entries = text.split('#\n')

    # loop through each entry and extract the name, link, and type
    for entry in entries:
        if not entry.strip():
            continue  # skip empty entries
        data = entry.strip().split('\n')
        name = data[0].replace("#","")
        link = data[1]
        file_type = data[2].split(':')[1]
        x=name+"\n"+link+"\n"+file_type
        if findtext in name:
            context.bot.send_message(chat_id=update.message.chat_id, text=x)
            return

def send(update, context):
    # Get the input message from the user
    user = update.message.from_user
    # adminuser = "Live_in_the_movie"
    adminuser = "Live_in_the_movie"
    # Check if the user has a username
    if user.username is not None:
        # Check if the user's username matches the desired username
        if user.username == adminuser:
            message = update.message.text.replace("/send", "")
            print(message)

            # Open the file containing user IDs and read the contents
            with open('user_ids.txt', 'r') as f:
                user_ids = f.readlines()

            # Send a message to each user
            for user_id in user_ids:
                try:
                    # Remove newline character from the user ID
                    user_id = user_id.strip()

                    # Send a message to the user
                    context.bot.send_message(chat_id=user_id, text=message)

                    # Log success message
                    print(f"Message sent to user {user_id}.")

                except Exception as e:
                    # Log error message if message couldn't be sent
                    print(f"Error sending message to user {user_id}: {e}")
        else:
            update.message.reply_text(f"only admin can use this function")


# Create the updater and dispatcher
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Register the command handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("find", find))
dp.add_handler(CommandHandler("find1", find_group_id))
dp.add_handler(CommandHandler("send", send))
dp.add_handler(CommandHandler("set", set))
button_handler = CallbackQueryHandler(button_click)
dp.add_handler(button_handler)
# Start the bot
updater.start_polling()
updater.idle()
