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
        "You died. Wait… Already?? You must be bad at this.",
        "You’re a looooooooooser.",
        "I bet a small kitten could have gotten further than this.",
        "I guess you gotta retry… again. And again. And again. >:)",
        "I bet you wish you were playing Dark Souls right now, huh?",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class ForestEntrance(Scene):

    def enter(self):
        print(dedent("""
        You are the hero of this story. A valiant, battle-worn knight who
        has slain dragons, ghouls and goblins alike. One night, you wake up
        to the screams of your brother who is being dragged away by a mob
        of goblins into the enchanted forest, it’s sacrifice night. Your brother
        is the perfect sacrifice the evil witch needs to summon her undead army
        and take over the country.

        You quickly pick up your Bag, Sword & Shield and chase the goblins to the
        forest entrance. A small group of goblins turn around to confront you,
        snarling, snapping and readying their weapons. They block the entrance to
        the forest and are about to attack you.

                What do you do? (Enter A, B or C)

        A) Charge at them sword first!
        B) Turn back, it is what it is. There’s too many to take on…
        C) You find a small bomb in your bag. Light and throw it!
        """))

        action = input("> ")

        if action == "A":
            print(dedent("""
            With no hesitation, you charge directly at the group of goblins!
            One after another, you cut down the small goblins knowing you can
            easily overpower each individual one. But goblins are sneaky…
            they plotted knowing you would charge in and had goblin archers
            waiting behind the trees. The barrage of arrows is too much for you
            to handle, as you’re turning to take on the archers, one arrow
            gets you in the knee. The next in the eye.
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            Really? You didn’t even try? Some hero you are…
            """))
            return 'death'

        elif action == "C":
            print(dedent("""
            You search your bag and see a small black powder bomb in it, perfect
            for groups of enemies! You set it alight and chuck it into the crowd
            to disperse of these goblins. As you throw the bomb, you see goblins
            behind the trees run for their lives, they must have PTSD from
            previous bomb experiences… the bomb dispatches of the goblin group.
            You run as fast as you can to catch up with the goblin mob.
            You notice a peculiar looking tree; a druid screams at you.

            "HEY! You’re gonna need this if you’re going to take on the witch!"
            """))
            return 'chest_room'

        else:
            print("That's not an option, my friend.")
            return 'forest_entrance'


class ChestRoom(Scene):

    def enter(self):
        print(dedent("""
        The druid’s beckons to you with his warning. He utters the words
        “Beware fair knight, for the witch is a powerful foe, you will not be
        able to defeat her as you are. Within this tree is a collection of nine
        chests, one of which contains a magical gauntlet which can disable the
        witches magic barrier and create the opening for you to strike! However,
        the other eight chests are mimics. Powerful creatures that pretend to
        be chests, waiting for the curious to open just to consume them where
        they stand!” You enter the tree to find yourself in a spacious, dark
        room, you turn and ask the druid “Is there no way you can help me find
        out which one it is in?”. The druid turns and says:
            “Pfffft, nah mate. You’re on your own there, I like my hands.”

                        (Choose a chest between 1 – 9)
        """))

        attempt = f"{randint(1,9)}"
        guess = input("Which chest will you choose? > ")
        guesses = 0

        while guess != attempt and guesses < 5:
            print("Nearly lost your hand there!")
            guesses += 1
            guess = input("Which chest will you choose? > ")

        if guess == attempt:
            print(dedent("""
            You guessed correctly! The gods are on your side. You open the
            chest to see a shining gauntlet, radiating an enormous amount power.
            With this power, you feel unstoppable! You don the gauntlet and
            start sprinting out of the tree, rushing off to rescue your brother.
            Before you get out of the dark room in the tree, the druid says to
            you “The goblins would have taken your brother to the top of the ancient
            tree in the center of the forest. Follow the path outside this tree to
            a great vine ladder, you can’t miss it, it’ll take you right to the top.
            Oh yeah! I almost forgot, to activate the gauntlet you need to utter the
            magical words! I forgot what they were… something stupid… but whatever,
            you’ll be fine, it’ll come to you! Good luck, Knight!”.  You sprint on
            the path as fast as you can.
            """))
            return 'the_ladder'

        else:
            print(dedent("""
            You reach into the chest, hoping to see the gauntlet but alas… there is
            no gauntlet. As you’re reaching in, large sharp teeth grow out of the
            lip of the chest and the chest slams shut faster than the human eye
            can see. You look down to no longer see an arm where there once was.
            From the blood loss, you start to faint, as your eyesight dims, you see
            the chest grow legs and arms, opening it’s fanged mouth. The druid
            screams “I’m not involved!” and sprints out of the tree. The mimic
            picks you up and eats you.
            """))
            return 'death'


