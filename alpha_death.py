class Death(Scene):
    quips = [
        "A",
        "B",
        "C",
        "D",
        "E",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)
