from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


# app = ApplicationBuilder().token("5738163783:AAFU7gKJ4w3eb3_W8v7_WT03jUCVbtLsQYk").build()
app = ApplicationBuilder().token("5713892468:AAGR6Dhsmo6q3DToNEpFYXCePd5UTXx1iBw").build()
print("start")
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))

app.run_polling()
