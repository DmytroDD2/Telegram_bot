from datetime import datetime, timedelta
import re


class InformationScore:
    def __init__(self, operation, name=None):
        self.name = name
        self.operation = operation

        self.cat_deposit = "deposit"
        self.cat_salary = "salary"
        self.cat_withdraw = "withdraw"
        self.cat_write_transfer = "write_transfer"

    def balance(self):
        with open("score.txt", "r") as open_score:
            return float(open_score.read())

    def categori(self):
        return f"{self.cat_deposit}\n" \
               f"{self.cat_salary}\n" \
               f"{self.cat_withdraw}\n" \
               f"{self.cat_write_transfer}" \


    def read_all(self):
        with open("base.txt", "r") as open_base:
            return open_base.read()

    def hystory(self, what_time):
        with open("base.txt", "r") as open_base:
            time_now = datetime.now()
            time_now1 = time_now.date()
            open_base.seek(0)
            for i in open_base.read().split(",\n"):
                if i:
                    search = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", i)
                    if search:
                        time_searhc = (datetime.strptime(search[0], "%Y-%m-%d %H:%M")).date()
                        if search and time_now1 - time_searhc <= timedelta(days=what_time):
                            yield i
                    else:
                        break

    def year(self):
        return self.hystory(365)

    def month(self):
        return self.hystory(30)

    def week(self):
        return self.hystory(7)

    def day(self):
        return self.hystory(1)


class Statistics(InformationScore):
    def stat_all(self, func):
        deposit = 0
        salary = 0
        withdraw = 0
        write_transfer = 0
        try:
            iter(func())
        except TypeError:
            return "Not trasaction"

        for i in func():
            money = int(i.split()[3])
            match i.split()[2]:
                case self.cat_deposit:
                    deposit += money

                case self.cat_salary:
                    salary += money
                case self.cat_withdraw:
                    withdraw += money
                case self.cat_write_transfer:
                    write_transfer += money


        proc_deposit = deposit / (salary + deposit) * 100 if deposit != 0 else 0
        proc_salary = salary / (salary + deposit) * 100 if salary != 0 else 0
        proc_withdraw = withdraw / (withdraw + write_transfer) * 100 if withdraw != 0 else 0
        proc_write_transfer = write_transfer / (withdraw + write_transfer) * 100 if write_transfer != 0 else 0
        return f'deposit: {round(proc_deposit, 2)} %\n' \
               f'salary: {round(proc_salary, 2)} %\n' \
               f'withdraw: {round(proc_withdraw, 2)}%\n' \
               f'write_transfer: {round(proc_write_transfer, 2)}%'

    def stat_year(self):
        return self.stat_all(self.year)

    def stat_moth(self):
        return self.stat_all(self.month)

    def stat_week(self):
        return self.stat_all(self.week)

    def stat_day(self):
        return self.stat_all(self.day())







