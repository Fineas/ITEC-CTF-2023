import random
import click
import signal

LEVELS = [
    [
        list("####################################"),
        list("#             #      #             #"),
        list("#  #######    #      #       #######"),
        list("#  #     #    #    ######    #     #"),
        list("## # ### #    #              # ### #"),
        list("#  # ### #########  #######  # ### #"),
        list("## # ### #    # ##  #     #  #     #"),
        list("#   ############ ## #     #    # ###"),
        list("#              # #  #     #   #  ###"),
        list("############## # ## #     # ##   ###"),
        list("#              # #  ### ### #    ###"),
        list("# ############## ## ###   # #    ###"),
        list("#              # #  ##### #      ###"),
        list("############## # ## #####   ########"),
        list("#                   # O            #"),
        list("####################################")
    ],
    [
        list("####################################"),
        list("#              #                   #"),
        list("#  #############  #############   ##"),
        list("#  #                #           # ##"),
        list("#  #  #############  #########   # #"),
        list("#  #  #              #       #     #"),
        list("#  #  #  #############  #    #### ##"),
        list("#  #o #           #  #  #       # ##"),
        list("#  ####  ##########  #  ######  # ##"),
        list("#     #           #  ##         # ##"),
        list("#  #### ############  ##########  ##"),
        list("#  #           #   #              ##"),
        list("#  #  ########## ######   ##########"),
        list("#  #  #              #        #   ##"),
        list("#  #  #  #############   #   #   ###"),
        list("#     #                    #   #O###"),
        list("####################################")
    ],
    [
        list("####################################"),
        list("#        #         #   #   #      ##"),
        list("#  #######  #  #############  ## o #"),
        list("#  #        #           #     #  # #"),
        list("#  #  #############  ###  ######## #"),
        list("#  #  #              #        #    #"),
        list("#  #  #  #######  #  ##### ## #    #"),
        list("#  #  #        #  #  #        ##   #"),
        list("#  #  ##########  #  #  ##### #### #"), 
        list("#  #              #     ##       # #"),
        list("#  #############  #####  ######  # #"),
        list("#         ##             ##      # #"),
        list("#########  ############# #  ###### #"),
        list("#                        ####      #"),
        list("#  #############################   #"),
        list("####################################")
    ]
]

MAZE_SIZE = 36
WALL = "#"
EMPTY = " "
PLAYER = "P"
NEXT = "O"
PREV = "o"
WIN = "W"
level = 0

DIRECTIONS = {
    "sus": (0, -1),
    "jos": (0, 1),
    "stanga": (-1, 0),
    "dreapta": (1, 0)
}

def clrscr():
    click.clear()

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]

    start = (1, 1)
    end = (random.randint(1, width - 1), height - 2)

    maze = carve_maze(start, end, maze)
    maze[start[1]][start[0]] = "P"
    maze[end[1]][end[0]] = "W"

    for i in range(36):
        maze[0][i] = '#'
        maze[35][i] = '#'
        maze[i][0] = '#'
        maze[i][35] = '#'

    return maze


def carve_maze(start, end, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    maze[start[1]][start[0]] = "P"
    maze[end[1]][end[0]] = "W"

    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        current = stack.pop()

        random.shuffle(directions)

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if next_cell[0] >= 0 and next_cell[0] < len(maze[0]) and next_cell[1] >= 0 and next_cell[1] < len(maze) and next_cell not in visited:
                maze[(current[1] + next_cell[1]) // 2][(current[0] + next_cell[0]) // 2] = " "
                maze[next_cell[1]][next_cell[0]] = " "

                stack.append(next_cell)
                visited.add(next_cell)

                if next_cell == end:
                    return maze

    return carve_maze((1, 1), (random.randint(1, len(maze[0]) - 1), len(maze) - 2), maze)


def print_maze(maze, lvl):
    print("  ----------- LEVEL  " + str(lvl) + " ----------- ")
    for row in maze:
        print("".join(row))


def get_move():
    while True:
        print()
        move = input("Enter a move (sus/jos/stanga/dreapta): ")
        if move in DIRECTIONS:
            return DIRECTIONS[move]


def play_lvl(lvl):
    if lvl < 3:
        maze = LEVELS[lvl]
    else:
        maze = generate_maze(MAZE_SIZE, MAZE_SIZE)

    player = (1, 1)
    maze[player[1]][player[0]] = PLAYER
    clrscr()
    print_maze(maze, lvl)

    at = ''

    while 1:

        dx, dy = get_move()

        x, y = player
        nx, ny = x + dx, y + dy

        if maze[ny][nx] == NEXT:
            at = 'O'
            return at

        if maze[ny][nx] == PREV:
            at = 'o'
            return at

        if maze[ny][nx] == WIN:
            at = 'W'
            return at

        if maze[ny][nx] != WALL:
            maze[y][x] = EMPTY
            player = (nx, ny)
            maze[ny][nx] = PLAYER

        clrscr()
        print_maze(maze, lvl)

def main():
    global level 

    result = ''

    while level < 4:

        if result == "O":
            level += 1
            result = play_lvl(level)

        elif result == "o":
            result = play_lvl(level - 1)

        elif result == 'W':
            print("ITEC{redacted}")
            return

        else:
            result = play_lvl(0)

def handler_function():
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM,handler_function) 
    signal.alarm(10) 

    main()