from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ sᴇᴛᴛɪɴɢs ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ ᴄᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ✯", url=f"https://t.me/rapstar_x3_kitty"),
            InlineKeyboardButton(
                text="✯ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ✯", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/DJ_x_d"):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✯ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ✯", url=f"https://t.me/rapstar_x3_kitty")

            InlineKeyboardButton(
                text="✯ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ✯", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥀 ᴍᴀɪɴᴛᴀɪɴᴇʀ 🥀", url=f"https://t.me/rapstar_on_fire"
                )
        ],
     ]
    return buttons
