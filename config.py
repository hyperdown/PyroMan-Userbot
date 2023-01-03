# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("ba64ca38a4cbdc0cd7bde7bd040cd81d")
API_ID = int(getenv("2277665", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001388720590]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("-1001388720590") or 0)
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "Lunatic0de")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "SharingUserbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv("REPO_URL", "https://github.com/mrismanaziz/PyroMan-Userbot")
STRING_SESSION1 = getenv("1BVtsOKIBuwjPe57zS0BvJcaMmTAdXqjGYt4u9b6Kt0fSDnrn2Ih29mkTJtuxAgcUPhaqoyts75RTGWpJxACteHufAdAZHh7vx7xK-lZHCxJTdeMIYmzWdUKUyvYragDDXJB9Ddngius3gw-ZHxhd_AkqVevPCt0vvQF6hYaJSdww9D3TXl8NrYeH6QYlCmKzIfZPrQGTgZ1etMpCKwdHpB_yq2s7rRbzCyHF2uMn5wUTmK5dS4zLhy_6RX_iLWWcFItLns_BnlDhiMfvcWkIa9nQ1Vvy5_bZylC7PC6ONJflP37qpJD6FAVr5fib4G5I0ITwmdyEusUdSWx2Bp4D7ncNn6PYhTY=", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
