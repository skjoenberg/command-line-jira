from CommandLine.command_line_input import CommandLineInput
from CommandLine.command_line_utilities import write_to_console
from Requests.IssueRequests.IssuePrintRequest import IssuePrintRequest
from Requests.IssueRequests.IssueStatusRequest import IssueStatusRequest
from Config.config_manager import ConfigManager
from jira_command_manager import JiraCommandManager
from jira_connection_manager import JiraConnectionHandler
from login_manager import LoginManager


class RequestController:
    def __init__(self):
        config_manager = ConfigManager()
        login_handler = LoginManager(config_manager.get_username())
        self._jch = JiraConnectionHandler(login_handler)
        self._jcm = JiraCommandManager(config_manager, self._jch)
        self._request_types = []

        self.initialize_request_types()

    def initialize_request_types(self):
        self._request_types.append(IssueStatusRequest())
        self._request_types.append(IssuePrintRequest())

    def execute_request(self, command_line_input: CommandLineInput):
        for request_type in self._request_types:
            if request_type.has_required_parameters(command_line_input):
                output = request_type.execute(self._jcm, command_line_input)
                write_to_console(output)
                break
