import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
API_URL ="http://localhost:8000/api/random-phrase/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Use /get_random_phrase to get a random phrase.")


async def get_random_phrase(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        message = data.get("text", "No phrase found")
    except requests.exceptions.RequestException as e:
        message = f"Error: {e}"
    await update.message.reply_text(message)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_random_phrase", get_random_phrase))

    application.run_polling()


if __name__ == "__main__":
    main()
