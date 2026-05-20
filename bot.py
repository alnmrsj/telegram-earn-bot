from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8955934439:AAE7vz78vI6F5F3YYttiwNpIc4QmlsuUuTQ"
users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        users[user_id] = 0

    text = """
🎉 أهلاً بك في بوت الربح

📌 الأوامر:
/balance - رصيدك
/tasks - المهام
/refer - رابط الإحالة
/withdraw - سحب
"""

    await update.message.reply_text(text)

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = users.get(user_id, 0)

    await update.message.reply_text(f"💰 رصيدك: {balance} نقطة")

async def tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 المهام:\n"
        "1- اشترك في القناة وارسل تم\n"
        "🎁 المكافأة: 10 نقاط"
    )

async def refer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot_username = "Catcat4x4bot"

    link = f"https://t.me/{bot_username}?start={user_id}"

    await update.message.reply_text(
        f"👥 رابط الإحالة:\n{link}"
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💸 الحد الأدنى للسحب: 1000 نقطة"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("tasks", tasks))
app.add_handler(CommandHandler("refer", refer))
app.add_handler(CommandHandler("withdraw", withdraw))

print("Bot Running...")

app.run_polling()
