from datetime import datetime

from Resources import Constants, CommonMethods
from Resources.Strategies import Strategy
from Resources.Strategies.Resources import Constants as StrategyConstants


class ConsoleUi:
    def __init__(self):
        self.__main_menu = Constants.get_const_main_menu()
        self.__strategies = StrategyConstants.get_const_strategies_dict()
        self.__observers = []

    def display_main_menu(self) -> None:
        main_menu_str = CommonMethods.get_menu_string(self.__main_menu)
        self.display(main_menu_str)

    def main_menu_loop(self) -> None:
        input_prompt = Constants.get_const_msg_input_prompt()
        input_prompt = f"{CommonMethods.get_string_with_separator(input_prompt)}\n"
        number_of_menu_items = len(self.__main_menu)

        while True:
            user_choice = input(input_prompt)[0:1]

            if user_choice.isdigit() and self.__is_user_choice_valid(user_choice, number_of_menu_items):
                user_choice = self.__get_key_for_number(int(user_choice))
                user_choice = self.__strategies[user_choice]
                self.__notify_observers(user_choice)
            else:
                message_choice_invalid = Constants.get_const_msg_choice_invalid()
                self.display(message_choice_invalid)

            self.display_main_menu()

    def __is_user_choice_valid(self, choice: str, menu_range: int) -> bool:
        return 0 < int(choice) <= menu_range

    def __get_key_for_number(self, option_number: int) -> str:
        for num, (key, menu_item) in enumerate(self.__main_menu.items(), start=1):
            if num == option_number:
                return key
        return ""

    def enter_new_workday_data(self) -> dict:
        workday_data_prompt = Constants.get_const_msg_workday_data_prompt()
        workday_data_keys = Constants.get_const_addable_time_keys()
        workday_data = {}

        self.display(workday_data_prompt)

        for key in workday_data_keys:
            while True:
                try:
                    if key == "day_date":
                        workday_data[key] = datetime.strptime(input(f"{key}: "), "%d.%m.%Y")
                    else:
                        workday_data[key] = CommonMethods.timedelta_parse(input(f"{key}: "))
                except ValueError:
                    use_correct_format = Constants.get_const_msg_use_correct_format()
                    self.display(use_correct_format)
                else:
                    break

        return workday_data

    def display(self, message: str):
        message = CommonMethods.get_string_with_separator(message)
        print(message)

    def subscribe(self, observer) -> None:
        self.__observers.append(observer)

    def unsubscribe(self, observer) -> None:
        self.__observers.remove(observer)

    def __notify_observers(self, strategy: Strategy) -> None:
        for observer in self.__observers:
            observer.update(strategy)
