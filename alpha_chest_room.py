class ChestRoom(Scene):

    def enter(self):
        print(dedent("""
        Room Description - 3 attempts - between 1 and 9
        """))

        attempt = f"{randint(1,9)}
        guess = input("Which one will you choose? > ")
        guesses = 0

        while guesses != attempt and guesses < 10:
            print("Nearly lost your hand there!")
            guesses += 1
            guess = input("Which one will you choose? > ")

        if guess == attempt:
            print(dedent("""
            Pass Description - receiving the item
            """))
            return 'the_ladder'

        else:
            print(dedent("""
            Fail Description - hand bitten off
            """))
            return 'death'
