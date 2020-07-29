import argparse
from runner import Runner
from player import Player
from targets import get_choices
from grape import Algorithm
from tools import IO
from tools import Make


def main() -> None:
    parser = argparse.ArgumentParser(description='Genetic Algorithm for Python')
    parser.add_argument('target', help='target', choices=get_choices())
    parser.add_argument('-f', '--file', help='file name', default='chromosome.json')
    parser.add_argument('-d', '--dir', help='executable file directory', default='program')
    parser.add_argument('-p', '--player', help='player mode', action='store_true')
    parser.add_argument('-l', '--load', help='cpu load', default=15, type=float)
    args = parser.parse_args()

    file: str = args.file
    player: bool = args.player
    target: str = args.target
    directory: str = args.dir
    load: float = args.load

    io = IO(file)
    if player:
        Player(target, io.load_chromosome())
    else:
        make = Make(directory)
        Runner(Algorithm(target, io.save_chromosome, make.generate), load)


if __name__ == "__main__":
    main()
