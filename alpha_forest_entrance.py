class ForestEntrance(Scene):

    def enter(self):
        print(dedent("""
        Base Description - Forest Entrance Scene
        What do you do?
        A)
        B)
        C)
        """))

        action = input("> ")
        input.lower()

        if action == "a":
            print(dedent("""
            Action Choice 1
            """))
            return 'death'

        elif action == "b":
            print(dedent("""
            Action Choice 2
            """))
            return 'death'

        elif action == "c":
            print(dedent("""
            Action Choice 3
            """))
            return 'chest_room'

        else:
            print("That's not an option, my friend.")
            return 'forest_entrance'
            
