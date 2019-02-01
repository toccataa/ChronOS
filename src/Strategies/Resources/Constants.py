from Strategies import AddWorkday, ListWorkdays, ExitProgram


def get_const_strategies_dict() -> dict:
    strategies = {
        "add_workday": AddWorkday.AddWorkday(),
        "edit_workday": "Edit workday",
        "delete_workday": "Delete workday",
        "list_workdays": ListWorkdays.ListWorkdays(),
        "total_balance": "Calculate total time balance",
        "range_balance": "Calculate time balance for range",
        "exit_program": ExitProgram.ExitProgram()
    }
    return strategies
