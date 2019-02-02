def get_const_day_times_dict() -> dict:
    day_times_dict = {
        "day_date": None,
        "check_in": None,
        "check_out": None,
        "checked_in_total": None,
        "lunch_start": None,
        "lunch_finish": None,
        "lunch_total": None,
        "lunch_normalized": None,
        "net_work_time": None,
        "to_work_total": None,
        "time_balance": None
    }
    return day_times_dict


def get_const_addable_time_keys() -> list:
    addable_time_keys = ["day_date",
                         "check_in",
                         "check_out",
                         "lunch_start",
                         "lunch_finish",
                         "to_work_total"]
    return addable_time_keys


def get_const_main_menu() -> dict:
    main_menu = {
        "add_workday": "Add new workday",
        "edit_workday": "Edit workday",
        "delete_workday": "Delete workday",
        "list_workdays": "List workdays",
        "total_balance": "Calculate total time balance",
        "range_balance": "Calculate time balance for range",
        "exit_program": "Exit program"
    }
    return main_menu


def get_const_msg_input_prompt() -> str:
    input_prompt = "Please select an option."
    return input_prompt


def get_const_msg_choice_invalid() -> str:
    choice_invalid = "Please enter one of the numbers listed (just the number, nothing else)."
    return choice_invalid


def get_const_msg_workday_data_prompt() -> str:
    workday_data_prompt = "Please enter the following data for new workday\n" \
                          "(if one or more pieces of data are not available yet,\n" \
                          "just hit Enter without entry.)\n" \
                          "Use format DD.MM.YYYY for day_date and HH:MM for the rest."
    return workday_data_prompt


def get_const_msg_use_correct_format() -> str:
    use_correct_format = "Please use the correct format: DD.MM.YYYY for date, HH:MM for time of day."
    return use_correct_format


def get_const_msg_no_workdays_on_record() -> str:
    no_workdays_on_record = "There are no workdays on record yet. Nothing to display."
    return no_workdays_on_record