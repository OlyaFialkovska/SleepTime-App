class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def to_minutes(self) -> int:
        return self.hour * 60 + self.minute

    @classmethod
    def from_minutes(cls, total_minutes: int):
        total_minutes %= 24 * 60
        hour = total_minutes // 60
        minute = total_minutes % 60
        return cls(hour, minute)

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

