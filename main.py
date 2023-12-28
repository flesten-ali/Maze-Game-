import random

print("You are in the middle of a maze.")
point = 0
swords = 3
potions = 3
while True:
    print("Where to go? ")
    choice  = input("Left[L] Right[R] Up[U] Down[D]:")
    if choice!="L" and choice!="R" and choice!="U" and choice!="D":
        print("You entered invalid direction. The Game Ends!")
        break
    event  = random.choice(["M" ,"P","T" ,"E"])
    if event == "M":
        print("A monster!")
        if swords!=0:
            swords-=1
            point+=1
            print("You saved yourself with a sword.")
        else:
            print("You die. No swords left.")
            print("You lost. Game ends. Your points:",point)
            break
    elif event =="P":
        print("A poison!")
        if potions!=0:
            potions-=1
            point+=1
            print("You saved yourself with a potion.")
        else:
            print("You die. No potion left.")
            print("You lost. Game ends. Your points:",point)
            break

    elif event == "T":
        point+=2
        print("You earn two points!")
    else:
        point+=1
        print("An empty road. Go ahead!")

    print()
    print("Points:",point)
    print()