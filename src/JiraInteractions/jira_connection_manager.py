import string

from jira import JIRA, Issue as JiraIssue
from jira.resources import Sprint as JiraSprint

from Config.config_manager import ConfigManager
from JiraInteractions.JiraDataObjects.sprint import Sprint
from LoginManagement.login_manager import LoginManager
from CommandLine.command_line_utilities import write_to_console
from typing import Optional


def _print_cannot_connect_error_message():
    write_to_console(
        "Jira connection returned: 401 Unauthorized error.\n" +
        "The error is most likely causing by wrong login information. Try resetting your password"
    )


class JiraConnectionHandler:
    _jira_agile_connection: Optional[JIRA]
    _loginHandler: LoginManager

    def __init__(self, login_manager: LoginManager, config_manager: ConfigManager):
        self._loginHandler = login_manager
        self._server = config_manager.server
        self._jira_agile_connection = None
        self._jira_greenhopper_connection = None

    def _jira_agile(self):
        if self._jira_agile_connection is None:
            try:
                agile_parameters, _ = self._setup_connection_parameters()
                jira_agile_connection: JIRA = JIRA(
                    basic_auth=agile_parameters["basic_auth"],
                    options=agile_parameters["options"])
                self._jira_agile_connection = jira_agile_connection
            except RecursionError as _:
                _print_cannot_connect_error_message()
        return self._jira_agile_connection

    def _jira_greenhooper(self):
        if self._jira_greenhopper_connection is None:
            try:
                _, greenhopper_parameters = self._setup_connection_parameters()
                jira_greenhopper_connection: JIRA = JIRA(
                    basic_auth=greenhopper_parameters["basic_auth"],
                    options=greenhopper_parameters["options"])
                self._jira_greenhopper_connection = jira_greenhopper_connection
            except RecursionError as _:
                _print_cannot_connect_error_message()
        return self._jira_greenhopper_connection

    def _setup_connection_parameters(self):
        """Creates the parameters needed for establishing a connection to Jira"""
        auth = self._loginHandler.get_login_information()
        agile_options = {"server": self._server, "agile_rest_path": 'agile'}
        greenhopper_options = {"server": self._server}
        return {"basic_auth": auth, "options": agile_options}, {"basic_auth": auth, "options": greenhopper_options}

    def get_issue(self, issue_name) -> JiraIssue:
        """Gets an issue based on an issue name"""
        return self._jira_agile.issue(issue_name)

    def get_project(self, project_name):
        """Gets a project based on a project name"""
        return self._jira_agile.project(project_name)

    def assign_issue(self, issue_id: int, user: str) -> None:
        """Assigns a user to an issue"""
        self._jira_agile.assign_issue(issue_id, user)

    def get_boards(self, board_name: str) -> [dict]:
        """Gets a board based on a board name"""
        return self._jira_agile.boards(name=board_name)

    def get_sprints(self, board_id: int, state: Optional[str] = None) -> [dict]:
        """Gets the sprints related to a board"""
        return self._jira_agile.sprints(board_id, state=state)

    def get_estimated_work_left_in_sprint(self, board_id: int, sprint_id: int) -> int:
        """Gets the amount of work left in a sprint"""
        return self._jira_greenhopper.incompletedIssuesEstimateSum(board_id, sprint_id)

    def get_transitions(self, issue: JiraIssue):
        """Gets the possible transitions of an issue"""
        return self._jira_agile.transitions(issue)

    def log_work(self, username: string, issue: JiraIssue, minutes_spent: int) -> None:
        """Logs work on an issue"""
        self._jira_agile.add_worklog(issue.key,timeSpent=str(minutes_spent) + "m", user=username)

    def move_issue(self, issue: JiraIssue, transition: int):
        """Moves an issue given a transition id"""
        self._jira_agile.transition_issue(issue.key, transition)

    def get_issues_in_sprint(self, sprint: Sprint):
        """"""
        #return self._jira_agile.sprint_info(sprint.board.id, sprint.id)
        return self._jira_agile.search_issues("Sprint = {:d}".format(sprint.id))#, startAt=sprint.id, maxResults=1)
