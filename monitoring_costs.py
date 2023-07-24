import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder
from clas_package.Information import InformationScore, Statistics
from clas_package.Counting import Counter

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def start(update: Update, context: CallbackContext) -> None:
    logging.info("Command start was triggered!")
    await update.message.reply_text("Start to work\n"
                                    "===========================================\n"
                                    "Find out the account balance: /account_balance\n"
                                    "Add a transaction: /transaction  <category amount>\n"
                                    "Delete payment: /remove  <data category amount>\n"
                                    "View available payment categories: /available_categories\n"
                                    "--------------------------------------------\n"
                                    "Transactions during the day: /day_transfer\n"
                                    "Transactions during the week: /week_transfer\n"
                                    "Transactions during the month: /month_transfer\n"
                                    "Transaction during the year: /year_transfer\n"
                                    "Transaction for all time: /all_transfer\n"
                                    "--------------------------------------------\n"
                                    "Statistics for the day: /statistics_day\n"
                                    "Statistics for the month: /statistics_moth\n"
                                    "Statistics for the week: /statistics_week\n"
                                    "Statistics for the year: /statistics_year\n"
                                    )


async def account_balance(update: Update, context: CallbackContext) -> None:
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd, cont)
    await update.message.reply_text(inf.balance())

async def transaction(update: Update, context: CallbackContext) -> None:
    contx = " ".join(context.args).split()
    print(contx)
    try:
        int(contx[1])

    except ValueError:
        await update.message.reply_text(f"❌{contx}is not a number")
    else:
        upd = update.message.text.split()[0].strip("/")
        dep = Counter(upd, contx)
        await update.message.reply_text(dep.ident())


async def available_categories(update:Update, context: CallbackContext):
    contx = " ".join(context.args).strip(",")
    upd = update.message.text.split("/")[0].strip("/")
    dep = InformationScore(upd, contx)
    await update.message.reply_text(dep.categori())


async def remove(update: Update, context: CallbackContext):
    contx = " ".join(context.args).strip(",")
    upd = update.message.text.split("/")[0].strip("/")
    dep = Counter(upd, contx)
    if len(contx.split(" ")) == 4:
        match contx.split(" ")[-2]:
            case "deposit":
                await update.message.reply_text(dep.delete_add())
            case "salary":
                await update.message.reply_text(dep.delete_add())
            case "withdraw":
                await update.message.reply_text(dep.delete_take())
            case "write_transfer":
                await update.message.reply_text(dep.delete_take())
            case _:
                await update.message.reply_text("❌Payment not found")
    else:
        await update.message.reply_text("❌Payment not found")


async def all_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd, cont)
    await update.message.reply_text(inf.read_all())


async def year_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    inf = InformationScore(upd)
    for i in inf.year():
        await update.message.reply_text(i, disable_notification=True)


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


async def day_transfer(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = InformationScore(upd)
    for i in inf.day():
        await update.message.reply_text(i, disable_notification=True)


async def statistics_year(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = Statistics(upd)
    await update.message.reply_text(inf.stat_year(), disable_notification=True)


async def statistics_moth(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = Statistics(upd)
    await update.message.reply_text(inf.stat_moth(), disable_notification=True)


async def statistics_week(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = Statistics(upd)
    await update.message.reply_text(inf.stat_week(), disable_notification=True)

async def statistics_day(update: Update, context: CallbackContext):
    upd = update.message.text.split()[0].strip("/")
    cont = context.args
    inf = Statistics(upd)
    await update.message.reply_text(inf.stat_day(), disable_notification=True)


key = ("TOKEN_BOT")


def run():
    app = ApplicationBuilder().token(key).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("account_balance", account_balance))
    app.add_handler(CommandHandler("transaction", transaction))
    app.add_handler(CommandHandler("available_categories", available_categories))
    app.add_handler(CommandHandler("remove", remove))

    app.add_handler(CommandHandler("all_transfer", all_transfer))
    app.add_handler(CommandHandler("day_transfer", day_transfer))
    app.add_handler(CommandHandler("week_transfer", week_transfer))
    app.add_handler(CommandHandler("month_transfer", month_transfer))
    app.add_handler(CommandHandler("year_transfer", year_transfer))

    app.add_handler(CommandHandler("statistics_year", statistics_year))
    app.add_handler(CommandHandler("statistics_moth", statistics_moth))
    app.add_handler(CommandHandler("statistics_week", statistics_week))
    app.add_handler(CommandHandler("statistics_day", statistics_day))

    app.run_polling()


if __name__ == "__main__":
    run()
