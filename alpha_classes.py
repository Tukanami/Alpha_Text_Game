#REFERENCE PAGE 228 (MAIN) and 200 (SKELETON)
class Scene(object):            # created

    def enter(self):
        pass

class Engine(object):           # created

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):             # created

    def enter(self):
        pass

class ForestEntrance(Scene):    # created

    def enter(self):
        pass

class ChestRoom(Scene):         # created

    def enter(self):
        pass

class TheLadder(Scene):         # created

    def enter(self):
        pass

class FinalBattle(Scene):       # created

    def enter(self):
        pass

class Map(object):              # created

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass
