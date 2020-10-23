class FinalBattle(Scene):

    def enter(self):
        print(dedent("""
        Room Description - What do you pick?
        A)
        B)
        C)
        """))

        action = input("> ")
        input.lower()

        if action == "a":
            print(dedent("""
            Fail Description 1
            """))
            return 'death'

        elif action == "b":
            print(dedent("""
            Fail Description 2
            """))
            return 'death'

        elif action == "c":
            print(dedent("""
            Pass Description
            """))
            return 'finished'

        else:
            print("That's not an option, my friend.")
            return 'final_battle'
