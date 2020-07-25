import argparse
from runner import Runner
from player import Player
from targets import SantaFeTrail, CartPole
from grape import Algorithm
from tools import IO


def get_targets():
    return {
        'santa-fe-trail': SantaFeTrail,
        'cart-pole': CartPole,
    }


def get_choices():
    return get_targets().keys()


def main():
    parser = argparse.ArgumentParser(description='Genetic Algorithm for Python')
    parser.add_argument('target', help='target', choices=get_choices())
    parser.add_argument('-f', '--file', help='file name', default='chromosome.json')
    parser.add_argument('-p', '--player', help='player mode', action='store_true')
    args = parser.parse_args()

    io = IO(args.file)
    target = get_targets()[args.target]()
    if args.player:
        Player(target, io.load_chromosome())
    else:
        Runner(Algorithm(target, io.save_chromosome))


if __name__ == "__main__":
    main()
