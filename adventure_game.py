import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


# get the current foe
def get_foe():
    foes = ["pirate", "dragon", "witch", "gorgon"]
    return random.choice(foes)


# display introduction
def display_intro(foe):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {foe} is somewhere around here, and "
                "has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


# present game choice
def get_path():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    return get_valid_input("(Please enter 1 or 2.)\n", ["1", "2"])


# check if input is valid
def get_valid_input(message, choices):
    choice = input(message).lower()
    if choice in choices:
        return choice
    else:
        get_valid_input(message, choices)


# confront foe
def confront_foe(weapon, foe):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                f"{foe}.")
    print_pause(f"Eep! This is the {foe}'s house!")
    print_pause(f"The {foe} attacks you!")
    if weapon == "dagger":
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")


# fight or run away
def fight_or_flee():
    return get_valid_input("Would you like to (1) fight or (2) run away?\n",
                           ["1", "2"])


# play again or quit
def replay_or_quit():
    choice = get_valid_input("Would you like to play again? (y/n)\n",
                             "[y,n]")
    if choice == "y":
        print_pause("Excellent! Restarting the game ...\n")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")


# fight foe
def fight_foe(weapon, foe):
    if weapon == "dagger":
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {foe}.")
        print_pause("You have been defeated!")
        replay_or_quit()
    else:  # player has sword of Ogoroth
        print_pause(f"As the {foe} moves to attack, you unsheath your new "
                    "sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as "
                    "you brace yourself for the attack.")
        print_pause(f"But the {foe} takes one look at your shiny new toy "
                    "and runs away!")
        print_pause(f"You have rid the town of the {foe}. You are "
                    "victorious!")
        replay_or_quit()


# enter cave with dagger
def enter_with_dagger():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword "
                "with you.")
    print_pause("You walk back out to the field.")


# enter cave with sword
def enter_with_sword():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now.")
    print_pause("You walk back out to the field.")


# knock on door or enter cave
def play_path(path, weapon, foe):
    if path == '1':  # knock on door
        confront_foe(weapon, foe)
        choice = fight_or_flee()
        if choice == '1':  # fight
            fight_foe(weapon, foe)
        else:  # run away
            print_pause("You run back into the field. Luckily, you don't "
                        "seem to have been followed.\n")
            path = get_path()
            play_path(path, weapon, foe)
    else:  # enter cave
        if weapon == "dagger":
            enter_with_dagger()
            weapon = "sword"  # get the sword of Ogoroth
        else:  # enter with sword of Ogoroth
            enter_with_sword()

        path = get_path()
        play_path(path, weapon, foe)


def play_game():
    foe = get_foe()
    display_intro(foe)
    path = get_path()
    play_path(path, weapon, foe)


weapon = "dagger"
play_game()
