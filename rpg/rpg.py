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
        'north': 'Kitchen',
        'east': 'Bedroom',
        'item': 'note',
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
        'item': 'shovel'
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
            # Έλεγχος κλειδωμένου Office
            if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                if 'key' in inventory:
                    print("You use the key to unlock the Office.")
                    rooms[nextRoom]['locked'] = False
                    currentRoom = nextRoom
                else:
                    print("The Office is locked! You need a key.")
            else:
                currentRoom = nextRoom
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

    # Νίκη αν μαζέψεις όλα τα αντικείμενα
    if len(inventory) == 7:  # Προσθέσαμε treasure στο Attic
        print("You collected all items! You win!")
        break
