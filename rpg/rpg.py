def showInstructions():
    #print a main menu and the commands
    print('''
          RPG Game
          ========

        Get to the Garden with a key and a potion
          Avoid the monsters!
          

          Commands:
          go [north south east west]
          get [item]
          ''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    if 'map' in inventory:
        drawMap()

def drawMap():
    print('''

[Garden] -----------[Garden]
|                      |
[Hall] --------- [Dining Room]
|                      |
[kitchen] --------- [Office]


          ''')

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms

rooms = {  
    'Hall' : {
         'south' : 'Kitchen',
         'east' : 'Dining Room',
         'north' : 'GardenWest',
        'item' : 'key'
       
    },
    'Kitchen' : {
        'north' : 'Hall',
        'east' : 'Office',
        'item' : 'map'
    },
    'Dining Room' : {
        'west' : 'Hall',
        'north' : 'GardenEast',
        'item' : 'potion',
        'south' : 'Office'
    },
    'GardenWest' : {
        'south' : 'Hall',
        'east' : 'GardenEast'
    },
    'GardenEast' :{
        'south' : 'Dining Room',
        'west' : 'GardenWest'
    }, 
    'Office' : {
        'north' : 'Dining Room',
        'west' : 'Kitchen', 
        'up' : 'PlayRoom',
        'locked' : True
    }, 
    'PlayRoom' : {
        'down' : 'Office'
    }
        
}


currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()
  
    if move[0] == 'go':
        direction = move[1]
        if direction in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][direction]
            if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                if 'key' in inventory:
                    print("you have the key so door unlocked!")
                    rooms[nextRoom]['locked'] = False
                    currentRoom = nextRoom
                else:
                    print('you cant go in this room,you need a key')
            else:
                currentRoom = nextRoom
        else:
            print('You can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
            