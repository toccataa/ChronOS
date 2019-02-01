import Workday
from TimeLog import TimeLog
from ConsoleUi import ConsoleUi

from Strategies import Strategy


class MainController:
    def __init__(self):
        self.__ui = None
        self.__newWorkday = None
        self.__timeLog = TimeLog()

    def run_program(self):
        self.__ui = ConsoleUi()
        self.__ui.subscribe(self)
        self.__ui.display_main_menu()
        self.__ui.menu_loop()

    def add_workday(self):
        new_workday_data = self.__ui.enter_new_workday_data()
        self.__newWorkday = Workday.Workday()
        for key, data in new_workday_data.items():
            self.__newWorkday.add_time(key, data)
        self.__newWorkday.calculate_times()
        self.__timeLog.add_workday(self.__newWorkday)

    def list_workdays(self):
        all_workdays = self.__timeLog.get_all_workdays()
        for date, workday in all_workdays.items():
            print(date)
            print(workday.get_all_times_in_printable_format())

    def exit_program(self):
        quit()

    def update(self, strategy: Strategy):
        strategy.start_strategy(self)


ChronOS = MainController()
ChronOS.run_program()

