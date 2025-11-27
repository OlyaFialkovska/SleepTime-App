import os
from time_model import Time


class HistoryStorage:
    def __init__(self, path: str = "last_result.txt"):
        self.path = path

    def save(self, time_obj: Time):
        """Save last suggested sleep time to a simple text file."""
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                f.write(f"{time_obj.hour} {time_obj.minute}")
        except OSError:
            # For a simple lab project we silently ignore storage errors
            pass

    def load(self):
        """Load last suggested sleep time if file exists and is valid."""
        if not os.path.exists(self.path):
            return None

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                content = f.read().strip()
            parts = content.split()
            if len(parts) != 2:
                return None
            hour = int(parts[0])
            minute = int(parts[1])
            return Time(hour, minute)
        except (OSError, ValueError):
            return None

