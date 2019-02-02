from Resources.Strategies.Strategy import Strategy


class ListWorkdays(Strategy):
    def start_strategy(self, actor):
        actor.list_workdays()
