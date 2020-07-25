import argparse
from runner import Runner
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
    parser.add_argument('-o', '--output', help='output file name', default='chromosome.json')
    args = parser.parse_args()

    io = IO(args.output)
    Runner(Algorithm(get_targets()[args.target](), io.save_chromosome))


if __name__ == "__main__":
    main()
