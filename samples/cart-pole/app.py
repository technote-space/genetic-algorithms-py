from packages import Context, Algorithm, Runner


def main():
    context = Context()
    algorithm = Algorithm(context)
    runner = Runner(context, algorithm)
    runner.start()


if __name__ == "__main__":
    main()
