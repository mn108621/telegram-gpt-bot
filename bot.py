Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from openai import OpenAI
... from telegram import Update
... from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
... import os
...
... client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
...
... async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
...     response = client.responses.create(
...         model="gpt-5",
...         input=update.message.text
...     )
...
...     await update.message.reply_text(response.output_text)
...
... app = ApplicationBuilder().token(
...     os.getenv("TELEGRAM_TOKEN")
... ).build()
...
... app.add_handler(
...     MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
... )
...
... app.run_polling()
