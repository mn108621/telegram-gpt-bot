from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = client.responses.create(
            model="gpt-5",
            input=update.message.text
        )

        await update.message.reply_text(response.output_text)

    except Exception as e:
        await update.message.reply_text(f"錯誤：{e}")

app = ApplicationBuilder().token(
    os.getenv("TELEGRAM_TOKEN")
).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("Bot 已啟動")
app.run_polling()
