def showInstructions():
    print('''
          Mini RPG
          =========
          Commands:
          go [direction] (north, south, east, west, up, down)
          get [item]
          exit - to quit the game
          ''')
def showMap():
    print('''      
          MAP:
          
      [Garden] -----------[Garden]
           |                |
      [Living Room] ---- [Kitchen]
           |                |
      [Bedroom] ------- [Office]
           |
          ud
           |
        [Attic]
          ''')

def showStatus():
    print('---------------------------')
    displayName = currentRoom
    # if currentRoom.startswith("Garden"):
    #     displayName = "Garden"
    print('You are in the ' + displayName)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    else:
        print("No items here!")
    print('---------------------------')
    if 'map' in inventory:
        showMap()
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
        'east': 'Office',
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
nextRoom =''

while True:
    showStatus()
    move=''
    while move=='':
        move = input('> ').lower().split()

    if move[0]=='go':
        direction=move[1]
        if direction in rooms[currentRoom]:
            nextRoom=rooms[currentRoom][direction]
            if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                if 'key' in inventory:
                    print("you have the key so door unlocked!")
                    rooms[nextRoom]['locked'] = False
                    currentRoom = nextRoom
                else:
                    print("You need the key to get in!")
            else:
                currentRoom = nextRoom
        else:
            print("You can't go that way!")
    elif move[0]=='get':
        item=move[1]
        if "item" in rooms[currentRoom] and item == rooms[currentRoom]['item']:
            inventory.append(rooms[currentRoom]["item"])
            del rooms[currentRoom]['item']
        else:
            print(f"Can't get {item}!")
    else:
        print("wrong input")