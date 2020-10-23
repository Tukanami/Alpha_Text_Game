class TheLadder(Scene):

    def enter(self):
        print(dedent("""
        Room Description 1 - What response?
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
            Pass Description
            """))
            return 'final_battle'

        elif action == "c":
            print(dedent("""
            Fail Description 2
            """))
            return 'death'

        else:
            print("That's not an option, my friend.")
            return 'the_ladder'
