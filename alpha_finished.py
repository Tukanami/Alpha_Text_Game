class Finished(Scene):
    def enter(self):
        print(dedent("""
        You've conquered the forest and rescued your brother!
        You've won! Good Job!
        """))
        return 'finished'
