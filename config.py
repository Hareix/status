#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "6"))
API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7364144228:AAFm8rsf2CkyM0B8464HhQarb6dTu7G7ZnQ")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "5545068262").split())
)  # Input type must be interger

# ADMIN USERS
ADMIN_USER = list(
    map(int, getenv("ADMIN_USER", "5545068262").split())
)  # Input type must be interger

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to Cheems Support Bot, Ask Anything regarding our bots here.",
)
