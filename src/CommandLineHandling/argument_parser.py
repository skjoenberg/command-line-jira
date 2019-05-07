import argparse
from argparse import ArgumentParser

from CommandLineHandling.command_line_input import CommandLineInput


def parse_arguments():
    parser = _setup_argument_parser()
    args = parser.parse_args()

    return args


def _setup_argument_parser():
    parser: ArgumentParser = argparse.ArgumentParser(description='Command line interface for JIRA.')
    parser.add_argument('type', choices=['issue', 'board'])
    parser.add_argument('id', metavar='ID', help='Identifier of the object (Eg. ISSUE-189)')
    parser.add_argument('-s', '--status', action='store_true', help='Gets the current status')

    return parser
