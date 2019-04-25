from jira import JIRA
from issue import Issue
from login_manager import LoginManager
from CommandLineHandling.command_line_utilities import write_to_console
from typing import Optional


class JiraConnectionHandler:
    _jira: Optional[JIRA]
    _loginHandler: LoginManager

    def __init__(self, login_manager: LoginManager):
        self._loginHandler = login_manager
        self._jira = None

        self._establish_connection()

    def _establish_connection(self):
        try:
            parameters = self._setup_connection_parameters()
            jira_connection: JIRA = JIRA(basic_auth=parameters["basic_auth"], options=parameters["options"])
            self._jira = jira_connection
        except RecursionError as _:
            write_to_console(
                "Jira connection returned: 401 Unauthorized error.\n" +
                "The error is most likely causing by wrong login information. Try resetting your password"
            )

    def _setup_connection_parameters(self):
        options = {
            "server": "http://wip.schantz.com",
        }
        return {
            "basic_auth": self._loginHandler.get_login_information(),
            "options": options
        }

    def get_issue(self):
        Issue(self._jira.issue("APD-1638")).pprint()
