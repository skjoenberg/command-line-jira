from jira import JIRA, Issue as JiraIssue

from LoginManagement.login_manager import LoginManager
from CommandLine.command_line_utilities import write_to_console
from typing import Optional


class JiraConnectionHandler:
    _jira_agile: Optional[JIRA]
    _loginHandler: LoginManager

    def __init__(self, login_manager: LoginManager):
        self._loginHandler = login_manager
        self._jira_agile = None
        self._jira_greenhopper = None

        self._establish_connection()

    def _establish_connection(self):
        try:
            agile_parameters, greenhopper_parameters = self._setup_connection_parameters()

            jira_agile_connection: JIRA = JIRA(
                basic_auth=agile_parameters["basic_auth"],
                options=agile_parameters["options"])

            jira_greenhopper_connection: JIRA = JIRA(
                basic_auth=greenhopper_parameters["basic_auth"],
                options=greenhopper_parameters["options"])

            self._jira_agile = jira_agile_connection
            self._jira_greenhopper = jira_greenhopper_connection

        except RecursionError as _:
            write_to_console(
                "Jira connection returned: 401 Unauthorized error.\n" +
                "The error is most likely causing by wrong login information. Try resetting your password"
            )

    def _setup_connection_parameters(self):
        server_url = "http://wip.schantz.com"
        auth = self._loginHandler.get_login_information()
        agile_options = {"server": server_url, "agile_rest_path": 'agile'}
        greenhopper_options = {"server": server_url}
        return {"basic_auth": auth, "options": agile_options}, {"basic_auth": auth, "options": greenhopper_options}

    def get_issue(self, issue_name) -> JiraIssue:
        return self._jira_agile.issue(issue_name)

    def get_project(self, project_name):
        return self._jira_agile.project(project_name)

    def assign_issue(self, issue_id: int, user: str) -> None:
        self._jira_agile.assign_issue(issue_id, user)

    def get_boards(self, board_name: str) -> [dict]:
        return self._jira_agile.boards(name=board_name)

    def get_sprints(self, board_id: int, state: Optional[str] = None) -> [dict]:
        return self._jira_agile.sprints(board_id, state=state)

    def get_estimated_work_left_in_sprint(self, board_id: int, sprint_id: int) -> int:
        return self._jira_greenhopper.incompletedIssuesEstimateSum(board_id, sprint_id)

    def get_transitions(self, issue: JiraIssue):
        return self._jira_agile.transitions(issue)