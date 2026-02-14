#Russian Roulette
import random
import time


chambers=[0,0,0,0,0,1]
random.shuffle(chambers)
player=1

#The death function checks the value of the current chamber and depending on it, gives out the WIN/LOSE condition or continues the game.
#Per call, one cell on the chamber list is removed.
def death(target):
                chamber = chambers.pop(0)
                if chamber==1:
                        suspense()
                        print(f"\n{target} died\n")
                        return False
                else:
                        suspense()
                        print("\nNothing happens\n")
                        return True

#The suspense function creates a suspense factor by adding a timeout before the death function is done.
def suspense():
    for _ in range(3):
        print(".", flush=True)
        time.sleep(0.5)
        print()

#The shoot_y function makes the player call the death function on themselves.
def shoot_y():
    print(f"\nPlayer {player} shoots themselves.")
    return death(f"Player {player}")

#The spin function randomizes the position of the values in the chambers list.
def spin():
    random.shuffle(chambers)
    print(f"\nPlayer {player} spins the cylinder.")

#The shoot_o function makes the player call the death function on the opponent, and if it doesn't end the game, then call the death function on themselves.
def shoot_o():
    opponent= 3-player
    print(f"\nPlayer {player} shoots their opponent.")
    result=death(f"Player {opponent}")
    if result==False:
         return False
    else:
         print("\nThey survived")
         return shoot_y()

print("\nRUSSIAN ROULETTE")

while True:
    print(f"\nPlayer {player}, your turn.\n")
    print("\nType 1: SHOOT YOURSELF\n")
    print("Type 2: SPIN CYLINDER\n")
    print("Type 3: SHOOT OPPONENT\n")
    print("Type 4: QUIT\n")

    choice = int(input("Choose: "))
    

    if choice == 1:
        if shoot_y() == False:
            print("\nGame Over.\n")
            break

    elif choice == 2:
        spin()

    elif choice == 3:
        if shoot_o() == False:
            print("\nGame Over.\n")
            break

    elif choice == 4:
        print("\nGoodbye.\n")
        break

    else:
        print("\nInvalid choice\n")

    player= 3- player

    