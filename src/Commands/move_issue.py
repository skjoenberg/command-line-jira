import string

from Commands.icommand import ICommand


class MoveIssue(ICommand):
    def __init__(self, transition: string):
        self._transition = transition

    @property
    def transition(self):
        return self._transition
