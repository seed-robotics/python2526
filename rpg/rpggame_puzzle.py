import sys

# -------------------------------
# Game Data
# -------------------------------

inventory = []

rooms = {
    'Living Room': {'north': 'Garden West', 'east': 'Kitchen', 'south': 'Bedroom', 'item': 'key'},
    'Kitchen': {'north': 'Garden East', 'west': 'Living Room', 'south': 'Office', 'item': 'knife'},
    'Bedroom': {'north': 'Living Room', 'west': 'Office', 'up': 'Attic', 'item': 'map'},
    'Office': {'east': 'Bedroom', 'north': 'Kitchen', 'item': 'sword', 'locked': True, 'key': 'key'},
    'Garden West': {'south': 'Living Room', 'east': 'Garden East', 'item': 'flower'},
    'Garden East': {'south': 'Kitchen', 'west': 'Garden West', 'item': 'monster'},
    'Attic': {'down': 'Bedroom', 'item': 'treasure', 'locked': True}  # Puzzle will unlock
}

currentRoom = 'Living Room'

# -------------------------------
# Functions
# -------------------------------

def showInstructions():
    print('''
Mini RPG
=========
Commands:
go [direction] (north, south, east, west, up, down)
get [item]
exit - to quit the game

Objective:
Find the sword and survive the monster!
''')

def showStatus():
    displayName = currentRoom
    if currentRoom.startswith("Garden"):
        displayName = "Garden"
    print('---------------------------')
    print('You are in the ' + displayName)
    print('Inventory:', inventory)
    
    if "map" in inventory:
        print('''
      MAP:
    [Garden] ---- [Garden]
       |                |
    [Living Room] ---- [Kitchen]
       |                |
    [Bedroom] ------- [Office]
       |
    [Attic]
        ''')

    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('---------------------------')

def process_command(move):
    global currentRoom
    
    if move[0] == 'go':
        if len(move) < 2:
            print("Go where?")
            return
        direction = move[1]
        if direction in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][direction]
            
            # Office locked by key
            if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                # Attic uses puzzle
                if nextRoom == 'Attic':
                    print("The door to the Attic is locked by a puzzle!")
                    answer = input("Solve this math puzzle to enter:\n"
                                   "I am a two-digit number. My tens digit is 3 more than my ones digit. "
                                   "If you reverse my digits, the number increases by 9. What number am I? ")
                    if answer.strip() == "41":
                        print("Correct! The door unlocks.")
                        rooms[nextRoom]['locked'] = False
                        currentRoom = nextRoom
                        showStatus()
                    else:
                        print("Wrong! The door remains locked.")
                        return
                # Office uses key
                else:
                    required_key = rooms[nextRoom].get('key')
                    if required_key in inventory:
                        print(f"You use the {required_key} to unlock the {nextRoom}.")
                        rooms[nextRoom]['locked'] = False
                        currentRoom = nextRoom
                        showStatus()
                    else:
                        print(f"The {nextRoom} is locked! You need a {required_key}.")
                        return
            else:
                currentRoom = nextRoom
                # Monster encounter
                if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] == "monster":
                    if "sword" in inventory:
                        print("You encounter the monster but have the sword! You survive.")
                        del rooms[currentRoom]['item']
                    else:
                        print("You encounter the monster and have no sword! You die...")
                        sys.exit()
                showStatus()
        else:
            print("You can't go that way!")

    elif move[0] == 'get':
        if len(move) < 2:
            print("Get what?")
            return
        item = move[1]
        if "item" in rooms[currentRoom] and item == rooms[currentRoom]['item']:
            inventory.append(item)
            print(f"{item} got!")
            if item == "map":
                print("You found the map! The full map is now visible.")
            del rooms[currentRoom]['item']
            showStatus()
        else:
            print(f"Can't get {item}!")

    elif move[0] == 'exit':
        print("Game exited. Bye!")
        sys.exit()
    else:
        print("Unknown command!")

# -------------------------------
# Start Game
# -------------------------------

showInstructions()
while True:
    showStatus()
    move = input('> ').lower().split()
    if move:
        process_command(move)
    
    # Win condition: all items collected
    required_items = ['treasure', 'key', 'map', 'sword']
    if all(x in inventory for x in required_items):
        print("You collected all main items and survived the monster! You win!")
        break
