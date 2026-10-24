from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import os
TOKEN = os.environ.get("TELEGRAM_TOKEN")

ADMIN_ID = 8969999721


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["📢 Complaints"],
        ["❓ Questions"],
        ["📝 Requests"],
        ["📧 Contact Me"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🎓 Welcome to the University Communication Bot!\n\nChoose an option:",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user = update.effective_user

    if text == "📢 Complaints":
        await update.message.reply_text(
            "Please write your complaint and send it."
        )

    elif text == "❓ Questions":
        await update.message.reply_text(
            "Please write your question and send it."
        )

    elif text == "📝 Requests":
        await update.message.reply_text(
            "Please write your request and send it."
        )

    elif text == "📧 Contact Me":
        await update.message.reply_text(
            "📧 Contact Email:\n\nsnvl1contact@gmail.com"
        )

    else:

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"""
📨 New Submission

Name: {user.first_name}
Username: @{user.username}

Message:
{text}
"""
        )

        await update.message.reply_text(
            "✅ Your message has been sent successfully."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

print("Bot is running...")

app.run_polling()
