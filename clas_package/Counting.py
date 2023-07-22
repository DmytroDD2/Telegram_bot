import logging
from telegram import Update
from datetime import datetime, timedelta
from telegram.ext import CommandHandler, CallbackContext, ApplicationBuilder
from dotenv import load_dotenv
import os
import re
from functools import wraps


class Counter:
    def __init__(self, operation, summ):
        self.summ = summ
        self.operation = operation
        self.score = None



    def add(self):
        with open("base.txt", "a+") as open_base:
            time = datetime.now()
            format_time = time.strftime("%Y-%m-%d %H:%M")
            data_time = f"{format_time} {self.operation} {self.summ}"
            open_base.write(str(data_time) + ",\n")
        with open("score.txt", "r+") as open_score:
            sconre = int(open_score.read()) + self.summ
            open_score.seek(0)
            open_score.write(str(sconre))
        return "✅"

    def take(self):
        with open("base.txt", "a+") as open_base:
            time = datetime.now()
            format_time = time.strftime("%Y-%m-%d %H:%M")
            data_time = f"{format_time} {self.operation} {self.summ}"
            open_base.write(str(data_time) + ",\n")
        with open("score.txt", "r+") as open_scorr:
            red_scor = int(open_scorr.read())
            if red_scor < self.summ:
                return "❌There are insufficient funds in the account"
            else:
                score = red_scor - self.summ
                open_scorr.seek(0)
                open_scorr.write(str(score))
        return "✅"




    def delete_add(self):
        with open("base.txt", "r+") as open_base:
            open_base_work = open_base.readlines()
            open_base.seek(0)

            for i in open_base_work:
                if i:
                    if i.strip(",\n") != self.summ:
                        open_base.write(i)

                else:
                    break

            open_base.truncate()
            with open("score.txt", "r+") as open_score:
                sconre = int(open_score.read()) - int(self.summ.split(" ")[-1])
                open_score.seek(0)
                open_score.write(str(sconre))

        return "✅"

    def delete_take(self):
        with open("base.txt", "r+") as open_base:
            open_base_work = open_base.readlines()
            open_base.seek(0)

            for i in open_base_work:
                if i:
                    if i.strip(",\n") != self.summ:
                        open_base.write(i)

                else:
                    break

            open_base.truncate()
            with open("score.txt", "r+") as open_score:
                sconre = int(open_score.read()) + int(self.summ.split(" ")[-1])
                open_score.seek(0)
                open_score.write(str(sconre))

        return "✅"

