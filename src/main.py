
import resources
from resources import Character, Goblin
from random import randint

if __name__ =="__main__":
    nemy = Character("Nemy", 20,5,2)
    goblin_one = Goblin(10,3,1)

    print(nemy)
    print()
    print(goblin_one)

    fight_round = 1
    print("============Fight=============")
    while nemy.get_health()!=0 and goblin_one.get_health()!=0:
        print(f"round {fight_round} ")
        nemy_attack = nemy.damage()*randint(1,3)
        goblin_one.take_damage(nemy_attack)
        if (goblin_one.get_health()==0):
            print("goblin has died.")
            break
        else:
            print(f" goblin has {goblin_one.get_health()}hp left.")
            goblin_attack=goblin_one.damage()*randint(1,3)
            nemy.take_damage(goblin_attack)
            print(f"Nemy has {nemy.get_health()}hp left")
            if (nemy.get_health()==0):print("nemy has died.")
        fight_round+=1
    if(nemy.get_health()==0): print("the goblin won!")
    else:print("nemy has won")
