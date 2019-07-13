import string
from argparse import Namespace
from pipe import Pipe

from CommandLine.command_line_input import CommandLineInput
from Commands import Status


@Pipe
def Map(args: Namespace) -> CommandLineInput:
    """Maps from Namespace (ArgParse) to CommandLineInput"""
    return CommandLineInput(args.type, args.id, create_command(args))


def create_command(args: Namespace):
    try:
        if args.status:
            return Status
    except:
        pass
    return Status

