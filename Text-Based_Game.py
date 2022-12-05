# GREGIE JAY DELOS SANTOS
# PROFESSOR PATRICK MOORE
# IT-140: INTRODUCTION TO SCRIPTING
# OCTOBER 16, 2022

# TITLE: BAMBO UNLIMITED

# FUNCTION for the goal of the game + commands
def showInstructions():
    # PRINT instructions + Introductions + Commmands for player
    # PRINT Title
    print("BAMBO UNLIMITED")
    # PRINT Objective
    print("Reconcile 6 items to win the game, or be caught and executed by the Warlord.")
    # PRINT Commands for movement
    print("Move commands: go North, go East, go South, go West")
    # PRINT Commands for item retrieval
    print("Add to Inventory: get 'item name'")
    # PRINT Command for exiting the game
    print("To leave the game: Exit\n")

# FUNCTION for movement of player
def showStatus(current_room, move, rooms):
    # MOVE player to corresponding room
    current_room = rooms[current_room][move]
    return current_room

# FUNCTION for retrieval of items for player
def showItem(current_room, move, rooms, inventory):
    # ADD item into player inventory
    inventory.append(rooms[current_room]['item'])
    # REMOVE item from corresponding room
    del rooms[current_room]['item']

# MAIN FUNCTION for actions
def main():
    # DICTIONARY of rooms + corresponding items
    rooms = {
        'Forest': {'South': 'Warehouse', 'North': 'Church', 'East': 'Turret Bunker', 'West': 'Abandoned Hut'},
        'Warehouse': {'North': 'Forest', 'East': 'Trench', 'item': '9mm Beretta Pistol'},
        'Trench': {'West': 'Warehouse', 'item': 'Night Vision Goggles'},
        'Church': {'South': 'Forest', 'East': 'Watch Tower', 'item': 'Water Canteen'},
        'Watch Tower': {'West': 'Church', 'item': 'Remote Detonator'},
        'Abandoned Hut': {'East': 'Forest', 'item': 'C-4 Explosives'},
        'Turret Bunker': {'West': 'Forest', 'North': 'Warlord Compound', 'item': 'Satellite Radio'},
        'Warlord Compound': '',
    }
    s = ' '

    # LIST for player inventory
    inventory = []

    # START the player in the forest
    current_room = "Forest"

    # START the player with instructions
    showInstructions()

    # WHILE LOOP START
    # REPLAY FOREVER UNTIL CONDITIONS MET
    while True:
        # IF player reaches the Warlord Compound and faces Warmonger (Villian)
        if current_room == 'Warlord Compound':
            # WINNING GAME
            if len(inventory) == 6:
                print('\n************************************************')
                print('Congratulations!')
                print('You have defeated the warlord, Warmonger, and saved the world from world domination!')
                print('Thank you for playing!')
                print('************************************************\n')
                break
            # LOSING GAME
            else:
                print('\n************************************************')
                print('BANG! BANG! BOOM! You have been shot! You did NOT have ALL your items for the mission...')
                print('You were taken hostage by the Warlord, Warmonger!')
                print('MISSION FAILED.')
                print('Thank you for playing!')
                print('************************************************\n')
                break
            # IF Player enters 'exit' ==> 'Exit'
            # This EXIT option allows Player to EXIT LOOP and EXIT GAME
            if len(current_room) == 'Exit':
            #current_room = 'Exit'
                exitDialogue = """
                    You have requested to leave the game...
                    Thanks for playing!
                    """
                print(exitDialogue)
                break
        # OUTPUT status information of user for: current room, inventory, and prompt next action
        print('\nYou are in the ' + current_room)
        print('Inventory:', inventory)
        # OUTPUT notification about item in the room
        if current_room != 'Warlord Compound' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()
        # IF player enters command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = showStatus(current_room, move[1], rooms)
            continue
        # IF player enters command to retrieve an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[4:]) in rooms[current_room]['item']:
            print('\n>>>You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            showItem(current_room, move, rooms, inventory)
            continue
        # IF player enters an INVALID command
        else:
            print('\n***Invalid move, please try again***')
            continue

main()