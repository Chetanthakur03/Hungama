import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23678164"))
API_HASH = getenv("API_HASH", "69d69eb8a4f8619d6fc9ddd80243c5f8")

BOT_TOKEN = getenv("BOT_TOKEN", "6086035101:AAG3ttqGgKZcHJckDdVGbkqIwl2jNbyR9lI")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Alok:alok@cluster0.fmaldbv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001812541943"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Alpha Robot")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5161032951").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/pirokid")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_Alpha_X_help")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alpha_X_supports")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "59920"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "14180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5984fde29e024b308d8defa276e4a601")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "561c1883f2974ff8b03087343e4b0ff8")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCXmIlZLtT-jphgg-jj2OGroceGlkjDMubS_vMVTOdHtwLTvrbJItsSIezGXZiymicrgGF5jR-du2wU8WkQvOBdThyz5bxughEdyfoJLsFeoetnff27mYw5PIn7pIJoIZfH1vzSqQFovGHnkp4oZuau3TLgiyyrASw_VFsl2QIsqkWWw6Al5McTJfv0mUgkFcLHUETK8oKNUVr9jx4d-KrvWkMMB41RY8UbROZTBHEIvPL3-7iMVZFSTA1sLK09gDO27cm5cJNrSxqNGfEFpoLNuULaIUe3kS6bzwYeYvfxUxVJv5yRqrPOUhjBeMVjhF4q4DZ8CiBQ6wFz3J6WGEFaAAAAAUv9mG0A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/95d40f0224268dbe7287f.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/73aee88ae407cfd6d6024.jpg"
