from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv
from flask import Flask
import threading
import os

# Load environment variables
load_dotenv()
Token = os.getenv("BOT_TOKEN")

# Flask server for keep-alive
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return 'Bot is running!'

@web_app.route('/healthz')
def health():
    return 'OK'

# Telegram bot handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Hello", callback_data="say_hello")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below test 👇", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "say_hello":
        await query.message.reply_text("👋 Hello clicked!")

# Start Flask in a background thread
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    web_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Start web server
    threading.Thread(target=run_flask).start()

    # Start Telegram bot
    app = ApplicationBuilder().token(Token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Telegram Bot is running...")
    app.run_polling()
