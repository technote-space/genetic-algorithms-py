import argparse
from runner import Runner
from targets import SantaFeTrail, CartPole
from grape import Algorithm


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
    args = parser.parse_args()

    Runner(Algorithm(get_targets()[args.target]()))


if __name__ == "__main__":
    main()
