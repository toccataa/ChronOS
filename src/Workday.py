from datetime import datetime, timedelta
from typing import Union

from Resources import Constants, CommonMethods


class Workday:
    def __init__(self):
        self.__day_times = Constants.get_const_day_times_dict()
        self.__is_time_balance_negative = False

    def is_lunch_total_calculable(self) -> bool:
        return self.__day_times["lunch_start"] is not None and self.__day_times["lunch_finish"] is not None

    def is_checked_in_total_calculable(self) -> bool:
        return self.__day_times["check_in"] is not None and self.__day_times["check_out"] is not None

    def is_net_work_time_calculable(self) -> bool:
        return self.__day_times["checked_in_total"] is not None and self.__day_times["lunch_total"] is not None

    def is_time_balance_calculable(self) -> bool:
        return self.__day_times["to_work_total"] is not None and self.__day_times["net_work_time"] is not None

    def normalize_lunch_time(self, lunch_time: timedelta):
        fifteen_minutes = timedelta(minutes=15)
        thirty_minutes = timedelta(minutes=30)
        if lunch_time < fifteen_minutes:
            lunch_time += thirty_minutes
        elif fifteen_minutes <= lunch_time <= thirty_minutes:
            lunch_time = thirty_minutes
        return lunch_time

    def calculate_lunch_total(self) -> None:
        if self.is_lunch_total_calculable():
            lunch_total = self.__day_times["lunch_finish"] - self.__day_times["lunch_start"]
            self.__day_times["lunch_total"] = lunch_total
            lunch_total = self.normalize_lunch_time(lunch_total)
            self.__day_times["lunch_normalized"] = lunch_total

    def calculate_checked_in_total(self) -> None:
        if self.is_checked_in_total_calculable():
            checked_in_total = self.__day_times["check_out"] - self.__day_times["check_in"]
            self.__day_times["checked_in_total"] = checked_in_total

    def calculate_net_work_time(self) -> None:
        if self.is_net_work_time_calculable():
            net_work_time = self.__day_times["checked_in_total"] - self.__day_times["lunch_normalized"]
            self.__day_times["net_work_time"] = net_work_time

    def calculate_time_balance(self) -> None:
        if self.is_time_balance_calculable():
            if self.__day_times["net_work_time"] >= self.__day_times["to_work_total"]:
                time_balance = self.__day_times["net_work_time"] - self.__day_times["to_work_total"]
                self.__is_time_balance_negative = False
                self.__day_times["time_balance"] = time_balance
            else:
                time_balance = self.__day_times["to_work_total"] - self.__day_times["net_work_time"]
                self.__is_time_balance_negative = True
                self.__day_times["time_balance"] = time_balance

    def calculate_times(self) -> None:
        self.calculate_lunch_total()
        self.calculate_checked_in_total()
        self.calculate_net_work_time()
        self.calculate_time_balance()

    def add_time(self, time_key: str, what_time: Union[datetime, timedelta]):
        if time_key in Constants.get_const_addable_time_keys():
            self.__day_times[time_key] = what_time

    def get_day_date(self) -> datetime:
        return self.__day_times["day_date"]

    def get_displayable_time(self, time_key: str) -> str:
        if time_key in self.__day_times:
            time_to_be_displayed = self.__day_times[time_key]
            displayable_time = None
            if isinstance(time_to_be_displayed, datetime):
                displayable_time = time_to_be_displayed.strftime("%H:%M")
            elif isinstance(time_to_be_displayed, timedelta):
                displayable_time = CommonMethods.get_hour_minute_str_from_timedelta(time_to_be_displayed)
            return displayable_time

    def get_all_times_as_displayables(self) -> dict:
        displayable_times = Constants.get_const_day_times_dict()
        for key in displayable_times:
            if key == "day_date":
                displayable_times[key] = CommonMethods.get_printable_date(self.__day_times[key])
            elif key == "time_balance" and self.__is_time_balance_negative:
                displayable_times[key] = f"-{self.get_displayable_time(key)}"
            else:
                displayable_times[key] = self.get_displayable_time(key)
        return displayable_times

    def get_all_times_in_printable_format(self) -> str:
        displayable_times = self.get_all_times_as_displayables()
        displayble_list = []
        separator = "\n"
        for key, time in displayable_times.items():
            displayble_list.append(f"{key}: {time}")
        displayable_str = separator.join(displayble_list)
        return displayable_str

    def get_time_balance_with_negativity_flag(self) -> (timedelta, bool):
        return self.__day_times["time_balance"], self.__is_time_balance_negative
