from typing import Optional

from JiraDataObjects.board import Board
from JiraDataObjects.issue import Issue


class CommandLineInput():
    def __init__(self):
        self.issue: Optional[Issue] = None
        self.board: Optional[Board] = None

    def set_issue(self, issue: Issue):
        self.issue = issue

    def set_board(self, board: Board):
        self.board = board
