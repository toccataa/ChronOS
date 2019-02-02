from datetime import datetime, timedelta

import Workday
from Resources import CommonMethods


class TimeKeeper:
    def __init__(self):
        self.__timeKeeper = {}

    def add_workday(self, workday: Workday):
        self.__timeKeeper[workday.get_day_date()] = workday

    def get_all_workdays(self) -> dict:
        return self.__timeKeeper

    def get_workday_of_day_date(self, day_date: datetime) -> Workday:
        return self.__timeKeeper[day_date]

    def get_time_log(self):
        return self.__timeKeeper

    def calculate_total_time_balance(self) -> (timedelta, bool):
        positive_balance = timedelta(seconds=0)
        negative_balance = timedelta(seconds=0)
        is_total_time_balance_negative = False

        for day_date, workday in self.__timeKeeper.items():
            time_balance_for_current_day, negativity_flag = workday.get_time_balance_with_negativity_flag()
            if negativity_flag:
                negative_balance += time_balance_for_current_day
            else:
                positive_balance += time_balance_for_current_day

        if positive_balance >= negative_balance:
            total_time_balance = positive_balance - negative_balance
        else:
            total_time_balance = negative_balance - positive_balance
            is_total_time_balance_negative = True

        return total_time_balance, is_total_time_balance_negative

    def get_total_time_balance_in_printable_format(self) -> str:
        total_time_balance, is_total_time_balance_negative = self.calculate_total_time_balance()
        interpreted_total_time_balance = CommonMethods.get_interpreted_time_balance(total_time_balance,
                                                                                    is_total_time_balance_negative)
        return interpreted_total_time_balance
