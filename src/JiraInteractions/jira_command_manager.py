import string

from jira.resources import Board

from JiraInteractions.JiraDataObjects.board import Board
from JiraInteractions.JiraDataObjects.sprint import Sprint
from Config.config_manager import ConfigManager
from JiraInteractions.jira_connection_manager import JiraConnectionHandler
from JiraInteractions.JiraDataObjects.issue import Issue
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


class InvalidTransitionName(Exception):
    """:exception caused by a trying to perform a non-existing transition on an issue"""

    def __init__(self, transition_name: string, transitions: dict):
        self.expression = transition_name
        self.message = "Transition \"" + transition_name + "\" does not exist." \
        "Possible transtions are: " + ", ".join(transitions.keys)


def _validate_issue_name(issue_name) -> None:
    """Validates that the issue has a name"""
    if issue_name == '':
        raise IllegalIssueName(issue_name)


class JiraCommandManager:
    def __init__(self, config_manager: ConfigManager, connection_handler: JiraConnectionHandler):
        """Initialize Jira command manager"""
        self._config_manager = config_manager
        self._connection_handler = connection_handler

    def get_issue(self, issue_name: str) -> Issue:
        """Gets a Jira issue object based on the issue name"""
        _validate_issue_name(issue_name)
        return Issue(self._connection_handler.get_issue(issue_name))

    def print_issue(self, issue_name):
        """Pretty prints information about an issue to the command line"""
        self.get_issue(issue_name).pprint()

    def assign_issue(self, issue_name: str, username: Optional[str] = None):
        """Assigns a user to an issue"""
        _validate_issue_name(issue_name)

        if not username:
            username = self._config_manager.get_username()

        issue = self.get_issue(issue_name)
        self._connection_handler.assign_issue(issue, username)

    def get_board(self, board_name: Optional[str] = None) -> Board:
        """Gets a Jira board object based on the board name"""

        board_name = board_name if board_name else self._config_manager.get_default_board()
        boards = self._connection_handler.get_boards(board_name)

        if len(boards) > 1:
            raise NameMatchesMultipleBoards(boards)

        return Board(boards.pop())

    def get_sprints(self, board: Board) -> Sprint:
        """Gets the sprints related to a board"""
        return self._connection_handler.get_sprints(board.id)

    def get_transitions(self, issue: Issue):
        """Gets the possible transitions"""
        return self._connection_handler.get_transitions(issue.issue)

    def get_active_sprint(self, board: Board):
        """Gets the active sprint related to a board"""
        return Sprint(self._connection_handler.get_sprints(board.id, "active").pop(), board)

    def estimated_work_left_in_sprint(self, sprint: Sprint):
        """Gets the estimated amount of work left in the sprint"""
        return self._connection_handler.get_estimated_work_left_in_sprint(sprint.board.id, sprint.id)

    def log_work(self, issue: Issue, minutes_spent: int) -> None:
        """Logs work on an issue"""
        self._connection_handler.log_work(self._config_manager.username, issue.issue, minutes_spent)

    def move_issue(self, issue: Issue, transition_name: string) -> None:
        """Moves an issue given a transition"""
        transitions = self.get_transitions(issue)
        for transition_dict in transitions:
            if transition_dict["name"] == transition_name:
                self._connection_handler.move_issue(issue.issue, transition_dict["id"])
                return

        raise InvalidTransitionName(transition_name, transitions)
