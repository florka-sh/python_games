print('''You are walking on the street and suddenly a truck hits you. After a some time 
you open your eyes and you get confused. You cannot recognise your surroundings, you are in another world!
The world you wake up is a fantasy world!!!
Infront of you are threee sets of equipmnt. ''')
print("--------------------------------")
#level.1
level_1_completed = False

while level_1_completed == False:
    A = "Mage"
    B = "Warrior"
    C = "Ranger"
    print('''
    A = "Mage set of armor. You will be a mage!"
    B = "Warrior set of armor. You will be a worrior!"
    C = "Range set of armor. You will be a shooter!"''')
    print()
    print()
    print("---------------")
    print("Pick a set of armor. A,B,C")

    pick_a_set_of_armot = input()

    if pick_a_set_of_armot == "A":
        print("You pick a mage class! Congratulation.")
        level_1_completed = True
    elif pick_a_set_of_armot == "B":
        print("You pick a warrior class! Congratulation.")
        level_1_completed = True
    elif pick_a_set_of_armot == "C":
        print("You pick a ranger class! Congratulation.")
        level_1_completed = True
    else:
        print("You need to make a choice, there is not much time left!!!")


# Level 2
print('''There is a town(T) close to you. There will be a 
quests for you or you can go in the dungeon(D) and try 
your new equipment.''')
print("Pick T(town) or D(dungeon)")

pick_path = input()
level_2_completed = False
while level_2_completed == False:
    if pick_path == "D":
        print("You enterd the dungeon")
        print("There is a bear!!! Whar do you do ? RUN or FITH?")
        choice = input()
        if choice == "RUN":
            print("You survived")
            print("Go to town. You can train there.")
            pick_path = "T"

        elif choice == "FITH":
            print("You are to weak")
            print("Your are dead!!")
            print ("Game over")
            break
        else:
            print("You need to make a choice!!!")
            
    elif pick_path == "T":
        print("Welcome to Camelot.")
        print(" New adventures are waitintg for you.")
        level_2_completed = True
    else:
        print("You need to make a choice")

