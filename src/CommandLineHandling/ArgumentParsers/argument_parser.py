from ..argument_stack import ArgumentStack


class ArgumentParser:
    def __init__(self, command_identifiers, action):
        self._command_identifiers = command_identifiers
        self._action = action

    def applies(self, argument_stack: ArgumentStack):
        if argument_stack.next() in self._command_identifiers:
            argument_stack.pop()
            self._action(argument_stack)
