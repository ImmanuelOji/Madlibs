
print("Welcome to Anecdoty!!!")
print("Ever wanted to relive your childhood stories??")
print("Anecdoty is an app where you can relive your childhood stories but in your own words!!")

print(" ")

print("Pick a story you want to read")
story_1 = "The Hare and the Tortoise"
story_2 = "The Dog and the Bone"
story_3 = "The boy who cried wolf"


def the_hare_and_the_tortoise():
    noun = input("Put in a noun: ")
    noun_2 = input("Put in a noun: ")
    adj = input("Put in an adjective: ")
    verb = input("Put in a verb in continuous tense: ")
    verb_2 = input("Put in a verb: ")

    the_hare_tortoise = f"There was once a {noun} who was friends with a {noun_2}.\
            One day, he challenged the {noun_2} to a race.\
             Seeing how {adj} the {noun_2} was {verb}, the {noun} thought he’ll win this easily.\
              So he took a {verb_2} while the {noun_2} kept on {verb}. When the {noun} woke up,\
               he saw that the {noun_2} was already at the finish line. Much to his chagrin,\
                the {noun_2} won the race while he was busy {verb_2}ing."

    print(the_hare_tortoise)


def the_dog_and_the_bone():
    noun = input("put in a noun: ")
    noun_2 = input("put in a noun: ")
    noun_3 = input("put in a noun: ")
    adj = input("put in an adjective: ")

    the_dog_the_bone = f"Once there was a {noun} who wandered the streets night and day in search of {noun_2}. \
            One day, he found a big juicy {noun_3} and he immediately grabbed it between his mouth and took it home.\
                On his way home, he crossed a river and saw another {noun} who also had a {noun_3} in its mouth. \
                He wanted that {noun_3} for himself too.\
                But as he opened his mouth, the {noun_3} he was biting fell into the river and sank.\
                That night, he went home {adj}."

    print(the_dog_the_bone)


def the_boy_who_cried_wolf():
    noun = input("put in a noun: ")
    noun_2 = input("put in a noun: ")
    verb = input("put in a verb in past tense: ")
    verb_2 = input("put in verb in continuous tense: ")
    verb_3 = input("put in verb in continuous tense: ")

    the_boy_wolf = f"There was once a {noun} who liked to play tricks.\
        One day, while he was watching over the {noun_2}, the {noun} decided to play a trick and cried “wolf! wolf!”.\
                The people who heard {verb} over to help him. But they were disappointed when they saw that there was\
                no wolf and the {noun} was {verb_2} at them. The next day, he did it again and people {verb} to his aid\
                only to be disappointed once again. On the third day, the {noun} saw a wolf {verb_3} one of his sheep\
                and cried for help. But the people who heard him thought this is just another of the {noun}’s pranks so\
                   no one came to help him. That day, the {noun} lost some of his sheep to the wolf."

    print(the_boy_wolf)


print(story_1)
print(story_2)
print(story_3)
print(" ")
pick = int(input("press 1 for the first story, 2 for the second and 3 for the third: "))

if pick == 1:
    print(" ")
    print("The Hare and the Tortoise")
    the_hare_and_the_tortoise()

if pick == 2:
    print(" ")
    print("The Dog and the Bone")
    the_dog_and_the_bone()

if pick == 3:
    print(" ")
    print("The boy who cried wolf")
    the_boy_who_cried_wolf()
