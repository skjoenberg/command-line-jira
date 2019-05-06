import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Command line interface for JIRA.')
    parser.add_argument('-b', '--board', metavar='Board', nargs='1', help='The relevant board')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
