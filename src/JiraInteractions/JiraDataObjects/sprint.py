from jira.resources import Sprint as JiraSprint
from JiraInteractions.JiraDataObjects.board import Board


class Sprint:
    def __init__(self, sprint: JiraSprint, board: Board):
        self._name = sprint.name
        self._id = sprint.id
        self._board = board

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def board(self):
        return self._board
