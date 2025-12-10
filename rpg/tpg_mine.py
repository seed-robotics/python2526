import pygame
pygame.init()

# --- Window setup ---
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini RPG with Pictures and Item Icons")

font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

# --- Rooms ---
rooms = {
    'Living Room': {'north': 'Garden West', 'east': 'Kitchen', 'south': 'Bedroom', 'item': 'key', 'image': 'living_room.jpg'},
    'Kitchen': {'north': 'Garden East', 'west': 'Living Room', 'south': 'Office', 'item': 'knife', 'image': 'kitchen.jpg'},
    'Bedroom': {'north': 'Living Room', 'east': 'Office', 'up': 'Attic', 'item': 'map', 'image': 'bedroom.jpg'},
    'Office': {'north': 'Kitchen', 'east': 'Bedroom', 'item': 'note', 'locked': True, 'image': 'office.jpg'},
    'Garden West': {'south': 'Living Room', 'east': 'Garden East', 'item': 'flower', 'image': 'garden_west.jpg'},
    'Garden East': {'south': 'Kitchen', 'west': 'Garden West', 'item': 'shovel', 'image': 'garden_east.jpg'},
    'Attic': {'down': 'Bedroom', 'item': 'treasure', 'image': 'attic.jpg'}
}

inventory = []
currentRoom = 'Living Room'

# --- Load images ---
def load_room_images():
    loaded = {}
    for name, data in rooms.items():
        img = pygame.image.load(f"./rpg/pictures/{data['image']}").convert()
        loaded[name] = pygame.transform.scale(img, (WIDTH, HEIGHT))
    return loaded

def load_item_images():
    names = ['key', 'knife', 'note', 'flower', 'shovel', 'map', 'treasure']
    imgs = {}
    for n in names:
        img = pygame.image.load(f"./rpg/pictures/{n}.png").convert_alpha()
        imgs[n] = pygame.transform.scale(img, (64, 64))
    return imgs

room_images = load_room_images()
item_images = load_item_images()

# --- Helper functions ---
def draw_room():
    # Draw background
    screen.blit(room_images[currentRoom], (0, 0))

    # If there's an item, draw it centered on screen
    if "item" in rooms[currentRoom]:
        item_name = rooms[currentRoom]["item"]
        item_img = item_images.get(item_name)
        if item_img:
            rect = item_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(item_img, rect)

    # Text overlay
    overlay = pygame.Surface((WIDTH, 120))
    overlay.set_alpha(160)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, HEIGHT - 120))

    # Info text
    lines = [
        f"You are in the {currentRoom}",
        f"Inventory: {', '.join(inventory) if inventory else 'Empty'}"
    ]
    if "item" in rooms[currentRoom]:
        lines.append(f"You see a {rooms[currentRoom]['item']}")
    else:
        lines.append("No items here.")


    pygame.display.flip()
    
# --- Game loop ---
running = True
while running:
    draw_room()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            move = None
            if event.key in (pygame.K_w, pygame.K_UP): move = 'north'
            elif event.key in (pygame.K_s, pygame.K_DOWN): move = 'south'
            elif event.key in (pygame.K_a, pygame.K_LEFT): move = 'west'
            elif event.key in (pygame.K_d, pygame.K_RIGHT): move = 'east'
            elif event.key == pygame.K_q: move = 'up'
            elif event.key == pygame.K_e: move = 'down'
            elif event.key == pygame.K_g: move = 'get'
            elif event.key == pygame.K_ESCAPE: running = False

            if move == 'get':
                if "item" in rooms[currentRoom]:
                    item = rooms[currentRoom]["item"]
                    inventory.append(item)
                    print(f"You picked up {item}")
                    del rooms[currentRoom]["item"]
                else:
                    print("Nothing to get here.")

            elif move in ['north', 'south', 'east', 'west', 'up', 'down']:
                if move in rooms[currentRoom]:
                    nextRoom = rooms[currentRoom][move]
                    if 'locked' in rooms[nextRoom] and rooms[nextRoom]['locked']:
                        if 'key' in inventory:
                            print("Door unlocked with your key!")
                            rooms[nextRoom]['locked'] = False
                            currentRoom = nextRoom
                        else:
                            print("The door is locked!")
                    else:
                        currentRoom = nextRoom
                else:
                    print("You can't go that way!")

    clock.tick(30)

pygame.quit()
