from datetime import datetime, timedelta


def get_longest_line_length(multiline_string: str) -> int:
    lines_list = multiline_string.splitlines()
    longest_line_length = 0

    for line in lines_list:
        current_line_length = len(line)
        if current_line_length > longest_line_length:
            longest_line_length = current_line_length

    return longest_line_length


def get_printable_date(date: datetime) -> str:
    return date.strftime("%d.%m.%Y")


def get_zeroed_time_string(time_period: int) -> str:
    if -10 < time_period < 0:
        time_str = f"-0{str(time_period)[1:]}"
    elif 0 <= time_period < 10:
        time_str = f"0{time_period}"
    else:
        time_str = str(time_period)
    return time_str


def get_hour_minute_str_from_timedelta(time_period: timedelta) -> str:
    total_seconds = time_period.total_seconds()
    total_minutes = int(total_seconds // 60)
    total_hours = int(total_minutes // 60)
    remaining_minutes = int(total_minutes % 60)
    total_hours_str = get_zeroed_time_string(total_hours)
    remaining_minutes_str = get_zeroed_time_string(remaining_minutes)
    displayable_time = f"{total_hours_str}:{remaining_minutes_str}"
    return displayable_time


def get_interpreted_time_balance(time_balance: timedelta, time_balance_negativity_flag: bool) -> str:
    if time_balance_negativity_flag:
        interpreted_time_balance = f"-{get_hour_minute_str_from_timedelta(time_balance)}"
    else:
        interpreted_time_balance = get_hour_minute_str_from_timedelta(time_balance)
    return interpreted_time_balance


def is_number(check: str) -> bool:
    try:
        int(check)
    except ValueError:
        return False
    else:
        return True


def timedelta_parse(time_to_parse: str) -> timedelta:
    colon_pos = time_to_parse.find(":")
    parsed_time = timedelta(hours=int(time_to_parse[0:colon_pos]), minutes=int(time_to_parse[colon_pos+1:]))
    return parsed_time
