import string

from Commands import ICommand


class CommandLineInput:
    def __init__(self, type: string, id: string, command: ICommand):
        """Read-only dto for command line input"""
        self._id = id
        self._type = type
        self._command = command

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def command(self):
        return self._command
