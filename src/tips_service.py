class TipsService:
    def __init__(self):
        self._tips = [
            "Avoid bright screens 1 hour before sleep.",
            "Keep your bedroom cool and dark.",
            "Try to go to bed and wake up at the same time.",
            "Avoid heavy meals and caffeine late in the day.",
        ]

    def get_short_tips(self):
        return self._tips[:2]

