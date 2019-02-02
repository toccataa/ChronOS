from ConsoleUi import ConsoleUi
from Resources.Strategies import Strategy
from Resources.TimeHandlers.TimeKeeper import TimeKeeper


class MainController:
    def __init__(self):
        self.__timeKeeper = TimeKeeper()
        self.__ui = ConsoleUi()

    def run_program(self):
        self.__ui.subscribe(self)
        self.__ui.display_main_menu()
        self.__ui.menu_loop()

    def add_workday(self):
        new_workday_data = self.__ui.enter_new_workday_data()
        self.__timeKeeper.add_workday(new_workday_data)

    def list_workdays(self):
        all_workdays = self.__timeKeeper.get_all_workdays()
        for date, workday in all_workdays.items():
            print(date)
            print(workday.get_all_times_in_printable_format())

    def exit_program(self):
        quit()

    def update(self, strategy: Strategy):
        strategy.start_strategy(self)


ChronOS = MainController()
ChronOS.run_program()

