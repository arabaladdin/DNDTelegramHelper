from telegram.ext import Updater, CommandHandler
from dbhelper import DBHelper
import json

# init the database helper
db = DBHelper()

TOKEN = '892132794:AAFkaq95dewuN-mLfTFYWSzWwfhalNz-ez4'
updater = Updater(TOKEN, use_context=True)


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name)
    )

#api message. text.
#remove /add
#just had an idea: when clicking inventory,
#a new temporary keyboard is passed that lists all the items


def add(update, context):
    text = update.message.text
    chat = update.message.from_user.id

    print(text, chat)
    # update.message.reply_text(
    #     'Hello {} and {}'.format(text, chat)
    # )
    db.add_item(text, chat)
    # items = db.get_items(chat)
    # # it's looping through each individual character
    # # first just remove /add
    # # python remove words beginning with / and then end with space

    # # message = "\n".join(items)


def list_item(update, context):
    #I know it's executing properly,
    #getting the database to add items to it is the real issue
    #how do I check?
    #is the database even really connected?
    print('work')

    user_id = update.message.from_user.id
    print(user_id)
    # print(user_id)
    # this is where it's getting stuck
    #trying to fetch the items but something is wrong.
    #are they not commited to the db or am I using the wrong commands?
    items = db.get_items()
    print(items)
    # items = db.get_items(id)
    # message = "\n".join(items)
    update.message.reply_text(
        'Hello {}'.format('items')
    )
    # send_message(message, chat)


def inventory(update, context):
    # get everything from db
    # chat = update.message.from_user.id
    # items = db.get_items(chat)
    # update.message.reply_text(
    #     '{}'.format(items)
    # )
    # print(items)
    pass


def stats(update, context):
    pass


def build_keyboard():
    keyboard = ['/inventory', '/stats']
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": False}
    return json.dumps(reply_markup)

#keyboard isn't showing up like it's supposed to
# build_keyboard()


# add keyboard
def main():
    db.setup()
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('add', add))
    updater.dispatcher.add_handler(CommandHandler('list', list_item))

    # where do we run build keyboard so it persists?
    # db.get_items()
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()