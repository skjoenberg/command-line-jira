from jira.resources import Sprint as JiraSprint
from JiraDataObjects.board import Board


class Sprint:
    def __init__(self, sprint: JiraSprint, board: Board):
        self.name = sprint.name
        self.id = sprint.id
        self.board = board
