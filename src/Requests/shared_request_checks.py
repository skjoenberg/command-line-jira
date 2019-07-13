from CommandLine.command_line_input import CommandLineInput
from Commands.Status import Status


def is_issue(command_line_input: CommandLineInput):
    """Checks whether the type of the command line input is an issue"""
    return command_line_input.type == "issue"


def is_status_command(command_line_input: CommandLineInput):
    """Checks whether the command line input is a status command"""
    return isinstance(command_line_input.command, Status)


def is_status_command(command_line_input: CommandLineInput):
    """Checks whether the command line input is a status command"""
    return isinstance(command_line_input.command, Status)
