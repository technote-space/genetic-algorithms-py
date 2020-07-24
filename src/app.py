from runner import Runner
from targets import SantaFeTrail
from grape import Algorithm


def main():
    Runner(
        Algorithm(SantaFeTrail(), lambda algorithm: algorithm.draw()),
        1
    )


if __name__ == "__main__":
    main()
