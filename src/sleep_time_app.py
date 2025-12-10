from sleep_calculator import SleepCalculator
from ui_console import UiConsole
from history_storage import HistoryStorage
from tips_service import TipsService


class SleepTimeApp:
    def __init__(self):
        self.calculator = SleepCalculator()
        self.ui = UiConsole()
        self.history = HistoryStorage()
        self.tips = TipsService()

    def run(self):
        last = self.history.load()
        if last is not None:
            print(f"Last saved suggested sleep time: {last}\n")

        wake_time = self.ui.read_time_input()
        results = self.calculator.calculate_by_wake_time(wake_time)

        self.ui.render_results(results)

        # Save the first suggested option if it exists
        if results:
            self.history.save(results[0].time_option)

        self.ui.show_tips(self.tips.get_short_tips())

