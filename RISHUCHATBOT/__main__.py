import sys
import asyncio
import importlib
from flask import Flask
import threading
import config
from RISHUCHATBOT import LOGGER, RISHUCHATBOT
from RISHUCHATBOT.modules import ALL_MODULES
from pyrogram import idle
from pyrogram.types import BotCommand

async def anony_boot():
    try:
        await RISHUCHATBOT.start()
        try:
            await RISHUCHATBOT.send_message(int(config.OWNER_ID), f"**{RISHUCHATBOT.mention} Is started✅**")
        except Exception as ex:
            LOGGER.info(f"@{RISHUCHATBOT.username} Started, please start the bot from owner id.")
    
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("RISHUCHATBOT.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    try:
        await RISHUCHATBOT.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("ping", "Check if the bot is alive or dead"),
                BotCommand("lang", "Select bot reply language"),
                BotCommand("chatlang", "Get current using lang for chat"),
                BotCommand("resetlang", "Reset to default bot reply lang"),
                BotCommand("id", "Get users user_id"),
                BotCommand("stats", "Check bot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
                BotCommand("chatbot", "Enable or disable chatbot"),
                BotCommand("status", "Check chatbot enable or disable in chat"),
                BotCommand("shayri", "Get random shayri for love"),
                BotCommand("ask", "Ask anything from chatgpt"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    LOGGER.info(f"@{RISHUCHATBOT.username} Started.")
    
    await idle()


app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping RISHUCHATBOT Bot...")
