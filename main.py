import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Use /menu to see what I can do.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
📌 *Main Menu*
/remind - Set a reminder
/timer - Start timer
/stopwatch - Start stopwatch
/quiz - Start daily quiz
/news - Latest current affairs
/qr - Generate QR
/convert - File converter
/leaderboard - Show scores
"""
    await update.message.reply_markdown(text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.run_polling()

if __name__ == "__main__":
    main()
