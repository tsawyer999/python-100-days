from typing import Self
import os
import copy
from time import sleep

WALL = "█"


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    @staticmethod
    def create_position(position: Self) -> Self:
        return Position(position.x, position.y)


class Maze:
    initial_position = Position(0, 1)
    final_position = Position(21, 3)
    map = [
        "██████████████████████",
        "  █     ███          █",
        "█ █ █ █   █ ████ █ ███",
        "█ █ █ ███ █ █  █ █ █  ",
        "█   █   █   ██   █   █",
        "██████████████████████"
    ]
    width = len(map[0])
    dept = len(map)

    def get_at(self, x: int, y: int) -> str:
        return self.map[y][x]


class Player:
    position: Position
    previous_position: Position

    def __init__(self, initial_position: Position) -> None:
        self.position = initial_position
        self.previous_position = initial_position


class Game:
    maze = Maze()
    player = Player(maze.initial_position)

    def move(self) -> bool:

        moved = self.try_move()
        if moved is False:
            self.player.previous_position = Position.create_position(self.player.position)
            moved = self.try_move()

        return moved

    def try_move(self):
        if self.move_east():
            return True

        if self.move_south():
            return True

        if self.move_west():
            return True

        if self.move_north():
            return True

        return False

    def move_north(self) -> bool:
        if self.player.position.y == 0:
            return False

        if self.player.previous_position.y == self.player.position.y - 1:
            return False

        future_map_item = self.maze.get_at(self.player.position.x, self.player.position.y - 1)
        if future_map_item == " ":
            self.player.previous_position = Position.create_position(self.player.position)
            self.player.position.y -= 1
            return True

        return False

    def move_east(self) -> bool:
        if self.player.position.x == self.maze.width - 1:
            return False

        if self.player.previous_position.x == self.player.position.x + 1:
            return False

        future_map_item = self.maze.get_at(self.player.position.x + 1, self.player.position.y)
        if future_map_item == " ":
            self.player.previous_position = Position.create_position(self.player.position)
            self.player.position.x += 1
            return True

        return False

    def move_south(self) -> bool:
        if self.player.position.y == self.maze.dept - 1:
            return False

        if self.player.previous_position.y == self.player.position.y + 1:
            return False

        future_map_item = self.maze.get_at(self.player.position.x, self.player.position.y + 1)
        if future_map_item == " ":
            self.player.previous_position = Position.create_position(self.player.position)
            self.player.position.y += 1
            return True

        return False

    def move_west(self) -> bool:
        if self.player.position.x == 0:
            return False

        if self.player.previous_position.x == self.player.position.x - 1:
            return False

        future_map_item = self.maze.get_at(self.player.position.x - 1, self.player.position.y)
        if future_map_item == " ":
            self.player.previous_position = Position.create_position(self.player.position)
            self.player.position.x -= 1
            return True

        return False

    def is_game_end(self) -> bool:
        return self.player.position.x == self.maze.final_position.x \
            and self.player.position.y == self.maze.final_position.y


def refresh_ui():
    ui = copy.deepcopy(game.maze.map)

    row = ui[game.player.position.y]
    part1 = row[:game.player.position.x]
    part2 = row[game.player.position.x + 1:]

    ui[game.player.position.y] = part1 + "X" + part2
    os.system('cls||clear')
    for line in ui:
        print(line)


game = Game()

while game.move():
    refresh_ui()
    sleep(0.1)
    if game.is_game_end():
        break

if game.is_game_end():
    print("You are free!")
else:
    print("Game Over")
