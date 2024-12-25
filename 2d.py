import os
import sys
import tty
import termios

class Room:
    def __init__(self, width, height, walls, items=None):
        self.width = width
        self.height = height
        self.walls = walls
        self.items = items or []

def create_basic_room(width, height):
    walls = [(x, 0) for x in range(width)] + \
            [(x, height-1) for x in range(width)] + \
            [(0, y) for y in range(height)] + \
            [(width-1, y) for y in range(height)]
    return Room(width, height, walls)


def create_maze_room(width, height):
    walls = create_basic_room(width, height).walls
    for x in range(2, width-2):
        for y in range(2, height-2, 2):
            walls.append((x, y))
    return Room(width, height, walls)

rooms = [
    create_basic_room(20, 10),
    create_maze_room(20, 10)
]

current_room = rooms[1]  # Start with the first room
MAP_WIDTH = current_room.width
MAP_HEIGHT = current_room.height
walls = current_room.walls


# Game map dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 10

# Player position
player_x = MAP_WIDTH // 2
player_y = MAP_HEIGHT // 2

def clear_screen():
    os.system('clear')

def draw_map():
    for y in range(current_room.height):
        for x in range(current_room.width):
            if (x, y) in current_room.walls:
                print("#", end="")
            elif x == player_x and y == player_y:
                print("@", end="")
            else:
                print(".", end="")
        print()



def get_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch.lower()

def move_player(direction):
    global player_x, player_y
    new_x, new_y = player_x, player_y
    
    if direction == 'w':
        new_y -= 1
    elif direction == 's':
        new_y += 1
    elif direction == 'a':
        new_x -= 1
    elif direction == 'd':
        new_x += 1
    
    if (new_x, new_y) not in current_room.walls:
        player_x, player_y = new_x, new_y


def main():
    while True:
        clear_screen()
        print(walls)
        print(f"player: ({player_x}, {player_y})")
        draw_map()
        print("\nUse WASD to move, Q to quit")
        
        key = get_input()
        
        if key == 'q':
            break
        elif key in ['w', 'a', 's', 'd']:
            move_player(key)

if __name__ == "__main__":
    main()
