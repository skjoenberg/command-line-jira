from argparse import Namespace
from pipe import Pipe

from CommandLine.command_line_input import CommandLineInput
from Commands.sprint_issues import SprintIssues
from Commands.status import Status
from Commands.log_work import LogWork
from Commands.move_issue import MoveIssue


@Pipe
def Map(args: Namespace) -> CommandLineInput:
    """Maps from Namespace (ArgParse) to CommandLineInput"""
    return CommandLineInput(args.type, args.id, create_command(args))


def create_command(args: Namespace):
    try:
        if args.status:
            return Status
    except AttributeError:
        pass

    try:
        if args.log_work:
            return LogWork(args.minutes)
    except AttributeError:
        pass

    try:
        if args.move_issue:
            return MoveIssue(args.transition)
    except AttributeError:
        pass

    try:
        if args.show_issues:
            return SprintIssues(args.show_issues)
    except AttributeError:
        pass

    # Default to status
    return Status

