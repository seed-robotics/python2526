def showInstructions():
    #print a main menu and the commands
    print('''
          RPG Game
          ========
<<<<<<< HEAD
=======


        Get to the Garden with a key and a potion
          Avoid the monsters!
          
>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e
          Commands:
          go [direction]
          get [item]
          ''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
<<<<<<< HEAD
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
=======
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
>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e

#an inventory, which is initially empty
inventory = []
<<<<<<< HEAD

#a dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east'  : 'Dining room',
        'item'  : 'key'
    },
    'Kitchen' : {
        'north' : 'Hall',
        'west'  : 'Hall',
        'item'  : 'monster'
    },
    'Dining room' : {
        'west'  : 'Hall',
        'south'  : 'Garden',
        'east' : 'playroom',
        'item' : 'flashlight'
    },
    'garden' : {
        'north'  : 'Dining room',
        'south'  : 'Garden',
        'west' : 'exit',
        'item'  : 'potion'
    },
    'playroom' : {
       'west' : 'Dining Room',
        'item' : 'monster',
        'item' : 'potion'
    },
    'exit' : {
        'east' : 'Garden'
=======
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
>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e
    }
        
}
<<<<<<< HEAD

#start the player in the Hall
=======
>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()
<<<<<<< HEAD

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
=======
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
>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
<<<<<<< HEAD
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
=======
            print('Can\'t get ' + move[1] + '!')
     
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
            



>>>>>>> 3b39b7742062aad9f462370b4e3fe88bccc4c97e
