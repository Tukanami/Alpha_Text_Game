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
        return self.next(self.start_scene)
