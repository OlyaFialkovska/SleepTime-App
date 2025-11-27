from time_model import Time
from cycle_plan import CyclePlan


class SleepCalculator:
    CYCLE_MINUTES = 90

    def calculate_by_wake_time(self, wake_time: Time):
        results = []
        wake_total = wake_time.to_minutes()

        # Suggest 3–6 full cycles of sleep
        for cycles in range(3, 7):
            sleep_total = wake_total - cycles * self.CYCLE_MINUTES
            sleep_time = Time.from_minutes(sleep_total)
            results.append(CyclePlan(sleep_time, cycles))

        return results

