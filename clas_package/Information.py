import logging
from telegram import Update
from datetime import datetime, timedelta
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder
from dotenv import load_dotenv
import os
import re

class InformationScore:
    def __init__(self, operation, name=None):
        self.name = name
        self.operation = operation

        self.__cat_deposit = "deposit"
        self.__cat_salary = "salary"
        self.__cat_withdraw = "withdraw"
        self.__cat_write_transfer = "write_transfer"

    def categori(self):
        return f"{self.__cat_deposit}\n" \
               f"{self.__cat_withdraw}\n" \
               f"{self.__cat_write_transfer}" \
               f"{self.__cat_deposit}"

    def read_all(self):
        with open("base.txt", "r") as open_base:
            return open_base.read()

    def month(self):
        with open("base.txt", "r") as open_base:
            time_now = datetime.now()
            time_now1 = time_now.date()
            open_base.seek(0)
            for i in open_base.read().split(",\n"):
                if i:
                    search = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", i)
                    if search:
                        time_searhc = (datetime.strptime(search[0], "%Y-%m-%d %H:%M")).date()
                        if search and time_now1 - time_searhc <= timedelta(days=30):
                            yield i
                    else:
                        break

    def week(self):
        with open("base.txt", "r") as open_base:
            time_now = datetime.now()
            time_now1 = time_now.date()
            open_base.seek(0)
            for i in open_base.read().split(",\n"):
                if i:
                    search = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", i)
                    if search:
                        time_searhc = (datetime.strptime(search[0], "%Y-%m-%d %H:%M")).date()
                        if search and time_now1 - time_searhc <= timedelta(days=7):

                            yield i
                    else:
                        break


class Statistics(InformationScore):

    def stat_moth(self):
        for i in super().week():
            return i






