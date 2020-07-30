import argparse
from runner import Runner
from player import Player
from targets import get_choices
from grape import Algorithm
from tools import IO, Make, Process


def main() -> None:
    parser = argparse.ArgumentParser(description='Genetic Algorithm for Python')
    parser.add_argument('target', help='target', choices=get_choices())
    parser.add_argument('-f', '--file', help='file name', default='chromosome.json')
    parser.add_argument('-r', '--result', help='result file name', default='result.txt')
    parser.add_argument('-d', '--dir', help='executable file directory', default='program')
    parser.add_argument('-p', '--player', help='player mode', action='store_true')
    parser.add_argument('-l', '--load', help='cpu load', default=15, type=float)
    args = parser.parse_args()

    file: str = args.file
    result: str = args.result
    player: bool = args.player
    target: str = args.target
    directory: str = args.dir
    load: float = args.load

    io = IO(file, result)
    if player:
        Player(target, io.load_chromosome())
    else:
        Process()
        make = Make(directory)
        Runner(Algorithm(target, io.draw, io.save_chromosome, io.save_result, make.generate), load)


if __name__ == "__main__":
    main()