class TheLadder(Scene):

    def enter(self):
        print(dedent("""
        Sprinting through the forest, you take sight of the vine ladder the druid
        was talking about. Wow… that is one tall tree and one flimsy ladder.
        You wonder whether it’ll hold your weight but you haven’t got time to think
        about that now, your brother’s about to be sacrificed and you’ve come this far!
        Can’t turn back. You arrive to the base of the ladder and start your climb.

        The ladder feels too flimsy, you throw away your bag, the ladder can’t take the
        extra weight. As you continue the high climb, you see a goblin archer far down
        at the bottom of the ladder readying their arrow to take you down.

                What do you do? (Enter A, B or C)

        A) Hold your shield to deflect the arrows whilst you climb!
        B) Throw your sword at the goblin archer!
        C) Power through and keep climbing!
        """))

        action = input("> ")

        if action == "A":
            print(dedent("""
            You don your shield with your right hand, deflecting every arrow the goblin
            archer shoots at you. You think to yourself “Hey, this was a great idea!
            This is going smoothly!” and smile smugly. As you look at the goblin to deflect
            another one of his arrows, your grip misses the next ladder step; not able to
            control how your weight has shifted, you fall backwards off of the ladder.
            You climbed quite high so this is a long fall, while dropping you have time
            to reflect: “I should have looked where I was climbing, huh?”. You die upon
            impact with the floor.
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            You see the goblin archer nocking his arrow, readying his shot at you.
            You dropped your bag so that’s not an option… but aha! You still have your sword.
            “Will I need this later on? I don’t have the time to think about it, I just
            gotta do it!”. You aim your throw and like a master sword thrower, you fling
            your sword at the goblin archer, getting it right between the eyes. Nice shot!
            You continue the ascent, getting to the top where the evil witch awaits…
            """))
            return 'final_battle'

        elif action == "C":
            print(dedent("""
            You think to yourself “Goblin archers are stupid… their aim isn’t any better than
            the stormtroopers from Star Wars. I’ll be fine” and continue the climb.
            The first few shots miss, justifying your choice. As you make your way up, an
            arrow hits you in the knee. Ouch! Another arrow hits you in the arm, breaking
            your grip on the ladder. As you fall backwards, you think to yourself
            “Maybe I shouldn’t have underestimated it”. The goblin smirks with a
            smug grin and lines up one last shot. Draw, Aim, Fire. The shot hits you
            right between the eyes before you even hit the floor. I guess this goblin
            was a prodigy archer?
            """))
            return 'death'

        else:
            print("That's not an option, my friend.")
            return 'the_ladder'


class FinalBattle(Scene):

    def enter(self):
        print(dedent("""
        You get to the top of the ancient tree and see the evil witch, old,
        wrinkled and diseased conjuring an evil spell, holding your brother
        sustained in midair. She’s chanting spiritual words and hasn’t taken notice
        of you yet so you attempt to sneak behind her and get a hit in.
        “You think I’m that foolish?” She says. You are blown back by a magical
        barrier and hit the wall with force. “She’s too powerful…” your brother
        murmurs, “there’s nothing we can do.”

        Hopeless and dazed, it feels like all is lost. You remember! The magic gauntlet!
        The druid said you’d need it to defeat the witch! You hold it up and the
        witch cowers in fear, “How did you get that?!”. However, it’s not doing
        anything… It needs magical words to activate it! What were they again?

                What do you say? (Enter A, B or C)

        A) Expelliarmus!
        B) Destroy!
        C) Ummmm… 69420?
        """))

        action = input("> ")

        if action == "A":
            print(dedent("""
            You stand proud and you scream the first thing that comes to your mind with vigor!
            The gauntlet, however, stays silent and dull. This isn’t Harry Potter, mate.
            The witch speaks: “Bahahaha, you don’t even know the activation chant?”.
            As the witch cackles, she picks you up with her magical blue stasis spell.
            With force, she pulls your body apart limb from limb. “Now I have twice the
            sacrifice needed!” she declares. The witch kills you and your brother.
            All is lost.
            """))
            return 'death'

        elif action == "B":
            print(dedent("""
            You have no idea what to say, but this seems most logical and could work!
            You’re basically telling the gauntlet what you want it to do right? But the witch
            stares at you blankly, knowing you don’t know the activation chant. You scream
            the word at the top of your lungs, the gauntlet does nothing. “Waste of my time”
            the witch said annoyingly, and uses her power to throw you off of the top of
            the tree. You fall to your death.
            """))
            return 'death'

        elif action == "C":
            print(dedent("""
            No idea what to say or do… but then it suddenly springs to mind, the Druid said that
            it was ‘something stupid’, right? What would make no sense in this context?
            You look at the gauntlet and say “69420?”. The gauntlet glows blue and gold,
            unleashing a magical force wave freeing your brother of the evil spell and
            knocking the witch down onto her knees. “Really?” You ask yourself, as the
            gauntlet shines bright. “Whatever.”, you walk up to the witch, punching her
            in the face with the gauntlet and decimating all that is left of her.
            You pick up your brother and take him home. You’re both gonna need some rest after that.
            """))
            return 'finished'

        else:
            print("That's not an option, my friend.")
            return 'final_battle'


class Finished(Scene):
    def enter(self):
        print(dedent("""
        You've conquered the forest, defeated the witch and rescued your brother!
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
