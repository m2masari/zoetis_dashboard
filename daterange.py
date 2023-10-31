import datetime


class daterange:
    def __init__(self):
        self.start_date = datetime.date(2023, 7, 1)
        self.end_date = datetime.date(2023, 9, 30)
        # self.end_date = datetime.date.today()

    def date_range(self, start_date):
        last_day_of_month = datetime.date(self.start_date.year, self.start_date.month, 1) + datetime.timedelta(days=32)
        return [{"startDate": self.start_date.strftime("%Y-%m-%d"),
                 "endDate": (last_day_of_month - datetime.timedelta(days=last_day_of_month.day)).strftime("%Y-%m-%d")}]

    def datelist(self):
        date_list = []
        while self.start_date < self.end_date:
            date_list.append(self.date_range(self.start_date))
            last_day_of_month = datetime.date(self.start_date.year, self.start_date.month, 1) + datetime.timedelta(
                days=32)
            end_date_of_month = last_day_of_month - datetime.timedelta(days=last_day_of_month.day)
            self.start_date = end_date_of_month + datetime.timedelta(days=1)
        return date_list
