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

    issue_parser.add_subparsers() | _add_log_work_subparser | _add_move_issue_subparser

    issue_parser.add_argument('-s', '--status', action='store_true', help='Gets the current status')

    issue_parser.set_defaults(type='issue')
    return subparsers


@Pipe
def _add_log_work_subparser(subparsers: _SubParsersAction):
    """Creates a subparser for logging work"""
    log_work_parser = subparsers.add_parser("log-work", aliases=["lw"], help="Logs work on an issue")
    log_work_parser.add_argument('minutes', metavar="MINUTES", help='Minutes of work to log')

    log_work_parser.set_defaults(log_work=True)
    return subparsers


@Pipe
def _add_move_issue_subparser(subparsers: _SubParsersAction):
    """Creates a subparser for logging work"""
    move_issue_parser = subparsers.add_parser("move", aliases=["mv"], help="Moves an issue from one status to another")
    move_issue_parser.add_argument("transition", metavar="TRANSITION", help="The transition to perform on the issue")

    move_issue_parser.set_defaults(move_issue=True)
    return subparsers


@Pipe
def _add_board_subparser(subparsers: _SubParsersAction) -> _SubParsersAction:
    """Creates a subparser for interacting with boards"""
    board_parser = subparsers.add_parser("board", aliases=['b'], help="Jira board")

    board_parser.add_argument('id', metavar='ID', help="Identifier of the object (Eg. \"Scrum Board\")")

    board_parser.add_argument("-si", "--show-issues", nargs="?", metavar="SPRINT", const="current",
                              help="Shows the issues on the board in a given sprint (Default: Current sprint)")

    board_parser.set_defaults(type='board')
    return subparsers


@Pipe
def _add_get_issues_in_sprint_subparser(subparsers: _SubParsersAction):
    """Creates a subparser for logging work"""
    get_issues_in_sprint_parser = subparsers.add_parser("issues", aliases=["i"], help="Prints the issues on the board")
    get_issues_in_sprint_parser.add_argument("-si", "--show-issues", nargs="?", metavar="SPRINT", help="Specifies the sprint")

    get_issues_in_sprint_parser.set_defaults(issues_in_sprint=True)
    return subparsers
