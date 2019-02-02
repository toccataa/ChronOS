from Resources.Strategies.Strategy import Strategy


class ExitProgram(Strategy):
    def start_strategy(self, actor):
        actor.exit_program()
