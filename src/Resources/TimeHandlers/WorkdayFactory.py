from Resources.TimeHandlers.Workday import Workday


def create_workday(new_workday_data: dict) -> Workday:
    new_workday = Workday.construct_from_dict(new_workday_data)
    return new_workday
