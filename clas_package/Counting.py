from datetime import datetime


class Counter:
    def __init__(self, operation, summ):
        self.summ = summ
        self.operation = operation
        self.score = None

        self.cat_deposit = "deposit"
        self.cat_salary = "salary"
        self.cat_withdraw = "withdraw"
        self.cat_write_transfer = "write_transfer"

    def ident(self):
        match self.summ[0]:
            case self.cat_deposit:
                return self.adds()

            case self.cat_salary:
                return self.adds()

            case self.cat_withdraw:
                return self.take()

            case self.cat_write_transfer:
                return self.take()

            case _:
                return "Unknown category"
    def adds(self):
        or_number()
        with open("base.txt", "a+") as open_base:
            time = datetime.now()
            format_time = time.strftime("%Y-%m-%d %H:%M")
            data_time = f"{format_time} {self.summ[0]} {self.summ[1]}"
            open_base.write(str(data_time) + ",\n")
        with open("score.txt", "r+") as open_score:
            sconre = int(open_score.read()) + int(self.summ[1])
            open_score.seek(0)
            open_score.write(str(sconre))
        return "✅ The operation was successfully performed!"

    def take(self):
        with open("score.txt", "r+") as open_scorr:
            red_scor = int(open_scorr.read())
            print(open_scorr.read())
            open_scorr.seek(0)
            if red_scor < int(self.summ[1]):

                return "❌There are insufficient funds in the account"
            else:
                if red_scor == int(self.summ[1]):
                    open_scorr.seek(0)
                    open_scorr.write('0')
                    open_scorr.truncate()
                else:
                    score = red_scor - int(self.summ[1])
                    open_scorr.seek(0)
                    open_scorr.write(str(score))
                    open_scorr.truncate()

                with open("base.txt", "a+") as open_base:
                    time = datetime.now()
                    format_time = time.strftime("%Y-%m-%d %H:%M")
                    data_time = f"{format_time} {self.summ[0]} {self.summ[1]}"
                    open_base.write(str(data_time) + ",\n")



        return "✅ The operation was successfully performed!"

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

        return "✅ Payment deleted"

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

        return "✅ Payment deleted"






def or_number() -> None:
    with open("score.txt", "r+") as open_score:
        try:
            int(open_score.readline())
        except ValueError:
            open_score.seek(0)
            open_score.truncate()
            open_score.write('0')

