from random import randint
from sys import exit
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


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

        if action == "A":
            print(dedent("""
            Action Choice 1
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            Action Choice 2
            """))
            return 'death'

        elif action == "C":
            print(dedent("""
            Action Choice 3
            """))
            return 'chest_room'

        else:
            print("That's not an option, my friend.")
            return 'forest_entrance'


class ChestRoom(Scene):

    def enter(self):
        print(dedent("""
        Room Description - 3 attempts - between 1 and 9
        """))

        attempt = randint(1,9)
        guess = input("Which one will you choose? > ")
        guesses = 0

        while guesses != attempt and guesses < 3:
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


class TheLadder(Scene):

    def enter(self):
        print(dedent("""
        Room Description 1 - What response?
        A)
        B)
        C)
        """))

        action = input("> ")

        if action == "A":
            print(dedent("""
            Fail Description 1
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            Pass Description
            """))
            return 'final_battle'

        elif action == "C":
            print(dedent("""
            Fail Description 2
            """))
            return 'death'

        else:
            print("That's not an option, my friend.")
            return 'the_ladder'


class FinalBattle(Scene):

    def enter(self):
        print(dedent("""
        Room Description - What do you pick?
        A)
        B)
        C)
        """))

        action = input("> ")

        if action == "A":
            print(dedent("""
            Fail Description 1
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            Fail Description 2
            """))
            return 'death'

        elif action == "C":
            print(dedent("""
            Pass Description
            """))
            return 'finished'

        else:
            print("That's not an option, my friend.")
            return 'final_battle'


class Finished(Scene):
    def enter(self):
        print(dedent("""
        You've conquered the forest and rescued your brother!
        You've won! Good Job!
        """))
        return 'finished'

class Map(object):
    scenes = {
        'forest_entrance': ForestEntrance(),
        'chest_room': ChestRoom(),
        'the_ladder': TheLadder(),
        'final_battle': FinalBattle(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('forest_entrance')
a_game = Engine(a_map)
a_game.play()
