import pygame
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

room_positions = {
    'Garden West': (100, 50),
    'Garden East': (200, 50),
    'Living Room': (100, 150),
    'Kitchen': (200, 150),
    'Bedroom': (100, 250),
    'Office': (200, 250),
    'Attic': (100, 350)
}

currentRoom = 'Living Room'
has_map = False
input_text = ""
font_size = 20

# -------------------------------
# Pygame Setup
# -------------------------------

pygame.init()
screen = pygame.display.set_mode((450, 500))
pygame.display.set_caption("Mini RPG")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, font_size)

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (30,30,30)
YELLOW = (255,255,0)

# -------------------------------
# Functions
# -------------------------------

def draw_map():
    screen.fill(BLACK)
    # Draw rooms
    for room, pos in room_positions.items():
        if has_map:
            pygame.draw.rect(screen, WHITE, (*pos, 50,50),2)
        else:
            pygame.draw.rect(screen, GRAY, (*pos,50,50))
    # Draw items if map visible
    if has_map:
        for room, pos in room_positions.items():
            if "item" in rooms[room]:
                item = rooms[room]['item']
                color = WHITE
                if item=="monster": color=RED
                elif item=="sword": color=YELLOW
                elif item in ["key","map","treasure","knife","flower"]: color=GREEN
                pygame.draw.circle(screen,color,(pos[0]+25,pos[1]+25),5)
    # Draw player
    pos = room_positions[currentRoom]
    pygame.draw.circle(screen,BLUE,(pos[0]+25,pos[1]+25),10)

def draw_input():
    input_surface = font.render("> "+input_text,True,WHITE)
    screen.blit(input_surface,(10,460))

def show_status_console():
    global has_map
    displayName = currentRoom
    if currentRoom.startswith("Garden"):
        displayName = "Garden"
    print('---------------------------')
    print('You are in the ' + displayName)
    print('Inventory:', inventory)
    if "map" in inventory:
        has_map=True
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
        print('You see a '+rooms[currentRoom]['item'])
    print('---------------------------')

def process_command(cmd):
    global currentRoom,has_map
    move = cmd.lower().split()
    if not move: return
    if move[0]=="go":
        if len(move)<2:
            print("Go where?")
            return
        direction = move[1]
        if direction in rooms[currentRoom]:
            nextRoom = rooms[currentRoom][direction]
            
            # Locked room
            if "locked" in rooms[nextRoom] and rooms[nextRoom]["locked"]:
                # Attic puzzle
                if nextRoom=="Attic":
                    print("The door to the Attic is locked by a puzzle!")
                    answer = input("Solve this math puzzle to enter:\n"
                                   "I am a two-digit number. My tens digit is 3 more than my ones digit. "
                                   "If you reverse my digits, the number increases by 9. What number am I? ")
                    if answer.strip()=="41":
                        print("Correct! The door unlocks.")
                        rooms[nextRoom]["locked"]=False
                        currentRoom = nextRoom
                        show_status_console()
                    else:
                        print("Wrong! The door remains locked.")
                        return
                # Office key
                else:
                    required_key = rooms[nextRoom].get("key")
                    if required_key in inventory:
                        print(f"You use the {required_key} to unlock the {nextRoom}.")
                        rooms[nextRoom]["locked"]=False
                        currentRoom = nextRoom
                        show_status_console()
                    else:
                        print(f"The {nextRoom} is locked! You need a {required_key}.")
                        return
            else:
                currentRoom = nextRoom
                # Monster
                if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]=="monster":
                    if "sword" in inventory:
                        print("You encounter the monster but have the sword! You survive.")
                        del rooms[currentRoom]["item"]
                    else:
                        print("You encounter the monster and have no sword! You die...")
                        pygame.quit()
                        sys.exit()
                show_status_console()
        else:
            print("You can't go that way!")
    elif move[0]=="get":
        if len(move)<2:
            print("Get what?")
            return
        item = move[1]
        if "item" in rooms[currentRoom] and item==rooms[currentRoom]["item"]:
            inventory.append(item)
            print(f"{item} got!")
            if item=="map":
                print("You found the map! The full map is now visible in Pygame.")
            del rooms[currentRoom]["item"]
            show_status_console()
        else:
            print(f"Can't get {item}!")
    elif move[0]=="exit":
        print("Game exited. Bye!")
        pygame.quit()
        sys.exit()
    else:
        print("Unknown command!")

# -------------------------------
# Start Game
# -------------------------------

print("Mini RPG - type commands in the Pygame window and press Enter")
print("Commands: go [direction], get [item], exit")

show_status_console()

while True:
    draw_map()
    draw_input()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                if input_text.strip():
                    process_command(input_text.strip())
                input_text=""
            elif event.key==pygame.K_BACKSPACE:
                input_text=input_text[:-1]
            else:
                input_text+=event.unicode

    # Win condition
    required_items = ["treasure","key","map","sword"]
    if all(x in inventory for x in required_items):
        print("You collected all main items and survived the monster! You win!")
        pygame.quit()
        sys.exit()
    
    clock.tick(30)
