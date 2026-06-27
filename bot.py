import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# تخزين بسيط (لاحقًا نحوله لقاعدة بيانات)
family = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا 👋 في بوت شجرة العائلة 🌳")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = " ".join(context.args)
    if not name:
        await update.message.reply_text("اكتب الاسم بعد الأمر /add")
        return

    family[name] = {"father": None}
    await update.message.reply_text(f"تم إضافة: {name}")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = " ".join(context.args)
    if name in family:
        father = family[name]["father"]
        await update.message.reply_text(f"الاسم: {name}\nالأب: {father}")
    else:
        await update.message.reply_text("غير موجود")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("search", search))

    app.run_polling()

if __name__ == "__main__":
    main()
