import logging
from telegram import Update
from datetime import datetime, timedelta
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder
from dotenv import load_dotenv
import os
import re
from clas_package.Information import InformationScore, Statistics
from clas_package.Counting import Counter


async def start(update: Update, context: CallbackContext) -> None:

    await update.message.reply_text("Start to work\n"
                                    "1:/deposit\n"
                                    "1:/salary\n"
                                    "2:/withdraw\n"
                                    "3:/write_transfer\n"
                                    "5:/available_categories\n"
                                    "4:/week_transfer\n"
                                    "5:/month_transfer\n"
                                    "6:/write_transfer\n"
                                    "7:/all_transfer\n"
                                    "8:/remove\n"
                                    "5:/week_transfer\n"
                                    "5:/statistics_moth\n"
                                    )





async def write_transfer(update: Update, context: CallbackContext) -> None:
    contx = "".join(context.args)
    try:
        contx = int(contx)

    except ValueError:
        await update.message.reply_text(f"❌{contx}is not a number")
    else:
        upd = update.message.text.split()[0].strip("/")
        dep = Counter(upd, contx)
        await update.message.reply_text(dep.take())




async def withdraw(update: Update, context: CallbackContext) -> None:
    contx = "".join(context.args)
    try:
        contx = int(contx)

    except ValueError:
        await update.message.reply_text(f"❌{contx}is not a number")
    else:
        upd = update.message.text.split()[0].strip("/")
        dep = Counter(upd, contx)
        await update.message.reply_text(dep.take())


async def deposit(update: Update, context: CallbackContext) -> None:
    contx = "".join(context.args)
    try:
        contx = int(contx)
    except ValueError:
        await update.message.reply_text(f"❌{contx}is not a number")
    else:
        upd = update.message.text.split()[0].strip("/")
        dep = Counter(upd, contx)
        await update.message.reply_text(dep.add())

async def salary(update: Update, context: CallbackContext) -> None:
    contx = "".join(context.args)
    try:
        contx = int(contx)
    except ValueError:
        await update.message.reply_text(f"❌{contx}is not a number")
    else:
        upd = update.message.text.split()[0].strip("/")
        dep = Counter(upd, contx)
        await update.message.reply_text(dep.add())



async def available_categories(update:Update, context: CallbackContext):
    contx = " ".join(context.args).strip(",")
    upd = update.message.text.split("/")[0].strip("/")
    dep = InformationScore(upd, contx)
    await update.message.reply_text(dep.categori())
async def remove(update: Update, context: CallbackContext):
    contx = " ".join(context.args).strip(",")
    upd = update.message.text.split("/")[0].strip("/")
    dep = Counter(upd, contx)
    match contx.split(" ")[-2]:
        case "deposit":
            await update.message.reply_text(dep.delete_add())
        case "salary":
            await update.message.reply_text(dep.delete_add())
        case "withdraw":
            await update.message.reply_text(dep.delete_take())
        case "write_transfer":
            await update.message.reply_text(dep.delete_take())










async def all_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd, cont)
    await update.message.reply_text(inf.read_all())


async def month_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd)
    for i in inf.month():
        await update.message.reply_text(i, disable_notification=True)


async def week_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd)
    for i in inf.week():
        await update.message.reply_text(i, disable_notification=True)

async def statistics_moth(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = Statistics(upd)
    await update.message.reply_text(inf.stat_moth(), disable_notification=True)

load_dotenv()

key = os.environ.get("TOKEN_BOT")


def run():
    app = ApplicationBuilder().token(key).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("salary", deposit))
    app.add_handler(CommandHandler("withdraw", withdraw))
    app.add_handler(CommandHandler("remove", remove))

    app.add_handler(CommandHandler("available_categories", available_categories))
    app.add_handler(CommandHandler("write_transfer", write_transfer))
    app.add_handler(CommandHandler("all_transfer", all_transfer))
    app.add_handler(CommandHandler("month_transfer", month_transfer))
    app.add_handler(CommandHandler("week_transfer", week_transfer))
    app.add_handler(CommandHandler("statistics_moth", statistics_moth))

    app.run_polling()


# class FinAccount:
#     def __init__(self):


if __name__ == "__main__":
    run()
