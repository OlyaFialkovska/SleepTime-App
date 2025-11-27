from time_model import Time


class CyclePlan:
    def __init__(self, time_option: Time, cycles_count: int):
        self.time_option = time_option
        self.cycles_count = cycles_count

    def format(self) -> str:
        return f"{self.time_option} (cycles: {self.cycles_count})"

