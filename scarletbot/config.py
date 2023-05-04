# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/scarletbot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "14050586" # integer value, dont use ""
    API_HASH = "42a60d9c657b106370c79bb0a8ac560c"
    TOKEN = os.environ.get("TOKEN")  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "5475511278" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "projectstark"
    SUPPORT_CHAT = "scarletsupportchat"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001871477087
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001871477087
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI = "mongodb+srv://Cutie:cutie1@cluster0.dctlhwo.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = "postgresql://clh9o9i3h001fajqkakm5d9v8:ijEQ9gfEcWAkPXdGtPgcBBCG@104.248.139.76:9001/clh9o9i3j001hajqkghwv85b5"
    START_IMG = "https://te.legra.ph/file/6c2d411c893e5d483c4bd.jpg"
    TEMP_DOWNLOAD_DIRECTORY = "./downloads/"
    
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "ibGjchtz3djmcaIDiG3qoLX8KE0Npo1ChFiH7QGpjoQY1uB7BGOPJ~DOT07c0VSH"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = []
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [1412909688]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = []
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = []
    WOLVES = []
    #DONATION_LINK = none # EG, paypal
    #CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "7AT86JXWTFKSFSCQ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    ALLOW_CHATS = []
    #SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
