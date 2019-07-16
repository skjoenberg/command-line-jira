from Commands.icommand import ICommand


class SprintIssues(ICommand):
    def __init__(self, sprint_id):
       self._sprint_id = sprint_id

    @property
    def sprint_id(self):
        return self._sprint_id
