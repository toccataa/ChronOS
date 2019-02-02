from Resources.Strategies.Strategy import Strategy


class AddWorkday(Strategy):
    def start_strategy(self, actor):
        actor.add_workday()
