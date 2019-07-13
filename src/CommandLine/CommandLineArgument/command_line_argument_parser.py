from pipe import *
import argparse
import string
from argparse import ArgumentParser, Namespace, _SubParsersAction

from CommandLine.command_line_utilities import get_command_line_arguments


def parse_arguments() -> Namespace:
    """Parses the arguments given in the command line"""

    return get_command_line_arguments() | _default_no_arguments_to_help | _parse_cmd_args


@Pipe
def _default_no_arguments_to_help(cmd_args: [string]) -> [string]:
    """Defaults zero arguments to the --help command"""
    if len(cmd_args) == 0:
        return ["-h"]

    return cmd_args


@Pipe
def _parse_cmd_args(cmd_args: [string]) -> Namespace:
    return _setup_argument_parser().parse_args(cmd_args)


def _setup_argument_parser() -> ArgumentParser:
    """Creates the argument parser for Command Line Jira"""

    return argparse.ArgumentParser(description='Command line interface for JIRA.') | _add_jira_objects_subparsers


@Pipe
def _add_jira_objects_subparsers(parser: ArgumentParser) -> ArgumentParser:
    """Adds issue and board subparsers to main parser"""
    parser.add_subparsers(help="Jira object to interact with:") | _add_issue_subparser | _add_board_subparser
    return parser


@Pipe
def _add_issue_subparser(subparsers: _SubParsersAction) -> _SubParsersAction:
    """Creates a subparser for interacting with issues"""

    issue_parser = subparsers.add_parser("issue", aliases=['i'], help="Jira issue")
    issue_parser.add_argument('id', metavar='ID', help='Identifier of the object (Eg. ISSUE-189)')
    issue_parser.add_argument('-s', '--status', action='store_true', help='Gets the current status')
    issue_parser.set_defaults(type='issue')
    return subparsers


@Pipe
def _add_board_subparser(subparsers: _SubParsersAction) -> _SubParsersAction:
    """Creates a subparser for interacting with boards"""

    board_parser = subparsers.add_parser("board", aliases=['b'], help="Jira board")
    board_parser.set_defaults(type='board')
    return subparsers
