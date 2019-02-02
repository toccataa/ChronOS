from Resources import UIs
from Resources import Constants
from Resources.Strategies import Strategy
from Resources import TimeHandlers


class MainController:
    def __init__(self):
        self.__timeKeeper = TimeHandlers.get_timekeeper()
        self.__ui = UIs.get_console_ui()

    def run_program(self):
        self.__ui.subscribe(self)
        title = Constants.get_const_msg_title()
        self.__ui.display(title)
        self.__ui.display_main_menu()
        self.__ui.main_menu_loop()

    def add_workday(self):
        new_workday_data = self.__ui.enter_new_workday_data()
        self.__timeKeeper.add_workday(new_workday_data)

    def list_workdays(self):
        all_workdays = self.__timeKeeper.get_all_workdays()

        if len(all_workdays) == 0:
            message = Constants.get_const_msg_no_workdays_on_record()
            self.__ui.display(message)
        else:
            for date, workday in all_workdays.items():
                print(date)
                print(workday.get_all_times_in_printable_format())

    def exit_program(self):
        exit_message = Constants.get_const_msg_exiting_program()
        self.__ui.display(exit_message)
        quit()

    def update(self, strategy: Strategy):
        strategy.start_strategy(self)


ChronOS = MainController()
ChronOS.run_program()
