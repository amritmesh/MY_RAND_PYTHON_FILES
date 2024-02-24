#This is an "adventure" game
def main():
    intro()
    items()
    encounter()
    choice = int(input('Choose your "weapon" (in numbers from 1 to 9): '))
    choices(choice)
    print("THE END!")

def intro():
    print("""Hello, young lad!
You have been chosen
to inherit your great
grandfather's cherished
potato farm! However, you
live on the other side of the
river. You must travel upstream
through the marsh to get to the
potato farm. Begin!""")

    input("Press ENTER to continue.")

def items():
    item = print("""You have packed several items for your "short" quest:
a fake mustache, a box of matches, pixie dust, the highest
quality nail file, highly concentrated pepper spray, one
single paper clip, strawberry-scented shampoo, Himalayan
pink salt, and most importantly,
A POTATO.""")

    input("Press ENTER to continue.")

def encounter():
    print("""Suddenly, you hear a horrendous squishing noise. You gag at
the repulsive stench of the highly visible green "gas" seeping
through the bushes. All signs of life have vanished. You turn around
to see a fat shadow in the midst of the gas. You reach into your pack.
Quick! What do you pull out?""")

    input("Press ENTER to continue.")

    print("""These are your choices:
potato = 1
mustache = 2
box = 3
dust = 4
file = 5
pepper = 6
clip = 7
shampoo = 8
salt = 9""")

def choices(choice):
    if choice == 1:
        print("""You hold the potato in your hand. You throw into the "gas"
with all the strength you have. There is a silence. Suddenly, you see the
gas swirling and getting absorbed by the potato. You run away before anything
bad happens.""")
    elif choice == 2:
        print("""You whip out the long shiny mustache. You slap above your mouth,
and neatly adjust so that it will pass as a proper disguise. You walk towards the
gas with all the pride you can muster, but just then, the mustache is ripped away
by the gas. You swear you could hear a faint 'remember me,', but all you could think
about is the excruciating pain bursting upon your upper lip.""")
    elif choice == 3:
        print("""You light the matches in the box, and throw it into the gas. BOOM!
Fire envelopes a fat shadow, and screaming, you run away. but it is too late. The fire
has already consumed you and the mysterious creature.""")
    elif choice == 4:
        print("""You use the pixie dust to fly above the gas. The gas rises higher, consuming
the hovering cloud of dust. You fall through the gas, and plop down face first into a huge
potato field.""")
    elif choice == 5:
        print("""You use the nail file to file down the mysterious green gas, which now has
appeared to be a solid. When you get to the core of solid "gas" you don't see a fat shadow
anymore. Instead, there stands your old Uncle Stuart.""")
    elif choice == 6:
        print("""You spray pepper spray into the gas, but it just drips down the side of the
"gas", which has now hardened into a solid.""")
    elif choice == 7:
        print("""You unfold the paper clip and craft an aluminum sowrd with it. You slash the
gas with three swift strikes, and in an instant, the chunks that you have cut off hit the ground
gurgling and squishing noise. You look where the chunk of gas, and a sizzling hole stares right
back at you where the solid "gas" was seconds before.""")
    elif choice == 8:
        print("""You take your strawberry scented shampoo, and squirt it all over the ground,
attempting to bring all signs of life back. Then, the animals grew out of the plants which started
growing, until the shampoo ran out.""")
    elif choice == 9:
        print("""You sprinkle the salt over the mysterious green gas, and get a napkin and utensils
to eat it. You take a huge bite out of it, expecting a good result. But a few seconds later, your heart
stops. You slowly black out. Your last thought is how you will never inherit your great grandfather's
potato farm.""")
    
main()
