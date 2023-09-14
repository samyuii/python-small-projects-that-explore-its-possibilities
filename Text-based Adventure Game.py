class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def add_path(self, direction, room):
        self.paths[direction] = room

def create_game():
    start = Room("Start", "You are in a dark cave. There are two paths ahead.")
    left = Room("Left Path", "You find a treasure chest!")
    right = Room("Right Path", "You encounter a monster!")

    start.add_path("left", left)
    start.add_path("right", right)
    left.add_path("back", start)
    right.add_path("back", start)

    return start

def play_game(start_room):
    current_room = start_room

    while True:
        print(f"You are in the {current_room.name}. {current_room.description}")
        direction = input("Which path will you choose? ")
        
        if direction in current_room.paths:
            current_room = current_room.paths[direction]
        else:
            print("You can't go that way!")

if __name__ == '__main__':
    game_start = create_game()
    play_game(game_start)
