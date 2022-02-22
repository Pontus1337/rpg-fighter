
import resources
from resources import Character, Goblin, save_character, load_characters
from random import randint, shuffle, choice

def fight(players: list, enemies:list):
    participants= players+enemies # make initiative ordering
    shuffle(participants)

    for char in participants:
        target =""
        # is target a player or a monster?
        if char in players:
            target = choice(enemies)
        else:
            target = choice(players)


        target.take_damage(char.get_attack())
        
        if target.get_health()==0:
            print(f"{target.get_name()} has died!")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} has {target.get_health()} hp remaining")
        if len(enemies)==0 or len(players) ==0:
            break

if __name__ =="__main__":
    enemies=[]
    players= load_characters()

    # emy = Character("Emy", 20,5,2)
    # nick = Character("Nick", 15,2,1)
    # players.append(emy)
    # players.append(nick)

    enemies.append(Goblin(10,3,2,1))
    enemies.append(Goblin(15,2,1,2))
    enemies.append(Goblin(12,3,2,3))

    round =1
    while len(enemies) != 0 and len(players) != 0:
        print(f"ROUND {round}, FIGHT")
        fight(players, enemies)
        print()
        round+=1
    
    if len(enemies) == 0:
        print("The players won!")
        print("wolud you like to save the remaining characters?")
        save_choice = input("(y/n)")
        if save_choice =="y":
            save_character(players)
        else:
            print("no progress was saved.")

    elif len(players)==0:
        print("The Goblins won!")







