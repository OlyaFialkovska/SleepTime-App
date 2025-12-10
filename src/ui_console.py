from time_model import Time


class UiConsole:
    def read_time_input(self) -> Time:
        print("=== SleepTime ===")
        print("This demo calculates suggested times to go to sleep")
        print("based on 90-minute sleep cycles.\n")

        while True:
            try:
                hour = int(input("Enter wake-up hour (0-23): "))
                minute = int(input("Enter wake-up minute (0-59): "))
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    return Time(hour, minute)
                print("Invalid time. Please enter values in correct ranges.\n")
            except ValueError:
                print("Please enter numbers only.\n")

    def render_results(self, results):
        print("\nSuggested times to go to sleep:")
        if not results:
            print("No results.")
            return

        for plan in results:
            print("-", plan.format())

    def show_tips(self, tips):
        print("\nBasic sleep tips:")
        for tip in tips:
            print("-", tip)

