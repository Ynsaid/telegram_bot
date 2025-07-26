from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv
import os 



load_dotenv()

Token = os.getenv("BOT_TOKEN")
# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Hello", callback_data="say_hello")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below 👇", reply_markup=reply_markup)

# Handle button click
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "say_hello":
        await query.message.reply_text("👋 Hello clicked!")

# Main bot setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(Token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot is running...")
    app.run_polling()
