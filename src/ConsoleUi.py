from datetime import datetime, timedelta

from Resources import Constants, CommonMethods


class ConsoleUi:
    def __init__(self):
        self.__main_menu = Constants.get_const_main_menu()
        self.__observers = []

    def display_main_menu(self) -> None:
        print(" * * * * *")
        for num, (key, menu_item) in enumerate(self.__main_menu.items(), start=1):
            print(f"{num}.) {menu_item}")

    def menu_loop(self) -> None:
        input_prompt = Constants.get_const_input_prompt()
        number_of_menu_items = len(self.__main_menu)

        while True:
            user_choice = input(input_prompt)[0:1]

            if CommonMethods.is_number(user_choice) and self.__is_user_choice_valid(user_choice, number_of_menu_items):
                user_choice = self.__get_option_for_number(int(user_choice))
                self.__notify_observers(user_choice)
            else:
                message_choice_invalid = Constants.get_const_choice_invalid()
                print(message_choice_invalid)

            self.display_main_menu()

    def __is_user_choice_valid(self, choice: str, menu_range: int) -> bool:
        return 0 < int(choice) <= menu_range

    def __get_option_for_number(self, option_number: int) -> str:
        for num, (key, menu_item) in enumerate(self.__main_menu.items(), start=1):
            if num == option_number:
                return key
        return ""

    def enter_new_workday_data(self) -> dict:
        workday_data_prompt = Constants.get_const_workday_data_prompt()
        workday_data_keys = Constants.get_const_addable_time_keys()
        workday_data = {}

        print(workday_data_prompt)

        for key in workday_data_keys:
            if key == "day_date":
                workday_data[key] = datetime.strptime(input(f"{key}: "), "%d.%m.%Y")
            else:
                workday_data[key] = CommonMethods.timedelta_parse(input(f"{key}: "))

        return workday_data

    def subscribe(self, observer) -> None:
        self.__observers.append(observer)

    def unsubscribe(self, observer) -> None:
        self.__observers.remove(observer)

    def __notify_observers(self, message: str) -> None:
        for observer in self.__observers:
            observer.update(message)
