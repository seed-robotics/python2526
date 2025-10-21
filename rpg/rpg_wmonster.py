def showInstructions():
    print('''
          Mini RPG
          =========
          Commands:
          go [direction] (north, south, east, west, up, down)
          get [item]
          exit - to quit the game
          
          MAP:
          
     [Garden] ---- [Garden]
           |                |
      [Living Room] ---- [Kitchen]
           |                |
      [Bedroom] ------- [Office]
           |
        [Attic]
          
          Objective:
          Find the sword to defeat the monster!
          ''')

def showStatus():
    print('---------------------------')
    displayName = currentRoom
    if currentRoom.startswith("Garden"):
        displayName = "Garden"
    print('You are in the ' + displayName)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('---------------------------')

inventory = []

rooms = {
    'Living Room': {
        'north': 'Garden West',
        'east': 'Kitchen',
        'south': 'Bedroom',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Garden East',
        'west': 'Living Room',
        'south': 'Office',
        'item': 'knife'
    },
    'Bedroom': {
        'north': 'Living Room',
        'west': 'Office',
        'up': 'Attic',
        'item': 'map'
    },
    'Office': {
        'east': 'Bedroom',
        'north': 'Kitchen',
        'item': 'sword',  # place the sword here
        'locked': True
    },
    'Garden West': {
        'south': 'Living Room',
        'east': 'Garden East',
        'item': 'flower'
    },
    'Garden East': {
        'south': 'Kitchen',
        'west': 'Garden West',
        'item': 'monster'  # the monster is here
    },
    'Attic': {
        'down': 'Bedroom',
        'item': 'treasure'
    }
}

currentRoom = 'Living Room'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('> ').lower().split()

    if move[0] == 'go':
        direction = move[1]
        if direction in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][direction]
            
            # Check for locked room
            if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                if 'key' in inventory:
                    print("You use the key to unlock the Office.")
                    rooms[nextRoom]['locked'] = False
                    currentRoom = nextRoom
                else:
                    print("The Office is locked! You need a key.")
            else:
                currentRoom = nextRoom
                
                # Check if monster is in the room
                if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] == "monster":
                    if "sword" in inventory:
                        print("You found the monster and defeated it with your sword! You win!")
                        break
                    else:
                        print("You found the monster and you have no sword! You die...")
                        break
        else:
            print("You can't go that way!")

    elif move[0] == 'get':
        item = move[1]
        if "item" in rooms[currentRoom] and item == rooms[currentRoom]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del rooms[currentRoom]['item']
        else:
            print(f"Can't get {item}!")

    elif move[0] == 'exit':
        print("Game exited. Bye!")
        break

    # Win condition: collect all items (including sword, treasure, etc.)
    if "treasure" in inventory and "key" in inventory and "map" in inventory:
        print("You collected all items! You win!")
        break
