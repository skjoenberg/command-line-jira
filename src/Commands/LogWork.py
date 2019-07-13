from Commands.ICommand import ICommand


class LogWork(ICommand):
    def __init__(self, minutes_spent):
        self._minutes_spent = minutes_spent

    @property
    def minutes_spent(self):
        return self._minutes_spent
