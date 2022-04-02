import random
import time
import sys


def typewriter_simulator(message: str):
    """
    Simulates a typewriter effect by implementing a delay before
    each letter appears.
    """
    for letter in message:
        time.sleep(0.03)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()


def print_pause(message: str, delay: int = 1):
    """
    Implements a time lag of 2 seconds after every message displayed
    on the console. Used to simulate a slower, more realistic
    gaming experience.
    """
    typewriter_simulator(message)
    time.sleep(delay)


def valid_input(prompt: str, options: list) -> str:
    """
    Validates that the provided input is among the expected options.
    Forces the user to re-enter their input until they enter a valid
    input.
    """
    while True:
        response = input(prompt).lower()
        if response in options:
            break
        elif response in options:
            break
        else:
            print_pause("Sorry, I don't understand.\n")
    return response


def origin():
    """
    Gives the intro to the game, defines the weapon the player
    begins with, and randomly selects the opponent for the game

    Returns:
    weapon [str]: the name of the weapon to be used
    attacker [str]: the randomly selected attacker for the game
    """
    weapon = "dagger"
    attackers = ["pirate", "wicked fairie", "gorgon", "dragon", "troll"]
    attacker = random.choice(attackers)

    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {attacker} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("\nIn front of you is a house.")
    print_pause("\nTo your right is a dark cave.")
    print_pause("\nIn your hand you hold your trusty "
                "(but not very effective) dagger.")

    return weapon, attacker


def cave(weapon: str, attacker: str):
    """
    Sets out the sequence of events to follow if the user enters the cave.

    Action:
    1. If the user still has a dagger, give them a sword and
    modify the weapon variable.
    2. If the user already has a sword, send them back with no change.
    """
    print_pause("You peer cautiously into the cave.")

    if weapon == "sword":
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")

    elif weapon == "dagger":
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        weapon = "sword"
    print_pause("\nYou walk back out to the field.")
    field(weapon, attacker)


def fight(weapon: str, attacker: str):
    """
    Sets out the sequence of events to follow if the user chooses to fight.

    Action:
    1. If the user still has a dagger, they lose the fight.
    2. The user wins the fight if they've gotten the sword of ogoroth.
    """
    if weapon == "dagger":
        print_pause("\nYou do your best...")
        print_pause(f"but your dagger is no match for the {attacker}.")
        print_pause("\nYou have been defeated!")

    elif weapon == "sword":
        print_pause(f"\nAs the {attacker} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("\nThe Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {attacker} takes one look at your shiny new toy "
                    "and runs away!")
        print_pause(f"\nYou have rid the town of the {attacker}. "
                    "You are victorious!")


def house(weapon: str, attacker: str):
    """
    Sets out the sequence of events to follow if the user goes for the house.

    Action:
    1. If the user still has a dagger, alert them they're underprepared.
    2. Present the user with the option to either fight or run back to field.
    3. Keep loop running until user inputs valid option.
    """
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps "
                f"a {attacker}.")
    print_pause(f"\nEep! This is the {attacker}'s house!")
    print_pause(f"\nThe {attacker} attacks you!")

    if weapon == "dagger":
        print_pause("\nYou feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")

    fight_or_run = valid_input("\nWould you like to (1) fight or"
                               " (2) run away? ", ['1', '2'])

    if fight_or_run == '1':
        fight(weapon, attacker)
    elif fight_or_run == '2':
        print_pause("You run back into the field. Luckily, you don't seem "
                    "to have been followed.")
        field(weapon, attacker)


def field(weapon: str, attacker: str):
    """
    Allows the user select whether to proceed to the house or the cave.
    """
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("\nEnter 2 to peer into the cave.")
    door_or_cave = valid_input("\nWhat would you like to do? "
                               "\n(Enter 1 or 2): ", ['1', '2'])

    if door_or_cave == '1':
        house(weapon, attacker)
    elif door_or_cave == '2':
        cave(weapon, attacker)


def main():
    """
    Entry point into the game. Sets the two important variables and allows
    the player play as many times as they'd like to.
    Ends the game when player decides to quit.
    """
    weapon, attacker = origin()
    field(weapon, attacker)

    play_again = valid_input("\nWould you like to play again? (y|n): ",
                             ['y', 'n']).lower()
    if play_again == 'y':
        print_pause("\nExcellent! Restarting the game...")
        print_pause("\n.................\n")
        weapon, attacker = origin()
        field(weapon, attacker)

    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time!")
        exit(0)


if __name__ == "__main__":
    main()
