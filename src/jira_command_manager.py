from JiraDataObjects.board import Board
from JiraDataObjects.sprint import Sprint
from config_manager import ConfigManager
from jira_connection_manager import JiraConnectionHandler
from JiraDataObjects.issue import Issue
from typing import Optional


class IllegalIssueName(Exception):
    """:exception caused by illegal issue name"""

    def __init__(self, issue_name):
        self.expression = issue_name
        self.message = "Issue name is not legal"


class NameMatchesMultipleBoards(Exception):
    """:exception caused by multiple boards matching a board name"""

    def __init__(self, boards):
        self.expression = boards
        self.message = "Multiple boards matches the name"


def _validate_issue_name(issue_name) -> None:
    if issue_name == '':
        raise IllegalIssueName(issue_name)


class JiraCommandManager:
    def __init__(self, config_manager: ConfigManager, connection_handler: JiraConnectionHandler):
        self._config_manager = config_manager
        self._connection_handler = connection_handler

    def get_issue(self, issue_name: str) -> Issue:
        _validate_issue_name(issue_name)
        return Issue(self._connection_handler.get_issue(issue_name))

    def print_issue(self, issue_name):
        self.get_issue(issue_name).pprint()

    def assign_issue(self, issue_name: str, username: Optional[str] = None):
        _validate_issue_name(issue_name)
        if not username:
            username = self._config_manager.get_username()
        issue = self.get_issue(issue_name)
        self._connection_handler.assign_issue(issue, username)

    def get_board(self, board_name: Optional[str] = None):
        board_name = board_name if board_name else self._config_manager.get_default_board()

        boards = self._connection_handler.get_boards(board_name)

        if len(boards) > 1:
            raise NameMatchesMultipleBoards(boards)

        return Board(boards.pop())

    def get_sprints(self, board: Board):
        return self._connection_handler.get_sprints(board.id)

    def get_active_sprint(self, board: Board):
        return Sprint(self._connection_handler.get_sprints(board.id, "active").pop(), board)

    def estimated_work_left_in_sprint(self, sprint: Sprint):
        return self._connection_handler.get_estimated_work_left_in_sprint(sprint.board.id, sprint.id)
