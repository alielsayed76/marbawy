import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("mongodb+srv://lucifer:ASShaw96@lucifer.vuows.mongodb.net/lucifer?retryWrites=true&w=majorityL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
DEV_NAME = getenv("DEV_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = ("BAR_ARBAWY")
UPDATES_CHANNEL = ("SOURCE_ARBAWY305")
SUDO_USERS = list(map(int, getenv(["SUDO_USERS", "5410906493"]).split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/91dd9880d8b9d74774487.jpg")
DURATION_LIMIT = int(("3900"))
UPSTREAM_REPO = ("https://github.com/alielsayed76/marbawy.git")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/68d5c1ba31d73ced616d1.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/68d5c1ba31d73ced616d1.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/68d5c1ba31d73ced616d1.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/68d5c1ba31d73ced616d1.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/68d5c1ba31d73ced616d1.jpg")
